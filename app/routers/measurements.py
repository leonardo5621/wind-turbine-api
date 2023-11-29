from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Annotated
from services import measurements
from api_schemas.schemas import MeanIn, MetricMean

router = APIRouter(
  prefix="/measurements"
)

@router.get("/")
async def get_asset_measurements() -> list[measurements.Metrics]:
  return [metric.value for metric in measurements.Metrics]

@router.post("/mean")
def get_asset_measurement_mean(meanCalculation: MeanIn) -> list[MetricMean]:
  mean_results = measurements.get_assets_metric_average(
    meanCalculation.asset_ids,
    meanCalculation.startTime,
    meanCalculation.endTime,
    meanCalculation.metric,
  )
  return mean_results