from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date


# создаем модель таблицы студентов
class Student(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[date]
    email: Mapped[str_uniq]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]
    course: Mapped[int]
    special_notes: Mapped[str_null_true]
    major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)

    major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)


# создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int_pk]
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)

# from sqlalchemy import Column, Integer, String, Date
# from app.database import Base
#
#
# # создаем модель таблицы студентов
# class Student(Base):
#     __tablename__ = "student"
#
#     id = Column(Integer, primary_key=True)
#     phone_number = Column(String(15), unique=True, nullable=False)
#     first_name = Column(String(30), unique=True, nullable=False)
#     last_name = Column(String(30), unique=True, nullable=False)
#     date_of_birth = Column(Date, nullable=False)
#     email = Column(String(255), unique=True, nullable=False)
#     address = Column(String(255), nullable=False)
#     enrollment_year = Column(Integer)
#     course = Column(Integer)
#     special_notes = Column(String(255), nullable=True)
#
#     def __str__(self):
#         return (f"{self.__class__.__name__}(id={self.id}, "
#                 f"first_name={self.first_name!r},"
#                 f"last_name={self.last_name!r})")
#
#     def __repr__(self):
#         return str(self)
#
#
# # создаем модель таблицы факультетов (majors)
# class Major(Base):
#     __tablename__ = "major"
#
#     id = Column(Integer, primary_key=True)
#     major_name = Column(String(30), unique=True, nullable=False)
#     major_description = Column(String(255), unique=True, nullable=False)
#     count_students = Column(Integer)
#
#     def __str__(self):
#         return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"
#
#     def __repr__(self):
#         return str(self)
