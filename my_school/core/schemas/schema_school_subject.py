from pydantic import BaseModel, ConfigDict


class SchoolSubjectBase(BaseModel):
    name: str


class SchoolSubjectRead(SchoolSubjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SchoolSubjectCreate(SchoolSubjectBase):
    pass


class SchoolSubjectUpdate(SchoolSubjectBase):
    name: str | None = None
