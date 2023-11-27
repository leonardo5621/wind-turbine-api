import datetime
from base import Base
from typing import List, Optional
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Measurement(Base):
  __tablename__ = "measurement"

  id: Mapped[int] = mapped_column(primary_key=True)
  
  timestamp: Mapped[datetime.datetime] = mapped_column(nullable=False)
  wind_speed: Mapped[float] = mapped_column(Float(), nullable=False)
  power: Mapped[float] = mapped_column(Float(), nullable=False)
  air_temperature: Mapped[float] = mapped_column(Float(), nullable=False)

  asset_id: Mapped[int] = mapped_column(ForeignKey("asset.id"), nullable=False)
  asset: Mapped["Asset"] = relationship(back_populates="measurements")
