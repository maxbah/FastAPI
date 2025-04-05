from typing import TYPE_CHECKING, List

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, str_null_true, int_pk
from app.order_items_association import order_item_association_table

if TYPE_CHECKING:
    from app.orders.models import Order

class Item(Base):
    id: Mapped[int_pk]
    item_name: Mapped[str]
    item_description: Mapped[str_null_true]
    count: Mapped[int] = mapped_column(default=0, server_default=text('0'))
    price: Mapped[int]
    orders: Mapped[List["Order"]] = relationship(
        secondary= order_item_association_table,
        back_populates='items')

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"item_name={self.item_name!r}")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "item_name": self.item_name,
            "item_description": self.item_description,
            "count": self.count,
            "price": self.price
        }