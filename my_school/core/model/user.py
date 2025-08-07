from typing import TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


from .base import Base
from .mixins.id_pimary_key import IdIntPrimaryKeyMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPrimaryKeyMixin, SQLAlchemyBaseUserTable[int]):
    pass

    @classmethod
    async def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
