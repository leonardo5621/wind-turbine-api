from pydantic import BaseModel
from constants.metrics import Metrics

class Asset(BaseModel):
  id: int
  name: str

class MeanIn(BaseModel):
  metric: Metrics
  startTime: int
  endTime: int
  asset_ids: list[int]

class MetricMean(BaseModel):
  asset_name: str
  mean: float