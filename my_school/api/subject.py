from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import db_helper
from .CRUD.crud_subject import create_subject, get_all
from core.schemas.schema_school_subject import SchoolSubjectCreate, SchoolSubjectRead

router = APIRouter(prefix="/subject", tags=["Subject"])


@router.get("/", response_model=list[SchoolSubjectRead])
async def get_all_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await get_all(session=session)


@router.post(
    "/",
    response_model=SchoolSubjectRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_subject(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    data: SchoolSubjectCreate,
):
    return await create_subject(session=session, data=data)
