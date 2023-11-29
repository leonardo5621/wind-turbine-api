from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services import measurements, assets, sessionmaker
from api_schemas.schemas import MeanIn, MetricMean

router = APIRouter(
  prefix="/measurements"
)

SessionDependency = Annotated[Session, Depends(sessionmaker.get_session_dependency)]

@router.get("/", tags=["measurements"])
async def get_asset_measurements() -> list[measurements.Metrics]:
  return [metric.value for metric in measurements.Metrics]

@router.post("/mean", tags=["measurements"])
def get_asset_measurement_mean(session: SessionDependency, meanCalculation: MeanIn) -> list[MetricMean]:
  if len(meanCalculation.asset_ids) == 0:
    raise HTTPException(status_code=404, detail="Please provide at least one asset id")

  ids = list(set(meanCalculation.asset_ids))
  if not assets.check_valid_asset_ids(session, ids):
    raise HTTPException(status_code=404, detail="Invalid asset ids list")

  mean_results = measurements.get_assets_metric_average(
    session,
    meanCalculation.asset_ids,
    meanCalculation.startTime,
    meanCalculation.endTime,
    meanCalculation.metric,
  )
  return mean_results