from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_order_laboratory_analysis():
    response = client.post("/laboratory/analysis")
    assert response.status_code == status.HTTP_201_CREATED


def test_receive_laboratory_analysis_result():
    response = client.get("/laboratory/analysis/test_id")
    assert response.status_code == status.HTTP_200_OK


def test_update_laboratory_analysis_information():
    response = client.patch("/laboratory/analysis/test_id")
    assert response.status_code == status.HTTP_204_NO_CONTENT
