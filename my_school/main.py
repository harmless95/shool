import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.config import setting
from api import router_user


@asynccontextmanager
def lifespan(app: FastAPI):
    yield


app_main = FastAPI()
app_main.include_router(router=router_user)


@app_main.get("/")
async def get_hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app_main",
        host=setting.run.host,
        port=setting.run.port,
    )
