
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.orders.models import Order
from app.items.models import Item
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class OrderDAO(BaseDAO):
    model = Order

    @classmethod
    async def get_orders_with_items(cls) -> list[Order]:
        async with async_session_maker() as session:
            stmt=(
                select(Order).options(selectinload(Order.items)).order_by(Order.id)
            )
            orders = await session.scalars(stmt)
            return list(orders)

    @classmethod
    async def create_order(cls, **order_data: dict) -> Order:
        async with async_session_maker() as session:
            new_order = Order(**order_data)
            session.add(new_order)
            await session.commit()
            return new_order

    @classmethod
    async def create_item(cls, **item_data: dict) -> Item:
        async with async_session_maker() as session:
            new_item = Item(**item_data)
            session.add(new_item)
            await session.commit()
            return new_item

    @classmethod
    async def create_order_item(cls, **order_data: dict):
        async with async_session_maker() as session:
            order1 = await cls.create_order(**order_data)
            order_promo = await cls.create_order(**{"promocode": "promo"})

            mouse = await cls.create_item(**{
                "item_name": "mouse",
                "item_description": "new mouse",
                "count": 10,
                "price": 100
            })
            monitor = await cls.create_item(**{
                "item_name": "monitor",
                "item_description": "new monitor 21 inch",
                "count": 5,
                "price": 150
            })
            keyboard = await cls.create_item(**{
                "item_name": "keyboard",
                "item_description": "new keyboard ",
                "count": 7,
                "price": 77
            })
            order1 = await session.scalar(
                select(Order).where(Order.id == order1.id).options(selectinload(Order.items))
            )
            order_promo = await session.scalar(
                select(Order).where(Order.id == order_promo.id).options(selectinload(Order.items))
            )
            order1.items.append(mouse)
            order_promo.items.append(mouse)
            order_promo.items.append(monitor)
            order_promo.items.append(keyboard)

            await session.commit()
            return order_promo.id
