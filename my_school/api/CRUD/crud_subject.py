from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.model import SchoolSubject
from core.schemas.schema_school_subject import SchoolSubjectCreate, SchoolSubjectBase


async def get_all(session: AsyncSession) -> Sequence[SchoolSubject]:
    stmt = select(SchoolSubject).order_by(SchoolSubject.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_subject(
    session: AsyncSession, data: SchoolSubjectCreate
) -> SchoolSubject:
    stmt = select(SchoolSubject).where(SchoolSubject.name == data.name)
    subject_school = await session.scalars(stmt)
    result = subject_school.first()
    if not result:
        subject = SchoolSubject(**data.model_dump())
        session.add(subject)
        await session.commit()
        await session.refresh(subject)
        result = subject
    return result
