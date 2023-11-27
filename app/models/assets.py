from turtle import back
from base import Base
from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Asset(Base):
  __tablename__ = "asset"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)

  measurements: Mapped["Measurement"] = relationship(back_populates="asset")