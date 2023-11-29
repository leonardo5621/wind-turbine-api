from fastapi import APIRouter
from pydantic import BaseModel
from services import assets
from api_schemas.schemas import Asset

router = APIRouter(
  prefix="/assets"
)

@router.get("/")
def get_assets() -> list[Asset]:
  available_assets = assets.get_assets()
  return available_assets