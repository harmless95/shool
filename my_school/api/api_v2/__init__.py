from fastapi import APIRouter

from core.config import setting
from .auth import router as router_auth
from .users import router as router_users

router = APIRouter(prefix=setting.api.v2.prefix)
router.include_router(router=router_auth)
router.include_router(router=router_users)
