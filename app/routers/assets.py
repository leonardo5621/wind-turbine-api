from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
  prefix="/assets"
)

class Asset(BaseModel):
  asset_id: int
  name: str

@router.get("/")
async def get_assets() -> list[Asset]:
  return []