from pydantic_settings import BaseSettings

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'fast_api'
DB_USER = 'postgres'
DB_PASSWORD = 'admin'


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str


def get_db_url():
    return (f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@"
            f"{DB_HOST}:{DB_PORT}/{DB_NAME}")
