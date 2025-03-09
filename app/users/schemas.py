from datetime import datetime
import re
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия студента, от 1 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта студента")
    password: str = Field(...,min_length=6, max_length=20, description="Пароль")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value


class UserAuth(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")

class UserChangeType(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr = Field(..., description="Электронная почта")
    is_user: bool = Field(False, description="Пользователь")
    is_student: bool = Field(False, description="Студент")
    is_teacher: bool = Field(False, description="Преподаватель")
    is_admin: bool = Field(False, description="Администратор")
    is_super_admin: bool = Field(False, description="Супер администратор")
