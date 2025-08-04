import uvicorn
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.config import setting
from api import router_student, router_day, router_subject
from core.model import db_helper

logging.basicConfig(
    level=logging.INFO,
    format=setting.logging.log_format,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app_main = FastAPI(lifespan=lifespan)
app_main.include_router(router=router_student)
app_main.include_router(router=router_day)
app_main.include_router(router=router_subject)


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
