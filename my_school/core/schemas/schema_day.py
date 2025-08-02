from typing import TYPE_CHECKING
from datetime import date
from pydantic import BaseModel

if TYPE_CHECKING:
    from .schema_student import StudentBase
    from .schema_school_subject import SchoolSubjectBase


class SchemaDayBase(BaseModel):
    day: date
    school_assessment: int


class SchemaDayRead(SchemaDayBase):
    id: int


class SchemaDayCreate(SchemaDayBase):
    student: StudentBase | None = None
    subject: SchoolSubjectBase | None = None


class SchemaDayUpdate(SchemaDayBase):
    day: date | None = None
    school_assessment: int | None = None
