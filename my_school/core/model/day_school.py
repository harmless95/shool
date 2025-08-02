from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey

from .base import Base

if TYPE_CHECKING:
    from .student import Student
    from .school_subjects import SchoolSubject


class DaySchool(Base):
    day: Mapped[date] = mapped_column(Date, nullable=False)
    school_assessment: Mapped[int] = mapped_column(nullable=False)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    student: Mapped["Student"] = relationship("Student")

    subject_id: Mapped[int] = mapped_column(ForeignKey("schoolsubjects.id"))
    subject: Mapped["SchoolSubject"] = relationship("SchoolSubject")
