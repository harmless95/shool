from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import Student


async def get_students(
    session: AsyncSession,
) -> list[Student]:
    stmt = select(Student).order_by(Student.id)
    students = await session.scalars(stmt)
    return students
