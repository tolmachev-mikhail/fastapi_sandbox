from fastapi import status


def test_order_laboratory_analysis(client):
    response = client.post("/laboratory/analysis")
    assert response.status_code == status.HTTP_201_CREATED


def test_receive_laboratory_analysis_result(client):
    response = client.get("/laboratory/analysis/test_id")
    assert response.status_code == status.HTTP_200_OK


def test_update_laboratory_analysis_information(client):
    response = client.patch("/laboratory/analysis/test_id")
    assert response.status_code == status.HTTP_204_NO_CONTENT
