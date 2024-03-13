from sqlalchemy import (Column, Date, Enum, Float, ForeignKey, Index, Integer,
                        String)
from sqlalchemy.orm import relationship

from database import Base
from enums import AnalysisType, PatientGender


class Registry(Base):
    __tablename__ = "registry"
    registry_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255))
    __table_args__ = (Index("idx_registry_name_last_name", "first_name", "last_name"),)
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
    __tablename__ = "analyses"

    analysis_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    analysis_type = Column(Enum(AnalysisType), nullable=False)
    analysis_result = Column(Float, nullable=False)
    analysis_date = Column(Date, nullable=False)
    patient = relationship("Patient", back_populates="analyses")
