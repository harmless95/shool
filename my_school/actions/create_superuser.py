import asyncio
import contextlib
from os import getenv

from api.dependencies.auntification.users import get_user_db
from api.dependencies.auntification.user_manager import get_usermanager
from core.auntefication.user_manager import UserManager
from core.schemas.users import UserCreate
from core.model import User, db_helper

get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_users_manager_context = contextlib.asynccontextmanager(get_usermanager)

default_email = getenv("DEFAULT_EMAIL", "admin@admin.com")
default_password = getenv("DEFAULT_PASSWORD", "abc")
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(user_create=user_create, safe=False)
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with db_helper.fabric_session() as session:
        async with get_user_db_context(session) as users_db:
            async with get_users_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
