__all__ = (
    "router_student",
    "router_day",
    "router_subject",
)

from api.api_v1.student import router as router_student
from api.api_v1.day_school import router as router_day
from api.api_v1.subject import router as router_subject
