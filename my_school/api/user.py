from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import Student, db_helper
from .CRUD.crud_student import get_students as crud_students

router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/")
async def get_students(
    session: AsyncSession = Depends(db_helper.session_getter),
) -> list[Student]:
    return await crud_students(session=session)
