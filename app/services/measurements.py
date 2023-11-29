from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from models.db_schemas import Measurement, Asset
from constants.metrics import Metrics


def get_column_from_enum(metric: Metrics):
  if metric == Metrics.WIND_SPEED:
    return Measurement.wind_speed.label(Metrics.WIND_SPEED.value)
  if metric == Metrics.POWER:
    return Measurement.power.label(Metrics.POWER.value)
  if metric == Metrics.AIR_TEMPERATURE:
    return Measurement.air_temperature.label(Metrics.AIR_TEMPERATURE.value)
  return None

def get_assets_metric_average(session: Session, asset_ids: list[int], startTime: int, endTime: int, metric: Metrics):
  start = datetime.fromtimestamp(startTime)
  end = datetime.fromtimestamp(endTime)
  mean_value_query = session.query(
    Measurement.asset_id.label("asset_id"),
    func.avg(get_column_from_enum(metric)).label("mean"),
  ).filter(
    Measurement.asset_id.in_(asset_ids), Measurement.timestamp > start, end > Measurement.timestamp
  ).group_by(
    Measurement.asset_id
  ).subquery()

  mean_results = session.query(
    Asset.name.label("asset_name"),
    mean_value_query.c.mean.label("mean"),
  ).select_from(Asset).join(mean_value_query).all()
  
  return mean_results
