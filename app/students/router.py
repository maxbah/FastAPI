from fastapi import APIRouter, Depends
from app.students.schemas import Student
from app.students.dao import StudentDAO
from app.students.rb import RBStudent

router = APIRouter(prefix='/students', tags=['Работа со студентами'])


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[Student]:
    return await StudentDAO.find_all(**request_body.to_dict())

@router.get("/{id}", summary="Получить одного студента по id")
async def get_one_student_by_id(student_id: int) -> Student | dict:
    result = await StudentDAO.find_one_or_none_by_id(student_id)
    return {"message": f"Студент с айди {student_id} не найден!"} if result is None else result

@router.get("/by_filter", summary="Получить одного студента по фильтру")
async def get_one_student_by_filter(request_body: RBStudent = Depends()) -> Student | dict:
    result = await StudentDAO.find_one_or_none_by_filter(**request_body.to_dict())
    return {"message": f"Студент по заданному фильтру не найден!"} if result is None else result
