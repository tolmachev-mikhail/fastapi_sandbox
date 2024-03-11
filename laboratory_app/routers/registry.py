from typing import Annotated

from fastapi import APIRouter, Query, status

router = APIRouter(prefix="/registry", tags=["Registry"])


@router.post("/patient", status_code=status.HTTP_201_CREATED)
def add_new_patient():
    pass


@router.get("/patient", status_code=status.HTTP_200_OK)
def find_patient(
    name: str, surname: str, passport_id: Annotated[str, Query(alias="passport-id")]
):
    return "Patient was found"
