import asyncio
import os

from authx.exceptions import MissingTokenError
from fastapi import APIRouter, Depends, HTTPException, Response, BackgroundTasks, UploadFile
from passlib.context import CryptContext
from starlette.responses import FileResponse, StreamingResponse

from app.background_tasks import synk_send_email
from app.users.authx import auth, config
from app.users.dao import UserDAO
from app.users.schemas import UserAuth

router = APIRouter(prefix='/authx', tags=['AuthX  авторизация'])
files_router = APIRouter(prefix='/files', tags=['Работа с файлами'])
email_router = APIRouter(prefix='/bg_tasks', tags=['Фоновые задачи'])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@files_router.post("/files")
async def upload_file(upl_f: UploadFile):
    file = upl_f.file
    f_name = upl_f.filename
    fp = os.path.join('uploaded_files', f_name)
    with open(fp, "wb") as f:
        f.write(file.read())


@files_router.post("/mult_files")
async def mult_upload_files(upl_f: list[UploadFile]):
    for f in upl_f:
        file = f.file
        f_name = f.filename
        fp = os.path.join('uploaded_files', f_name)
        with open(fp, "wb") as f_f:
            f_f.write(file.read())


@files_router.get("/files/{f_name}")
async def get_file(f_name: str):
    f_path = os.path.join("uploaded_files", f_name)
    return FileResponse(f_path)


# Функция генератор которая будет брать файл частями и возвращать
def iter_file(f_name: str):
    f_path = os.path.join("uploaded_files", f_name)
    with open(f_path, 'rb') as f:
        while chunk := f.read(1024 * 1024):
            yield chunk


@files_router.get('/files/streaming/{f_name}')
async def get_stream_file(f_name: str):
    f_type = os.path.basename(f_name).split(".")[1]
    return StreamingResponse(iter_file(f_name), media_type=f"video/{f_type}")


@email_router.post("/send_email")
async def send_email(bg_task: BackgroundTasks):
    # for async
    # asyncio.current_task(synk_send_email())
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

@router.post('/logoutx', summary='Разлогиниться через AuthX')
async def logout_user(response: Response):
    response.delete_cookie(key=config.JWT_ACCESS_COOKIE_NAME)
    return {'message': 'Пользователь успешно вышел из системы'}