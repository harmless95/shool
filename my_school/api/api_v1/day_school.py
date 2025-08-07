from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache
from fastapi_cache import FastAPICache

from core.model import db_helper
from api.CRUD.crud_day import get_day_all, create_day, get_day_by_id, update_day
from core.schemas.schema_day import (
    SchemaDayCreate,
    SchemaDayBase,
    SchemaDayRead,
    SchemaDayUpdate,
)
from core.model import DaySchool

router = APIRouter(prefix="/day", tags=["Day"])


@router.get(
    "/",
    response_model=list[SchemaDayRead],
    status_code=status.HTTP_200_OK,
)
@cache(expire=60)
async def get_all_day(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> list[SchemaDayRead]:
    days = await get_day_all(session=session)
    return [SchemaDayRead.model_validate(day) for day in days]


@router.get(
    "/{id_day}/",
    response_model=SchemaDayRead,
    status_code=status.HTTP_200_OK,
)
@cache(expire=60)
async def get_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    id_day: int,
) -> SchemaDayRead:
    return await get_day_by_id(session=session, id_day=id_day)


@router.post(
    "/",
    response_model=SchemaDayRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_school_day(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data: SchemaDayCreate,
) -> SchemaDayRead:
    result = await create_day(session=session, data=data)
    await FastAPICache.clear()
    return result


@router.put(
    "/{id_day}/",
    status_code=status.HTTP_200_OK,
)
async def update_day_total(
    data_update: SchemaDayUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_day: DaySchool = Depends(get_by_id),
):
    result = await update_day(
        data_update=data_update,
        session=session,
        data_day=data_day,
    )
    await FastAPICache.clear()
    return result


@router.patch(
    "/{id_day}/",
    status_code=status.HTTP_200_OK,
)
async def update_day_total(
    data_update: SchemaDayUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_day: DaySchool = Depends(get_by_id),
):
    result = await update_day(
        data_update=data_update,
        session=session,
        data_day=data_day,
        partial=True,
    )
    await FastAPICache.clear()
    return result


@router.delete(
    "/{id_day}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_day(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_day: DaySchool = Depends(get_by_id),
) -> None:
    await session.delete(data_day)
    await FastAPICache.clear()
