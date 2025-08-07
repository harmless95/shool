from fastapi_users.db import SQLAlchemyBaseUserTable

from .base import Base
from .mixins.id_pimary_key import IdIntPrimaryKeyMixin


class User(Base, IdIntPrimaryKeyMixin, SQLAlchemyBaseUserTable[int]):
    pass
