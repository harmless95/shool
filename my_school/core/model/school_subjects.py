from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base
from .mixins.id_pimary_key import IdIntPrimaryKeyMixin
from .students_subject import students_object_table

if TYPE_CHECKING:
    from .day_school import DaySchool
    from .student import Student


class SchoolSubject(Base, IdIntPrimaryKeyMixin):
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    day_schools: Mapped["DaySchool"] = relationship(
        "DaySchool", back_populates="subject"
    )

    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=students_object_table,
        back_populates="school_subjects",
    )
