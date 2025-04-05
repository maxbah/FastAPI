from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.items.models import Item


class Order(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    promocode: str = Field(..., description="Промокод товара")
    created_at: datetime = Field(..., description="Время создания заказа")
    #items: list["Item"] = Field(..., description="Список товаров")