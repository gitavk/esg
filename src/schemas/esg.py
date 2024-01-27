from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LeadCreate(BaseModel):
    name: str
    signal: list[int]


class ESGCreate(BaseModel):
    leads: list[LeadCreate]


class ESGSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    crosses_zero: int
