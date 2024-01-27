from typing import Any

from fastapi import APIRouter

from src.schemas.esg import ESGCreate

router = APIRouter()


@router.post("/")
def create_esg(esg_in: ESGCreate) -> Any:
    return esg_in


@router.get("/")
def read_esg() -> Any:
    return {}
