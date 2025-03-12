from authx.exceptions import MissingTokenError
from fastapi import APIRouter, Depends, HTTPException, Response

from app.users.authx import auth, config
from app.users.schemas import UserAuth

router = APIRouter(prefix='/authx', tags=['AuthX  авторизация'])

@router.post('/loginx', summary='Авторизация через AuthX')
def login(user_cred: UserAuth, response: Response):
     if user_cred.email == "xyz@example.com" and user_cred.password == "123456":
          token = auth.create_access_token(uid=user_cred.email)
          response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
          return {"access_token": token}
     raise HTTPException(401, detail={"message": "Invalid credentials"})

@router.get("/protectedx", summary="Доступ к скрытым данным",
            dependencies=[Depends(auth.access_token_required)])
def get_protected():
     try:
          return {"message": "Secured data"}
     except MissingTokenError as e:
          raise HTTPException(401, detail={"message": str(e)}) from e
