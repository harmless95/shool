from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from core.model import DaySchool, Student, SchoolSubject
from core.schemas.schema_day import SchemaDayCreate


async def get_day_all(session: AsyncSession):
    stmt = select(DaySchool).order_by(DaySchool.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_day(session: AsyncSession, data: SchemaDayCreate) -> SchemaDayCreate:
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
        student_id=result_student,
        subject_id=result_subject,
    )
    session.add(day)
    await session.commit()
    await session.refresh(day)
    return SchemaDayCreate(
        day=day.day,
        school_assessment=day.school_assessment,
        student=data.student,
        subject=data.subject,
    )
