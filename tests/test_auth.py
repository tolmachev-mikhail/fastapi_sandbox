import os

import pytest
from fastapi import status


@pytest.mark.parametrize(
    "data",
    [
        {
            "grant_type": "",
            "username": "fake_employee@lab.com",
            "password": "fake_password",
            "scope": "",
            "client_id": "",
            "client_secret": "",
        },
        {
            "grant_type": "",
            "username": "fake_patient@gmail.com",
            "password": "fake_password",
            "scope": "",
            "client_id": "",
            "client_secret": "",
        },
    ],
)
def test_negative_auth(client, data: dict):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = client.post("/auth/token", headers=headers, data=data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize(
    "data",
    [
        {
            "grant_type": "",
            "username": os.getenv("SYS_TST_USER"),
            "password": os.getenv("SYS_TST_PASSWORD"),
            "scope": "",
            "client_id": "",
            "client_secret": "",
        },
    ],
)
def test_positive_auth(client, data: dict):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = client.post("/auth/token", headers=headers, data=data)
    assert response.status_code == status.HTTP_200_OK
