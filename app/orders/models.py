from app.database import Base, int_pk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import func
from typing import TYPE_CHECKING, List

from app.order_items_association import order_item_association_table
if TYPE_CHECKING:
    from app.items.models import Item

class Order(Base):
    id: Mapped[int_pk]
    promocode: Mapped[str|None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now,
                                                 server_default=func.now())
    items: Mapped[List["Item"]] = relationship(
        secondary=order_item_association_table,
        back_populates='orders')

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"order_id={self.id!r}")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "promocode": self.promocode,
            "created_at": self.created_at
        }