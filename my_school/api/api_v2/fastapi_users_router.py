from fastapi_users import FastAPIUsers

from core.model import User
from core.types.user_id import UserIdType
from api.dependencies.auntification.user_manager import get_usermanager
from api.dependencies.auntification.backend import authentication_backend

fastapi_users_router = FastAPIUsers[User, UserIdType](
    get_usermanager,
    [authentication_backend],
)

current_active_user = fastapi_users_router.current_user(active=True)
current_active_superuser = fastapi_users_router.current_user(
    active=True, superuser=True
)
