from app.dao.base import BaseDAO
from app.majors.models import Major
from app.database import async_session_maker
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete
from sqlalchemy.exc import SQLAlchemyError


class MajorDAO(BaseDAO):
    model = Major

    @classmethod
    async def update_major_descr(cls, filter_by, **values):
        async with (async_session_maker() as session):
            async with session.begin():
                query = (
                    sqlalchemy_update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session="fetch")
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount

    @classmethod
    async def del_major(cls, **filter_by) -> dict:
        async with async_session_maker() as session:
            async with session.begin():
                del_query = sqlalchemy_delete(cls.model).filter_by(**filter_by)
                res = await session.execute(del_query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return res.rowcount