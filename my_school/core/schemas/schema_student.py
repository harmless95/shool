from datetime import date

from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    name: str
    surname: str
    year_of_birth: date


class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    name: str | None = None
    surname: str | None = None
    year_of_birth: date | None = None
