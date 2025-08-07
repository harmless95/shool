from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date

from core.model.base import Base
from .mixins.id_pimary_key import IdIntPrimaryKeyMixin
from .students_subject import students_object_table

if TYPE_CHECKING:
    from .school_subjects import SchoolSubject
    from .day_school import DaySchool


class Student(Base, IdIntPrimaryKeyMixin):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(150), nullable=False)
    year_of_birth: Mapped[date] = mapped_column(Date, nullable=False)

    day_schools: Mapped["DaySchool"] = relationship(
        "DaySchool", back_populates="student"
    )

    school_subjects: Mapped[list["SchoolSubject"]] = relationship(
        "SchoolSubject",
        secondary=students_object_table,
        back_populates="students",
    )
