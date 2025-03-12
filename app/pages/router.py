from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.students.router import get_all_students
from app.users.router import get_me

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/profile')
async def get_my_profile(request: Request, profile=Depends(get_me)):
    return templates.TemplateResponse(name='profile.html', context={'request': request, 'profile': profile})


@router.get('/students')
async def get_students_html(request: Request, student=Depends(get_all_students)):
    return templates.TemplateResponse(name='students.html',
                                      context={'request': request, 'students': student})

@router.get('/register')
async def register_user(request: Request):
    return templates.TemplateResponse(name='register_form.html',
                                      context={'request': request})

@router.get('/login', summary='Войти с учетной записью')
async def login(request: Request):
    return templates.TemplateResponse(name='login_form.html', context={'request': request})
