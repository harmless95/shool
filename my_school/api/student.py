from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import db_helper, Student
from .CRUD.crud_student import (
    get_students as crud_students,
    create_student as crud_student_create,
)
from core.schemas.schema_student import StudentBase, StudentCreate, StudentRead

router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/", response_model=list[StudentBase])
async def get_students(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    students = await crud_students(session=session)
    return students


@router.post("/", response_model=StudentRead)
async def create_student(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data_student: StudentCreate,
) -> Student:
    student = await crud_student_create(session=session, data_student=data_student)
    return student
