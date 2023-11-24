from fastapi import APIRouter
from enum import Enum

router = APIRouter(
  prefix="/measurements"
)

class Metrics(Enum):
  WIND_SPEED="wind_speed"
  POWER="power"
  AIR_TEMPERATURE ="air_temperature"


@router.get("/{asset_id}")
async def get_asset_measurements(asset_id: str):
  return []

@router.get("/median/{metric}")
async def get_asset_measurement_median(metric: Metrics):
  return []