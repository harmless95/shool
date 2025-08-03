from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base
from .students_subject import students_object_table

if TYPE_CHECKING:
    from .student import Student


class SchoolSubject(Base):
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=students_object_table,
        back_populates="school_subjects",
    )
