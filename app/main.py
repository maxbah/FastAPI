import asyncio
from fastapi import FastAPI
import uvicorn
from app.students.router import router as router_students
from app.majors.router import router as router_majors
from app.users.router import router as router_users
from app.pages.router import router as router_pages
from app.authx.router import (router as router_authx,
                              email_router as router_email,
                              files_router as router_file)
from app.items.router import router as router_item
from app.orders.router import router as router_order
from app.currency.router import router as router_currency
from fastapi.middleware.cors import CORSMiddleware
from app.events.startup import on_startup, on_loop_startup
from contextlib import asynccontextmanager


import os
import psutil

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before
    print("Before start app")
    await asyncio.create_task(on_startup())
    await asyncio.create_task(on_loop_startup())

    yield
    # After
    print("After all")

app = FastAPI(lifespan=lifespan)

app.add_middleware(CORSMiddleware, allow_origins=["*"])

# @app.on_event("startup")
# async def startup_event():
#     await asyncio.create_task(on_startup())
#     await asyncio.create_task(on_loop_startup())


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


app.include_router(router_currency)
app.include_router(router_order)
app.include_router(router_item)
app.include_router(router_file)
app.include_router(router_email)
app.include_router(router_authx)
app.include_router(router_students)
app.include_router(router_majors)
app.include_router(router_users)
app.include_router(router_pages)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)  # 0.0.0.0.0 for docker, else 127.0.0.1

