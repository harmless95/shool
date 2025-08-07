from sqlalchemy import ForeignKey, Table, Column, Integer, UniqueConstraint

from .base import Base

students_object_table = Table(
    "students_object_table",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("school_subject_id", ForeignKey("school_subjects.id"), primary_key=True),
    UniqueConstraint("student_id", "school_subject_id", name="uniq_student_subject"),
)
