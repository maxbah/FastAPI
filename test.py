# from datetime import date
# from http.client import responses
#
# from pydantic import ValidationError
#
# from old_models.models import Student

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
#
# student_data = {
#     "student_id": 1,
#     "phone_number": "+1234567890",
#     "first_name": "Иван",
#     "last_name": "Иванов",
#     "date_of_birth": date(2000, 1, 1),
#     "email": "ivan.ivanov@example.com",
#     "address": "Москва, ул. Пушкина, д. Колотушкина",
#     "enrollment_year": 2042,
#     "major": "Информатика",
#     "course": 6,
#     "special_notes": "Увлекается программированием"
# }
#
#
# def test_valid_student(data: dict) -> None:
#     try:
#         student = Student(**data)
#         print(student)
#     except ValidationError as e:
#         print(f"Ошибка валидации: {e}")
#
#
#
# print(f'RES: {test_valid_student(student_data)}')

# API testing using httpx
import asyncio
from itertools import count

import httpx


# async def add_major(major_name: str, major_description: str):
#     url = 'http://127.0.0.1:8000/majors/add/'
#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/json'
#     }
#     data = {
#         "major_name": major_name,
#         "major_description": major_description,
#         "count_students": 0
#     }
#     async with httpx.AsyncClient() as client:
#         resp = await client.post(url, headers=headers, json=data)
#         print('RESP: ', resp)
#         return resp.json()
#
# # вызов функции
# response = asyncio.run(add_major(major_name='Философия', major_description='Тут мы обучаем философов'))
# print(response)

class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def meth_mult(self):
        return self.a*self.b
    def method_sum(self):
        return 'instance method called', self, self.a+self.b
    @classmethod
    def classmethod_sum(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'A static method called'

class Min(Sum):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def method_min(self):
        super().method_sum()
        return self.a - self.b
    @classmethod
    def class_method_min(cls):
        return cls
    @staticmethod
    def stat_min():
        return 'B Static method'
#
# s = Sum(2,3)
# print(s.method_sum())

# m=Min(4, 3)
# print(m.method_min())
# print(m.method_min())
# print(m.method_sum())
# print(m.meth_mult())

class Singleton():

    __isinstance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.__isinstance is None:
    #         cls.__isinstance = super(Singleton, cls).__new__(cls, *args, **kwargs)
    #     return cls.__isinstance

sin1 = Singleton()
sin2 = Singleton()

print(sin1.__dir__)
print(sin2.__dir__)
print(sin1 is sin2)

def decor(c, d):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print(1)
            func(c, d, *args, **kwargs)
            print(2)
        return wrapper
    return decorate


@decor(1, 2)
def to_decorate(c, d, a, b):
    print(f'Decorated {a+b+c+d}')


print(to_decorate(3,5))


class N:
    count = 0

    def __init__(self):
        self.__class__.count += 1

    @classmethod
    def obj_count(cls):
        return cls.count


x = N()
print(x.obj_count())
n = N()
print(n.obj_count())


k=('a', 'b', 'c', 'd')
d={'a2':'a1', 'b':'b', 'c':'c1', 'd':'d'}

for i in k:
    print(i)
print(*k +(1,))
print(d)
print(*d)


