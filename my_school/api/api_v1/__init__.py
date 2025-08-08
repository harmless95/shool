from fastapi import APIRouter

from core.config import setting
from .day_school import router as router_school
from .student import router as router_student
from .subject import router as router_subject

# /router v1
router_v1 = APIRouter(prefix=setting.api.v1.prefix)

router_v1.include_router(router=router_school)
router_v1.include_router(router=router_student)
router_v1.include_router(router=router_subject)
