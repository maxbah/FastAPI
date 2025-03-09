from sqlalchemy import select, insert, update, event, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.majors.models import Major
from app.students.models import Student


class StudentDAO(BaseDAO):
    model = Student

    @classmethod
    async def get_all_student_info(cls, student_id: int) -> dict | None:
        async with async_session_maker() as session:
            query_stud = select(cls.model).options(joinedload(cls.model.major)).filter_by(id=student_id)
            result = await session.execute(query_stud)
            student_info = result.scalar_one_or_none()
            if student_info is None:
                return None
            stud_data = student_info.to_dict()
            stud_data['major'] = student_info.major.major_name
            return stud_data

    @classmethod
    async def add_student(cls, **student_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_student = Student(**student_data)
                session.add(new_student)
                await session.flush()
                new_student_id = new_student.id
                await session.commit()
                return new_student_id

    @event.listens_for(Student, 'after_insert')
    def receive_after_insert(mapper, connection, target):
        major_id = target.major_id
        connection.execute(
            update(Major)
            .where(Major.id == major_id)
            .values(count_students=Major.count_students + 1)
        )

    @classmethod
    async def update_student_major(cls, filter_by, **values):
        async with async_session_maker() as session:
            async with session.begin():
                upd_query = (
                    update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session="fetch")
                )
                res = await session.execute(upd_query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return res.rowcount


    @classmethod
    async def del_student(cls, student_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=student_id)
                res = await session.execute(query)
                student_to_del = res.scalar_one_or_none()
                if not student_to_del:
                    return None
                # dell stud
                await session.execute(delete(cls.model).filter_by(id=student_id))
                await session.commit()
                return student_id


    @event.listens_for(Student, 'after_delete')
    def receive_after_delete(mapper, connection, target):
        major_id = target.major_id
        connection.execute(
            update(Major)
            .where(Major.id == major_id)
            .values(count_students=Major.count_students - 1)
        )
