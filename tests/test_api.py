import pytest
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


def build_leads(signals: list[list[int]]):
    return {
        "leads": [
            {
                "name": "I" * idx,
                "signal": s,
            }
            for idx, s in enumerate(signals, 1)
        ]
    }


@pytest.mark.parametrize(
    "signals, expected",
    (
        ([[]], 0),
        ([[], []], 0),
        ([[0, 0, 0]], 0),
        ([[1, 1, 1]], 0),
        ([[1, 2, 3]], 0),
        ([[], [1, 1, 1]], 0),
        ([[-1, -1, -1]], 0),
        ([[-1, -3, -4]], 0),
        ([[], [-1, -1, -1]], 0),
        ([[-1, -1, -1], [1, 1, 1]], 0),
        ([[-1, 1], [1, -1]], 2),
        ([[-1, 1, -1], [1, -1, 1]], 4),
        ([[-1, 1, 0, 1]], 3),
        ([[1, 0, 1, 0]], 3),
        ([[-1, 0, 1, 0]], 3),
    ),
)
def test_crosses_zero(client, signals, expected):
    response = client.post("/", json=build_leads(signals))
    assert response.json()["crosses_zero"] == expected
