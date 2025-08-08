from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import setting
from .auth import router as router_auth
from .users import router as router_users
from .messages import router as router_messages

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=setting.api.v2.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(router=router_auth)
router.include_router(router=router_users)
router.include_router(router=router_messages)
