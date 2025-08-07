from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from core.model import db_helper, Student
from api.CRUD.crud_student import (
    get_students as crud_students,
    create_student as crud_student_create,
    get_student,
    update_student,
)
from core.schemas.schema_student import (
    StudentBase,
    StudentCreate,
    StudentRead,
    StudentRead2,
    StudentUpdate,
)

router = APIRouter(prefix="/student", tags=["Student"])


@router.get(
    "/{id_student}/",
    response_model=StudentRead2,
    status_code=status.HTTP_200_OK,
)
@cache(expire=60)
async def get_student_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    id_student: int,
) -> Student:
    return await get_student(
        session=session,
        id_student=id_student,
    )


@router.get(
    "/",
    response_model=list[StudentRead2],
    status_code=status.HTTP_200_OK,
)
@cache(expire=60)
async def get_students(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    students = await crud_students(session=session)
    return students


@router.post(
    "/",
    response_model=StudentRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_student: StudentCreate,
) -> Student:
    student = await crud_student_create(session=session, data_student=data_student)
    await FastAPICache.clear()
    return student


@router.put(
    "/{id_student}/",
    status_code=status.HTTP_200_OK,
)
async def update_student_total(
    data_update: StudentUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_student: Student = Depends(get_student_by_id),
):
    result = await update_student(
        data_update=data_update,
        session=session,
        data_student=data_student,
    )
    await FastAPICache.clear()

    return result


@router.patch(
    "/{id_student}/",
    status_code=status.HTTP_200_OK,
)
async def update_student_partial(
    data_update: StudentUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_student: Student = Depends(get_student_by_id),
):
    result = await update_student(
        data_update=data_update,
        session=session,
        data_student=data_student,
        partial=True,
    )
    await FastAPICache.clear()
    return result


@router.delete(
    "/{id_student}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student_by_id(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_student: Student = Depends(get_student_by_id),
) -> None:
    await session.delete(data_student)
    await FastAPICache.clear()
