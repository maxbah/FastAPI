
from pydantic import BaseModel, ConfigDict, Field


class ItemAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    item_name: str = Field(..., description='имя товара')
    item_description: str = Field(..., description='описание товара')
    count: int = Field(..., description='количество товара')
    price: int = Field(..., description='цена товара')

class Item(ItemAdd):
    model_config = ConfigDict(from_attributes=True)

class ItemUpdate(ItemAdd):
    model_config = ConfigDict(from_attributes=True)
    item_description: str = Field(..., description='описание товара')
    count: int = Field(..., description='количество товара')
    price: int = Field(..., description='цена товара')
