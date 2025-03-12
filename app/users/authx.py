# Авторизация с использованием библиотеки authx
from fastapi import APIRouter

from authx import AuthXConfig, AuthX

config = AuthXConfig()
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME="my_acces_token"
config.JWT_TOKEN_LOCATION = ["cookies"]


auth = AuthX(config=config)
# auth.handle_errors(app)
