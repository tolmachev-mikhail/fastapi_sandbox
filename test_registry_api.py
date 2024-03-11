from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_add_new_patient():
    response = client.post("/registry/patient")
    assert response.status_code == status.HTTP_201_CREATED


def test_search_for_the_patient():
    response = client.get("/registry/patient?name=test&surname=test&passport-id=test")
    assert response.status_code == status.HTTP_200_OK
