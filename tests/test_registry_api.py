import pytest
from fastapi import status


def test_adding_new_patient_by_registar(client, registar_auth_headers):
    response = client.post("/registry/patient", headers=registar_auth_headers)
    assert response.status_code == status.HTTP_201_CREATED


def test_negative_adding_new_patient_by_doctor(client, doctor_auth_headers):
    response = client.post("/registry/patient", headers=doctor_auth_headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_negative_adding_new_patient_by_laborant(client, laborant_auth_headers):
    response = client.post("/registry/patient", headers=laborant_auth_headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_search_for_patient_by_registar(client, registar_auth_headers):
    response = client.get(
        "/registry/patient?name=test&surname=test", headers=registar_auth_headers
    )
    assert response.status_code == status.HTTP_200_OK
