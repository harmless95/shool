from fastapi import APIRouter

from api.dependencies.auntification.backend import authentication_backend
from core.config import setting

from .fastapi_users_router import fastapi_users_router

router = APIRouter(
    prefix=setting.api.v2.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users_router.get_auth_router(authentication_backend)
)
