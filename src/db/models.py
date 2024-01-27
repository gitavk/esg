import datetime as dt
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from .engine import Base


class ESG(Base):
    __tablename__ = "esgs"
    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.utcnow)
    leads: Mapped[list["Lead"]] = relationship(
        "Lead",
        back_populates="esg",
        cascade="all, delete-orphan",
    )
    crosses_zero: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self) -> str:
        return f"ESG({self.id}, {self.crosses_zero})"


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    esg_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("esgs.id", ondelete="CASCADE"),
        index=True,
    )
    esg: Mapped[ESG] = relationship("ESG", back_populates="leads")
    name: Mapped[str]
    signal: Mapped[str] = mapped_column(Text)
    crosses_zero: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self) -> str:
        return f"Lead({self.name}, {self.crosses_zero})"
