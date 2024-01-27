from fastapi.testclient import TestClient


def test_create_esg(client: TestClient) -> None:
    response = client.post("/", json={"leads": []})
    assert response.status_code == 200
    assert response.json() == {"leads": []}


def test_read_esg(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {}
