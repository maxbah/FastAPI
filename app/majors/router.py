from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_session_maker
from app.majors.dao import MajorDAO
from app.majors.models import Major
from app.majors.schemas import MajorAdd, MajorUpdateDescr

router = APIRouter(prefix='/majors', tags=['Работа с факультетами'])


@router.get("/", summary="Получить все факультеты")
async def get_all_majors():
    async with async_session_maker() as session:
        query = select(Major)
        result = await session.execute(query)
        students = result.scalars().all()
        return students

@router.post("/add/", summary='Добавление нового факультета')
async def add_major(major: MajorAdd) -> dict:
    check = await MajorDAO.add(**major.dict())
    return {"message": f"{major.major_name} факультет успешно добавлен"} if check \
        else {"message": "Ошибка при добавлении факультета"}

@router.put("/update_descr/", summary="Изменить описание факультета")
async def update_major_descr(major: MajorUpdateDescr) -> dict:
    check =  await MajorDAO.update_major_descr(filter_by={"major_name": major.major_name},
                                   major_description=major.major_description)
    return {"message": f"Данные факультета {major.major_name} обновлены"} if check \
        else {"message": f"Данные факультета {major.major_name} не были обновлены"}

@router.delete("/del/{major_id}", summary="Удаление факультета")
async def dell_major(major_id: int) -> dict:
    check = await MajorDAO.del_major(id=major_id)
    print(f"CHECK: {check}")
    return {"message": f"Факультет c ID {major_id} успешно удален"} if check == 1 \
        else {"message": f"Ошибка удаления Факультета c ID {major_id}"}
