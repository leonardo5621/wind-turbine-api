from fastapi import APIRouter
from pydantic import BaseModel
from services import assets

router = APIRouter(
  prefix="/assets"
)

class Asset(BaseModel):
  id: int
  name: str

@router.get("/", response_model_exclude={"tax"})
def get_assets() -> list[Asset]:
  available_assets = assets.get_assets()
  return available_assets