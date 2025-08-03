from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict

from .schema_student import StudentRead, StudentBase
from .schema_school_subject import SchoolSubjectRead, SchoolSubjectBase


class SchemaDayBase(BaseModel):
    day: date
    school_assessment: int
    model_config = ConfigDict(from_attributes=True)


class SchemaDayRead(SchemaDayBase):
    id: int
    student: Optional[StudentRead]
    subject: Optional[SchoolSubjectRead]
    model_config = ConfigDict(from_attributes=True)


class SchemaDayCreate(SchemaDayBase):
    student: Optional[StudentBase]
    subject: Optional[SchoolSubjectBase]
    model_config = ConfigDict(from_attributes=True)


class SchemaDayUpdate(SchemaDayBase):
    day: date | None = None
    school_assessment: int | None = None
    student: Optional[StudentBase] | None = None
    subject: Optional[SchoolSubjectBase] | None = None
