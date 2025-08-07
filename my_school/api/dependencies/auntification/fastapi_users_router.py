from fastapi_users import FastAPIUsers

from core.model import User
from core.types.user_id import UserIdType
from .user_manager import get_usermanager
from .backend import authentication_backend

fastapi_users_router = FastAPIUsers[User, UserIdType](
    get_usermanager,
    [authentication_backend],
)
