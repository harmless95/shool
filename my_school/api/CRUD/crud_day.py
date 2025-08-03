from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import select
from fastapi import HTTPException, status

from core.model import DaySchool, Student, SchoolSubject
from core.schemas.schema_day import SchemaDayCreate, SchemaDayRead


async def get_day_all(session: AsyncSession) -> Sequence[DaySchool]:
    stmt = (
        select(DaySchool)
        .options(
            selectinload(DaySchool.student),
            selectinload(DaySchool.subject),
        )
        .order_by(DaySchool.id)
    )
    result = await session.scalars(stmt)
    return result.all()


async def create_day(session: AsyncSession, data: SchemaDayCreate) -> SchemaDayRead:
    stmt_student = select(Student).where(
        Student.name == data.student.name,
        Student.surname == data.student.surname,
        Student.year_of_birth == data.student.year_of_birth,
    )
    result_student = await session.scalar(stmt_student)
    if not result_student:
        student = Student(
            name=data.student.name,
            surname=data.student.surname,
            year_of_birth=data.student.year_of_birth,
        )
        session.add(student)
        await session.flush()
        result_student = student

    stmt_subject = select(SchoolSubject).where(SchoolSubject.name == data.subject.name)
    result_subject = await session.scalar(stmt_subject)
    if not result_subject:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid subject"
        )

    day = DaySchool(
        day=data.day,
        school_assessment=data.school_assessment,
        student_id=result_student.id,
        subject_id=result_subject.id,
    )
    session.add(day)
    await session.commit()
    stmt_day = (
        select(DaySchool)
        .options(
            selectinload(DaySchool.subject),
            selectinload(DaySchool.student),
        )
        .where(DaySchool.id == day.id)
    )
    result_day = await session.scalars(stmt_day)
    day = result_day.first()
    return SchemaDayRead.model_validate(day)
