from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.db.models import ESG, Lead
from src.schemas.esg import ESGCreate


def create(db: Session, esg: ESGCreate) -> ESG:
    db_obj = ESG()
    db.add(db_obj)
    db.commit()
    leads = []
    for ldata in esg.model_dump()["leads"]:
        ldata["signal"] = ",".join(map(str, ldata.pop("signal")))
        leads.append(Lead(esg_id=db_obj.id, **ldata))
    db.add_all(leads)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get(db: Session, esg_id: UUID) -> ESG:
    db_obj = db.get(ESG, esg_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="ESG not found")
    return db_obj
