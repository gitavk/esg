from sqlalchemy.orm import Session

from src.db.models import ESG, Lead


def test_esg(session):
    esg = ESG()
    session.add(esg)
    session.commit()
    assert esg.id is not None
    assert esg.crosses_zero == 0
    assert not esg.leads


def test_leads(session: Session):
    esg = ESG()
    session.add(esg)
    session.commit()
    lead2 = Lead(
        esg=esg,
        name="II",
        signal="2, -2",
    )
    lead3 = Lead(
        esg=esg,
        name="III",
        signal="1, -1",
    )
    session.add_all([lead2, lead3])
    session.commit()
    assert esg.id is not None
    assert len(esg.leads) == 2
