from datetime import datetime
from .sessionmaker import session_maker
from models.schemas import Measurement
from sqlalchemy.sql.expression import func
from enum import Enum


class Metrics(Enum):
  WIND_SPEED="wind_speed"
  POWER="power"
  AIR_TEMPERATURE ="air_temperature"

def get_metric_column(metric: Metrics):
  if metric == Metrics.WIND_SPEED:
    return Measurement.wind_speed.label(Metrics.WIND_SPEED.value)
  if metric == Metrics.POWER:
    return Measurement.power.label(Metrics.POWER.value)
  if metric == Metrics.AIR_TEMPERATURE:
    return Measurement.air_temperature.label(Metrics.AIR_TEMPERATURE.value)
  return None

def get_filtered_measurements(asset_id: int, startTime: float, endTime: float, metric: Metrics):

  start = datetime.fromtimestamp(startTime)
  end = datetime.fromtimestamp(endTime)
  with session_maker() as session:
    median = session.query(
      func.percentile_cont(0.5).within_group(get_metric_column(metric)),
    ).filter(
      Measurement.asset_id == asset_id, Measurement.timestamp > start, end > Measurement.timestamp
    ).scalar()
  return median
