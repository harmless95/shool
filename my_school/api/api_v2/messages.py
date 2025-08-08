from fastapi import APIRouter

from core.config import setting

router = APIRouter(prefix=setting.api.v2.messages, tags=["Messages"])
