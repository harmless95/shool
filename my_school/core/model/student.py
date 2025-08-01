from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date

from core.model.base import Base


class Student(Base):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(150), nullable=False)
    year_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
