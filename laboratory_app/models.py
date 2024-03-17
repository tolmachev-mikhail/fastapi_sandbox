from sqlalchemy import (CheckConstraint, Column, Date, Enum, Float, ForeignKey,
                        Index, Integer, String)
from sqlalchemy.orm import relationship

from .database import Base, engine
from .enums import AnalysisType, JobTitle, PatientGender


class Registry(Base):
    __tablename__ = "registry"
    registry_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255))
    __table_args__ = (
        Index("idx_registry_name_last_name", "first_name", "last_name"),
        Index("idx_email", "email"),
        CheckConstraint(
            "email ~* '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'",
            name="check_user_email",
        ),
    )
    patients = relationship("Patient", uselist=False, back_populates="registry")


class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    registry_id = Column(Integer, ForeignKey("registry.registry_id"))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Enum(PatientGender), nullable=False)
    data_of_birth = Column(Date, nullable=False)
    __table_args__ = (Index("idx_patient_name_last_name", "first_name", "last_name"),)
    analyses = relationship("Analysis", back_populates="patient")
    registry = relationship("Registry", back_populates="patients")


class Analysis(Base):
    __tablename__ = "analysis"

    analysis_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    analysis_type = Column(Enum(AnalysisType), nullable=False)
    analysis_result = Column(Float, nullable=False)
    analysis_date = Column(Date, nullable=False)
    patient = relationship("Patient", back_populates="analyses")


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255))
    job_title = Column(Enum(JobTitle))
    __table_args__ = (
        Index("idx_employee_name_last_name", "first_name", "last_name"),
        Index("idx_employee_email", "email"),
        CheckConstraint(
            "email = first_name || '_' || last_name || '@lab.com'",
            name="check_employee_email",
        ),
    )


Base.metadata.create_all(bind=engine)
