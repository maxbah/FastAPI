
from sqlalchemy import Table, Column, ForeignKey, Integer
from app.database import Base


order_item_association_table = Table(
    "order_item_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("orders.id"), nullable=False),
    Column("item_id", ForeignKey("items.id"), nullable=False),
    Column("count", Integer, default=1, server_default="1", nullable=False)
)
