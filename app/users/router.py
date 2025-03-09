from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user, get_current_admin_user
from app.users.rb import RBUser
from app.users.schemas import User, UserAuth, UserChangeType

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/", summary="Регистрация нового пользователя")
async def register_user(user_data: User) -> dict:
    user = await UserDAO.find_one_or_none_by_filter(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UserDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


@router.post("/login/", summary="Вход")
async def user_auth(response: Response, user_data: UserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}

@router.get("/me/", summary="Показать данные текущего пользователя")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data

@router.post("/logout/", summary="Разлогиниться")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}

@router.get("/all_users/", summary="Вывести всех пользователей")
async def get_all_users(user_data: User = Depends(get_current_admin_user)):
    return await UserDAO.find_all()


@router.put("/update_type/", summary='Изменить тип пользователя')
async def change_type(user: UserChangeType, request_body: RBUser = Depends(get_current_admin_user)):
    all_users_data = await UserDAO.find_all()
    for u in all_users_data:
        if user.email == u.to_dict()['email']:
            check = await UserDAO.update(filter_by={'email': user.email},
                                         is_user=user.is_user,
                                         is_student=user.is_student,
                                         is_teacher=user.is_teacher,
                                         is_admin=user.is_admin,
                                         is_super_admin=user.is_super_admin
                                         )
            return {"message": f"Тип пользователя {user.email} изменен"} if check \
                else {"message": f"Ошибка изменения типа пользователя {user.email}"}

@router.delete('/delete/', summary='Удалить пользователя по айди')
async def dell_user_by_id(user_id: int, request_body: RBUser = Depends(get_current_admin_user)) -> dict:
    check = await UserDAO.del_by_id(user_id)
    return {"message": f"Пользователь с айди {user_id} успешно удален"} if check \
        else {"message": f"Ошибка удаления Пользователь с айди {user_id}"}
