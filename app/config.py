from pydantic_settings import BaseSettings

DB_HOST = 'localhost'
#DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'fast_api'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
SECRET_KEY='gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt'
ALGORITHM='HS256'

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str


def get_db_url():
    #return "postgresql+asyncpg://fast_api_bysy_user:LpWxVgVkIvi3mmglbGEU2ercJvAe3xE9@dpg-cvc2gh2n91rc73cgbbsg-a.oregon-postgres.render.com/fast_api_bysy"
    return (f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@"
            f"{DB_HOST}:{DB_PORT}/{DB_NAME}")


def get_auth_data():
    return {"secret_key": SECRET_KEY, "algorithm": ALGORITHM}
