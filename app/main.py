from http.client import HTTPException

from fastapi import FastAPI

from old_models.models import Student, UpdateFilter, StudentUpdate, DeleteFilter
from js_db import add_student, upd_student, dell_student
from utils import json_to_dict_list
from typing import Optional, List

import os



# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()


@app.get("/student", response_model=Student)
def get_student_from_param_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list

@app.get("/students/id")
def get_all_students_student_id(student_id: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    if student_id is None:
        return students
    else:
        for student in students:
            if student["student_id"] == student_id:
                filtered_students.append(student)
    return filtered_students

@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018) -> List[Student]:
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students


@app.get("/")
def home_page():
    return {"message": "Привет!"}


@app.post("/add_student")
def add_student_handler(student: Student):
    student_dict = student.dict()
    check = add_student(student_dict)
    if check:
        return {"message": "Студент успешно добавлен!"}
    else:
        return {"message": "Ошибка при добавлении студента"}


@app.put("/update_student")
def update_student_handler(filter_student: UpdateFilter, new_data: StudentUpdate):
    check = upd_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Информация о студенте успешно обновлена!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")


@app.delete("/delete_student")
def delete_student_handler(filter_student: DeleteFilter):
    check = dell_student(filter_student.key, filter_student.value)
    if check:
        return {"message": "Студент успешно удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")
