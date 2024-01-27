from uuid import UUID

from pydantic import BaseModel


class LeadCreate(BaseModel):
    name: str
    signal: list[int]


class ESGCreate(BaseModel):
    leads: list[LeadCreate]


class ESGSchema(BaseModel):
    id: UUID
    crosses_zero: int
