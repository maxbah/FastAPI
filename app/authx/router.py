import asyncio

from authx.exceptions import MissingTokenError
from fastapi import APIRouter, Depends, HTTPException, Response, BackgroundTasks
from passlib.context import CryptContext

from app.background_tasks import synk_send_email
from app.users.authx import auth, config
from app.users.dao import UserDAO
from app.users.schemas import UserAuth, User


router = APIRouter(prefix='/authx', tags=['AuthX  авторизация'])
email_router = APIRouter(prefix='/bg_tasks', tags=['Фоновые задачи'])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@email_router.post("/send_email")
async def send_email(bg_task: BackgroundTasks):
    # for async
    #asyncio.current_task(synk_send_email())
    # for synk
    bg_task.add_task(synk_send_email)
    return {"message": "All emails were sent"}


@router.post('/loginx', summary='Аутентификация через AuthX')
async def login(user_cred: UserAuth, response: Response):
     user = await UserDAO.find_one_or_none_by_filter(email=user_cred.email)
     if user is None:
          return {"message": f"User with {user_cred.email} not found"}
     if user_cred.email != user.email and pwd_context.verify(user.password, pwd_context.hash(user_cred.password)):
         raise HTTPException(401, detail={"message": "Invalid credentials"})
     token = auth.create_access_token(uid=user_cred.email)
     response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
     return {"access_token": token}

@router.get("/protectedx", summary="Доступ к скрытым данным",
            dependencies=[Depends(auth.access_token_required)])
def get_protected():
     try:
          return {"message": "Secured data"}
     except MissingTokenError as e:
          raise HTTPException(401, detail={"message": str(e)}) from e
