from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import db_helper
from .CRUD.crud_day import get_day_all, create_day
from core.schemas.schema_day import SchemaDayCreate, SchemaDayBase

router = APIRouter(prefix="/day", tags=["Day"])


@router.get(
    "/",
    response_model=list[SchemaDayBase],
)
async def get_all_day(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await get_day_all(session=session)


@router.post(
    "/",
    response_model=SchemaDayBase,
    status_code=status.HTTP_201_CREATED,
)
async def create_school_day(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data: SchemaDayCreate,
):
    return await create_day(
        session=session,
        data=data,
    )
