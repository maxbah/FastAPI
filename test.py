from datetime import date

from pydantic import ValidationError

from old_models.models import Student

# def get_stud_id_param_request(st_id: int):
#     url = "http://127.0.0.1:8000/students/id"
#     response = requests.get(url, params={"student_id": st_id})
#     return response.json()
#
#
# students = get_stud_id_param_request(7)
# for s in students:
#     print(s)
#
#
# def get_stud_id_param_path(st_id: int):
#     url = f"http://127.0.0.1:8000/students/{st_id}"
#     response = requests.get(url)
#     return response.json()
#
#
# students = get_stud_id_param_path(st_id=2)
# print("P P:", students)
#
#
# def get_all_students():
#     url = "http://127.0.0.1:8000/students"
#     response = requests.get(url)
#     return response.json()
#
#
# students = get_all_students()
# print('All stud list')
# for i in students:
#     print(i)
#
#
# def get_stud_with_param_reqest(course: int):
#     url = "http://127.0.0.1:8000/students"
#     response = requests.get(url, params={"course": course})
#     return response.json()
#
#
# students = get_stud_with_param_reqest(3)
# print(' 3 course stud list:')
# for s in students:
#     print(s)
#
#
# def get_students_with_param_path(course: int):
#     url = f"http://127.0.0.1:8000/students/{course}"
#     response = requests.get(url)
#     return response.json()
#
#
# students = get_students_with_param_path(2)
# for student in students:
#     print(student)
#
#
# def get_students_with_param_mix(course: int, major: Optional[str], enrollment_year: int):
#     url = f"http://127.0.0.1:8000/students/{course}"
#     response = requests.get(url, params={"major": major, "enrollment_year": enrollment_year})
#     return response.json()
#
#
# students = get_students_with_param_mix(2, major=None, enrollment_year=2018)
# print(students)

student_data = {
    "student_id": 1,
    "phone_number": "+1234567890",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_of_birth": date(2000, 1, 1),
    "email": "ivan.ivanov@example.com",
    "address": "Москва, ул. Пушкина, д. Колотушкина",
    "enrollment_year": 2042,
    "major": "Информатика",
    "course": 6,
    "special_notes": "Увлекается программированием"
}


def test_valid_student(data: dict) -> None:
    try:
        student = Student(**data)
        print(student)
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")



print(f'RES: {test_valid_student(student_data)}')