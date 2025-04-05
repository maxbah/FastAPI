from fastapi import APIRouter, Depends
from app.orders.dao import OrderDAO
from app.orders.schemas import Order


router = APIRouter(prefix='/orders', tags=['Работа с заказами'])

@router.post("/add/", summary="Новый заказ")
async def add_order(order: Order) -> dict:
    print('ORDER DICT:', order)
    check = await OrderDAO.create_order_item(**order.dict())
    if check:
        return {"message": "Заказ успешно создан!", "order": order}
    else:
        return {"message": "Ошибка создания заказа!"}

@router.get("/orders_items/", summary="Все заказы с товарами")
async def get_order_item() -> dict:
    check = await OrderDAO.get_orders_with_items()
    for order in check:
        print(f"Order: {order.id}, {order.promocode}, ITEMS:")
        for i in order.items: # type: Item
            print(f"Items: {i}")
    if check:
        return {"message": "Список заказов с товарами"}
    else:
        return {"message": "Ошибка получения списка заказов с товарами!"}
