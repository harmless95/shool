from typing import Annotated, TYPE_CHECKING
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from core.model import db_helper, User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)],
):
    yield User.get_db(session=session)
