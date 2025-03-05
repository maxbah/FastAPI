
from app.dao.base import BaseDAO
from app.students.models import Student


class StudentDAO(BaseDAO):
    model = Student