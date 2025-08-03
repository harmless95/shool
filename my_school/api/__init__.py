__all__ = (
    "router_student",
    "router_day",
    "router_subject",
)

from .student import router as router_student
from .day_school import router as router_day
from .subject import router as router_subject
