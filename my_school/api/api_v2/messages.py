from typing import Annotated
from fastapi import APIRouter, Depends

from core.config import setting
from core.model import User
from api.api_v2.fastapi_users_router import (
    current_active_user,
    current_active_superuser,
)
from core.schemas.users import UserRead

router = APIRouter(prefix=setting.api.v2.messages, tags=["Messages"])


@router.get("")
def get_user_messages(
    user: Annotated[User, Depends(current_active_user)],
):
    return {
        "message": ["a1", "a2", "a3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[User, Depends(current_active_superuser)],
):
    return {
        "message": ["secrets-a1", "secrets-a2", "secrets-a3"],
        "user": UserRead.model_validate(user),
    }
