from fastapi import FastAPI
from app.students.router import router as router_students
from app.majors.router import router as router_majors
from app.users.router import router as router_user
import os
import psutil


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет всем!"}


@app.get("/quit")
def iquit():
    parent_pid = os.getpid()
    parent = psutil.Process(parent_pid)
    for child in parent.children(recursive=True):  # or parent.children() for recursive=False
        child.kill()
    parent.kill()

app.include_router(router_students)
app.include_router(router_majors)
app.include_router(router_user)
