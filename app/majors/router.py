from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_session_maker
from app.majors.models import Major


router = APIRouter(prefix='/majors', tags=['Работа с факультетами'])


@router.get("/", summary="Получить все факультеты")
async def get_all_majors():
    async with async_session_maker() as session:
        query = select(Major)
        result = await session.execute(query)
        students = result.scalars().all()
        return students
