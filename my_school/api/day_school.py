from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import db_helper

router = APIRouter(prefix="/day", tags=["Day"])


@router.get("/")
async def get_all_day(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    pass
