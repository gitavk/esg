from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.db.models import ESG


def test_create_esg(client: TestClient) -> None:
    response = client.post("/", json={"leads": []})
    assert response.status_code == 200
    assert response.json()["crosses_zero"] == 0


def test_read_esg(client: TestClient, session: Session) -> None:
    esg = ESG()
    session.add(esg)
    session.commit()
    session.refresh(esg)
    response = client.get(f"/{esg.id}")
    assert response.status_code == 200
    assert response.json()["crosses_zero"] == 0
