from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.items.models import Item


class ItemDAO(BaseDAO):
    model = Item

    @classmethod
    async def add_item(cls, **item_data: dict):
        async with async_session_maker() as session:
            new_item=Item(**item_data)
            session.add(new_item)
            await session.flush()
            new_item_id = new_item.id
            await session.commit()
            return new_item_id
