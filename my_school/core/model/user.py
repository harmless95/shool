from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from .base import Base
from .mixins.id_pimary_key import IdIntPrimaryKeyMixin
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPrimaryKeyMixin, SQLAlchemyBaseUserTable[UserIdType]):
    pass

    @classmethod
    async def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
