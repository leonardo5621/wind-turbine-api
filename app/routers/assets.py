from fastapi import APIRouter

router = APIRouter(
  prefix="/assets"
)

@router.get("/")
async def get_assets():
  return []