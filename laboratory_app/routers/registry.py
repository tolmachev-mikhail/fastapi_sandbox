from datetime import date
from typing import Annotated

from fastapi import APIRouter, Query, Security, status
from pydantic import BaseModel, EmailStr, validator

from laboratory_app.enums import AuthScopes, PatientGender

from .auth import User, get_current_user


class Client(BaseModel):
    first_name: str
    last_name: str
    gender: PatientGender
    date_of_birth: date
    email: EmailStr

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Mikhail",
                    "last_name": "Tolmachev",
                    "gender": PatientGender.MALE,
                    "date_of_birth": "1993-05-29",
                    "email": "mik_tol@gmail.com",
                }
            ]
        }
    }

    @validator("email")
    def parse_email(cls, v):
        if v.endswith("lab.com"):
            raise ValueError("Email must not end with 'lab.com'")
        return v


class RegisteredClientInDB(Client):
    hashed_password: str


router = APIRouter(prefix="/registry", tags=["Registry"])


@router.post("/patient", status_code=status.HTTP_201_CREATED)
def register_client(
    user: Annotated[User, Security(get_current_user, scopes=[AuthScopes.REGISTAR])],
    client: Client,
):
    pass


@router.get("/patient", status_code=status.HTTP_200_OK)
def find_patient(
    user: Annotated[User, Security(get_current_user, scopes=[AuthScopes.EMPLOYEE])],
    name: str,
    surname: str,
):
    return "Patient was found"
