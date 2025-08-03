from typing import Sequence
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from core.model import Student
from core.schemas.schema_student import StudentCreate, StudentUpdate


async def get_student(
    session: AsyncSession,
    id_student: int,
) -> Student:
    stmt = select(Student).where(Student.id == id_student)
    result = await session.scalars(stmt)
    student = result.first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid student by id"
        )
    return student


async def get_students(
    session: AsyncSession,
) -> Sequence[Student]:
    stmt = select(Student).order_by(Student.id)
    students = await session.scalars(stmt)
    return students.all()


async def create_student(
    session: AsyncSession,
    data_student: StudentCreate,
) -> Student:
    stmt = select(Student).where(
        and_(
            Student.name == data_student.name,
            Student.surname == data_student.surname,
            Student.year_of_birth == data_student.year_of_birth,
        )
    )
    student_school = await session.scalars(stmt)
    result = student_school.first()
    if not result:
        student = Student(**data_student.model_dump())
        session.add(student)
        await session.commit()
        await session.refresh(student)
        result = student
    return result
