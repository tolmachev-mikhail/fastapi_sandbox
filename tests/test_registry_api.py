from fastapi import status


def test_add_new_patient(client):
    response = client.post("/registry/patient")
    assert response.status_code == status.HTTP_201_CREATED


def test_search_for_the_patient(client):
    response = client.get("/registry/patient?name=test&surname=test&passport-id=test")
    assert response.status_code == status.HTTP_200_OK
