import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.config import setting
from api import router_student
from core.model import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app_main = FastAPI(lifespan=lifespan)
app_main.include_router(router=router_student)


@app_main.get("/")
async def get_hello():
    return {
        "message": "Hello World",
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app_main",
        host=setting.run.host,
        port=setting.run.port,
    )
