from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from .base import Base
from .students_school import students_object_table

if TYPE_CHECKING:
    from .student import Student


class SchoolSubject(Base):
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    school_assessment: Mapped[int] = mapped_column(nullable=False)
    id_student: Mapped[int] = mapped_column(ForeignKey("students.id"))

    students: Mapped["Student"] = relationship(
        secondary=students_object_table, back_populates="school_subjects"
    )
