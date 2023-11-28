import datetime
from typing import List, Optional
from sqlalchemy import String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Asset(Base):
  __tablename__ = "asset"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)

  measurements: Mapped[List["Measurement"]] = relationship(back_populates="asset")

class Measurement(Base):
  __tablename__ = "measurement"

  id: Mapped[int] = mapped_column(primary_key=True)
  
  timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(),nullable=False)
  wind_speed: Mapped[float] = mapped_column(Float(), nullable=False)
  power: Mapped[float] = mapped_column(Float(), nullable=False)
  air_temperature: Mapped[float] = mapped_column(Float(), nullable=False)

  asset_id: Mapped[int] = mapped_column(ForeignKey("asset.id"), nullable=False)
  asset: Mapped["Asset"] = relationship("Asset", back_populates="measurements")
