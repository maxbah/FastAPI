from fastapi import APIRouter, Depends

from app.items.dao import ItemDAO
from app.items.rb import RBItem
from app.items.schemas import ItemAdd, Item, ItemUpdate

router = APIRouter(prefix='/items', tags=['Работа с товарами'])


@router.get("/", summary="получить все товары")
async def get_all_items(request_body: RBItem = Depends()) -> list[Item]:
    return await ItemDAO.find_all(**request_body.to_dict())


@router.post("/add/", summary="Добавить новый товар")
async def add_items(item: ItemAdd) -> dict:
    print('ITEM DICT:', item)
    check = await ItemDAO.add_item(**item.dict())
    if check:
        return {"message": "товар успешно добавлен!", "item": item}
    else:
        return {"message": "Ошибка при добавлении товара!"}


@router.put("/update_item/", summary="Обновить существующий товар")
async def update_item(item: ItemUpdate) -> dict:
    check = await ItemDAO.update(filter_by={"item_name": item.item_name},
                                 item_description=item.item_description,
                                 count=item.count, price=item.price)
    return {"message": f"Данные товара {item.item_name} успешно обновлены"} if check \
        else {"message": "Ошибка обновления данных товара"}


@router.delete("/dell/{item_id}", summary= "Удаление товара по айди")
async def dell_item_by_id(item_id: int) -> dict:
    check = await ItemDAO.del_by_id(item_id)
    return {"message": f"Товар с айди {item_id} успешно удален"} if check \
        else {"message": f"Ошибка удаления товара с айди {item_id}"}

