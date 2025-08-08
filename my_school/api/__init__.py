from fastapi import APIRouter

from .api_v1 import router_v1
from .api_v2 import router_v2

# / all routers
router_all_api = APIRouter()

router_all_api.include_router(router=router_v1)
router_all_api.include_router(router=router_v2)
