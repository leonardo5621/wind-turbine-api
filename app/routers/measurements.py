from fastapi import APIRouter, Query
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

router = APIRouter(
  prefix="/measurements"
)

class Metrics(Enum):
  WIND_SPEED="wind_speed"
  POWER="power"
  AIR_TEMPERATURE ="air_temperature"

class MedianIn(BaseModel):
  metric: Metrics
  startTime: float
  endTime: float
  asset_ids: list[int]

class MetricMedian(BaseModel):
  asset_id: int
  median: float

@router.get("/")
async def get_asset_measurements() -> list[Metrics]:
  return []

@router.post("/median")
async def get_asset_measurement_median(medianCalculation: MedianIn) -> list[MetricMedian]:
  return []