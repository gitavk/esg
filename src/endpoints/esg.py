from typing import Any
from uuid import UUID

from fastapi import APIRouter

import src.crud.esg as crud_esg
from src.endpoints.deps import SessionDep
from src.schemas.esg import ESGCreate, ESGSchema

router = APIRouter()


@router.post("/", response_model=ESGSchema)
def create_esg(session: SessionDep, esg_in: ESGCreate) -> Any:
    esg = crud_esg.create(session, esg_in)
    return esg


@router.get("/{id}", response_model=ESGSchema)
def read_esg(session: SessionDep, id: UUID) -> Any:
    return crud_esg.get(session, id)
