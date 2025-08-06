from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache
from fastapi_cache import FastAPICache

from core.model import db_helper, SchoolSubject
from .CRUD.crud_subject import create_subject, get_all, get_subject, update_subject
from core.schemas.schema_school_subject import (
    SchoolSubjectCreate,
    SchoolSubjectRead,
    SchoolSubjectUpdate,
)


router = APIRouter(prefix="/subject", tags=["Subject"])


@router.get(
    "/{id_subject}/",
    response_model=SchoolSubjectRead,
    status_code=status.HTTP_200_OK,
)
@cache(expire=60)
async def get_subject_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    id_subject: int,
) -> SchoolSubject:
    return await get_subject(
        session=session,
        id_subject=id_subject,
    )


@router.get(
    "/",
    response_model=list[SchoolSubjectRead],
    status_code=status.HTTP_200_OK,
)
@cache(expire=60)
async def get_all_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await get_all(session=session)


@router.post(
    "/",
    response_model=SchoolSubjectRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data: SchoolSubjectCreate,
):
    result = await create_subject(session=session, data=data)
    await FastAPICache.clear()
    return result


@router.put(
    "/{id_subject}/",
    status_code=status.HTTP_200_OK,
)
async def update_subject_total(
    data_update: SchoolSubjectUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_subject: SchoolSubject = Depends(get_subject_by_id),
):
    result = await update_subject(
        session=session, data_subject=data_subject, data_update=data_update
    )
    await FastAPICache.clear()
    return result


@router.patch(
    "/{id_subject}/",
    status_code=status.HTTP_200_OK,
)
async def update_subject_partial(
    data_update: SchoolSubjectUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_subject: SchoolSubject = Depends(get_subject_by_id),
):
    result = await update_subject(
        session=session,
        data_subject=data_subject,
        data_update=data_update,
        partial=True,
    )
    await FastAPICache.clear()
    return result


@router.delete("/{id_subject}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    subject: SchoolSubject = Depends(get_subject_by_id),
) -> None:
    await session.delete(subject)
    await FastAPICache.clear()
