# Пример кастомной авторизации с использование jwt
from jose import jwt
from datetime import datetime, timedelta, timezone

from pydantic import EmailStr

from app.config import get_auth_data
from passlib.context import CryptContext

from app.users.dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UserDAO.find_one_or_none_by_filter(email=email)
    if not user or verify_password(plain_password=password, hashed_password=user.password) is False:
        return None
    return user
