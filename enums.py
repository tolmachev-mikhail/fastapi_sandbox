from strenum import StrEnum


class PatientGender(StrEnum):
    MALE = "Male"
    FEMALE = "Female"


class AnalysisType(StrEnum):
    FBC = "Full Blood Count"
    URINALYSIS = "Urinalysis"
    BBA = "Blood Biochemistry Analysis"
