from fastapi import APIRouter, Depends
from app.students.schemas import Student, StudentAdd, StudentInfoUpdate
from app.students.dao import StudentDAO
from app.students.rb import RBStudent

router = APIRouter(prefix='/students', tags=['Работа со студентами'])


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[Student]:
    return await StudentDAO.find_all(**request_body.to_dict())

@router.get("/{id}", summary="Получить одного студента по id")
async def get_one_student_by_id(student_id: int) -> Student | dict:
    result = await StudentDAO.get_all_student_info(student_id)
    return {"message": f"Студент с айди {student_id} не найден!"} if result is None else result

@router.get("/by_filter", summary="Получить одного студента по фильтру")
async def get_one_student_by_filter(request_body: RBStudent = Depends()) -> Student | dict:
    result = await StudentDAO.find_one_or_none_by_filter(**request_body.to_dict())
    return {"message": f"Студент по заданному фильтру не найден!"} if result is None else result

@router.post("/add/", summary='Добавление нового студента')
async def add_student(student: StudentAdd) -> dict:
    check = await StudentDAO.add_student(**student.dict())
    if check:
        return {"message": "Студент успешно добавлен!", "student": student}
    else:
        return {"message": "Ошибка при добавлении студента!"}

@router.put("/update_student_info/", summary="Обновление данных студента")
async def update_student_major_id(student: StudentInfoUpdate) -> dict:
    check = await StudentDAO.update_student_major(filter_by={"last_name": student.last_name},
                                                  phone_number=student.phone_number,
                                                  address=student.address,
                                                  major_id = student.major_id
                                                  )
    return {"message": f"Данные студента {student.last_name} успешно обновлены"} if check \
        else {"message": "Ошибка обновления данных студента"}

@router.delete("/dell/{student_id}", summary="Удаление студента по айди")
async def del_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.del_student(student_id)
    return {"message": f"Студент с айди {student_id} успешно удален"} if check \
        else {"message": f"Ошибка удаления студента с айди {student_id}"}
