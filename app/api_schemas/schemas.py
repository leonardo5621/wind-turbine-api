from pydantic import BaseModel, Field
from constants.metrics import Metrics

class Asset(BaseModel):
  id: int
  name: str

class MeanIn(BaseModel):
  metric: Metrics
  startTime: int = Field(description="Starting point for mean calculation, it should be provided as a timestamp epoch (1701358195 for example)")
  endTime: int = Field(description="End point for mean calculation, it should be provided as a timestamp epoch  value (1701358195 for example)")
  asset_ids: list[int]

class MetricMean(BaseModel):
  asset_name: str
  mean: float