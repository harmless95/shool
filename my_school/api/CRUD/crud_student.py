from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import Student
from core.schemas.schema_student import StudentCreate


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
    student = Student(**data_student.model_dump())
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return student
