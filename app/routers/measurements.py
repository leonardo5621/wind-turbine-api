from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Annotated
from services import measurements

router = APIRouter(
  prefix="/measurements"
)


class MedianIn(BaseModel):
  metric: measurements.Metrics
  startTime: float
  endTime: float
  asset_ids: list[int]

class MetricMedian(BaseModel):
  asset_id: int
  median: float

@router.get("/")
async def get_asset_measurements() -> list[measurements.Metrics]:
  return [metric.value for metric in measurements.Metrics]

@router.post("/median")
def get_asset_measurement_median(medianCalculation: MedianIn) -> list[MetricMedian]:
  median = measurements.get_filtered_measurements(
    medianCalculation.asset_ids[0],
    medianCalculation.startTime,
    medianCalculation.endTime,
    medianCalculation.metric,
  )
  return []