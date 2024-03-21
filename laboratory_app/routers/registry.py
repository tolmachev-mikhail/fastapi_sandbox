from typing import Annotated

from fastapi import APIRouter, Query, Security, status

from laboratory_app.enums import AuthScopes

from .auth import User, get_current_user

router = APIRouter(prefix="/registry", tags=["Registry"])


@router.post("/patient", status_code=status.HTTP_201_CREATED)
def add_new_patient(
    user: Annotated[User, Security(get_current_user, scopes=[AuthScopes.REGISTAR])]
):
    return "Patient was added"


@router.get("/patient", status_code=status.HTTP_200_OK)
def find_patient(
    user: Annotated[User, Security(get_current_user, scopes=[AuthScopes.EMPLOYEE])],
    name: str,
    surname: str,
):
    return "Patient was found"
