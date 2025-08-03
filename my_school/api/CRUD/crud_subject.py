from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from core.model import SchoolSubject
from core.schemas.schema_school_subject import (
    SchoolSubjectCreate,
    SchoolSubjectBase,
    SchoolSubjectUpdate,
)


async def get_subject(
    session: AsyncSession,
    id_subject: int,
) -> SchoolSubject:
    stmt = select(SchoolSubject).where(SchoolSubject.id == id_subject)
    result = await session.scalars(stmt)
    subject = result.first()
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid subject by id",
        )
    return subject


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
