import structlog
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.resposes import PlainTextResponse
from sqlalchemy.orm import Session
from services import measurements, assets, sessionmaker
from api_schemas.schemas import MeanIn, MetricMean


router = APIRouter(
  prefix="/measurements"
)

logger = structlog.get_logger()

SessionDependency = Annotated[Session, Depends(sessionmaker.get_session_dependency)]

@router.get("/", tags=["measurements"])
async def get_asset_measurements() -> list[measurements.Metrics]:
  return [metric.value for metric in measurements.Metrics]

@router.post("/mean", tags=["measurements"])
def get_asset_measurement_mean(session: SessionDependency, meanCalculation: MeanIn) -> list[MetricMean]:
  log = logger.new(metric=meanCalculation.metric, startTime=meanCalculation.startTime, endTime=meanCalculation.endTime)
  if len(meanCalculation.asset_ids) == 0:
    log.error("Received empty asset ids list")
    raise HTTPException(status_code=404, detail="Please provide at least one asset id")

  ids = list(set(meanCalculation.asset_ids))
  if not assets.check_valid_asset_ids(session, ids):
    log.error("At least one of the asset ids have not been found in the database")
    raise HTTPException(status_code=404, detail="Invalid asset ids list")
  try:
    mean_results = measurements.get_assets_metric_average(
      session,
      meanCalculation.asset_ids,
      meanCalculation.startTime,
      meanCalculation.endTime,
      meanCalculation.metric,
    )
    return mean_results
  except Exception as err:
    log.error("Failed to query database", err)
    return PlainTextResponse("Internal Server Error", status_code=500)
