from fastapi import APIRouter

from core.config import setting
from core.schemas.users import UserRead, UserUpdate

from .fastapi_users_router import fastapi_users_router

router = APIRouter(prefix=setting.api.v2.users, tags=["Users"])
# /me
# /{id}
router.include_router(
    router=fastapi_users_router.get_users_router(
        UserRead,
        UserUpdate,
    )
)
