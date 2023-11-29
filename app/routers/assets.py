from fastapi import APIRouter, Depends
from fastapi.resposes import PlainTextResponse
from services import assets, sessionmaker
from api_schemas.schemas import Asset
from sqlalchemy.orm import Session

router = APIRouter(
  prefix="/assets"
)

@router.get("/", tags=["assets"])
def get_assets(session: Session = Depends(sessionmaker.get_session_dependency)) -> list[Asset]:
  available_assets = assets.get_assets(session)
  return available_assets
    