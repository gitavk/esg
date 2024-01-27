from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def create_esg() -> Any:
    return {}


@router.get("/")
def read_esg() -> Any:
    return {}
