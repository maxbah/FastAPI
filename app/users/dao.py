from sqlalchemy import update
from sqlalchemy.exc import SQLAlchemyError

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import User


class UserDAO(BaseDAO):
    model = User

    # @classmethod
    # async def update_user_type(cls, filter_by, **values):
    #     async with async_session_maker() as session:
    #         async with session.begin():
    #             query = (
    #                 update(cls.model)
    #                 .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
    #                 .values(**values)
    #                 .execution_options(synchronize_session="fetch")
    #             )
    #             print(f'QueRY:', query)
    #             result = await session.execute(query)
    #             try:
    #                 await session.commit()
    #             except SQLAlchemyError as e:
    #                 await session.rollback()
    #                 raise e
    #             return result.rowcount
