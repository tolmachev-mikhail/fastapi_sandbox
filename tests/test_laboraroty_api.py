import pytest
from fastapi import status


def test_positive_order_laboratory_analysis(client, registar_auth_headers):
    # given
    response = client.post("/laboratory/analysis", headers=registar_auth_headers)
    # then
    assert response.status_code == status.HTTP_201_CREATED


def test_negative_order_laboratory_analysis(
    client, doctor_auth_headers, laborant_auth_headers
):
    # when
    doctor_response = client.post("/laboratory/analysis", headers=doctor_auth_headers)
    laborant_response = client.post(
        "/laboratory/analysis", headers=laborant_auth_headers
    )
    # then
    assert doctor_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert laborant_response.status_code == status.HTTP_401_UNAUTHORIZED


def test_receive_laboratory_analysis_result(
    client, doctor_auth_headers, laborant_auth_headers, registar_auth_headers
):
    # when
    doctor_response = client.get(
        "/laboratory/analysis/test_id", headers=doctor_auth_headers
    )
    laborant_response = client.get(
        "/laboratory/analysis/test_id", headers=laborant_auth_headers
    )
    registar_response = client.get(
        "/laboratory/analysis/test_id", headers=registar_auth_headers
    )
    # then
    assert doctor_response.status_code == status.HTTP_200_OK
    assert laborant_response.status_code == status.HTTP_200_OK
    assert registar_response.status_code == status.HTTP_200_OK


def test_positive_update_laboratory_analysis_information(client, doctor_auth_headers):
    # when
    response = client.patch("/laboratory/analysis/test_id", headers=doctor_auth_headers)
    # then
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_negative_update_laboratory_analysis_information(
    client, laborant_auth_headers, registar_auth_headers
):
    # when
    laborant_response = client.patch(
        "/laboratory/analysis/test_id", headers=laborant_auth_headers
    )
    registar_response = client.patch(
        "/laboratory/analysis/test_id", headers=registar_auth_headers
    )
    # then
    assert laborant_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert registar_response.status_code == status.HTTP_401_UNAUTHORIZED
