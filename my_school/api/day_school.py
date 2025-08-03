from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import db_helper
from .CRUD.crud_day import get_day_all, create_day
from core.schemas.schema_day import SchemaDayCreate, SchemaDayBase, SchemaDayRead

router = APIRouter(prefix="/day", tags=["Day"])


@router.get(
    "/",
    response_model=list[SchemaDayRead],
)
async def get_all_day(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    days = await get_day_all(session=session)
    return [SchemaDayRead.model_validate(day) for day in days]


@router.post(
    "/",
    response_model=SchemaDayRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_school_day(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data: SchemaDayCreate,
):
    return await create_day(session=session, data=data)
