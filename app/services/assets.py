from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from models.db_schemas import Asset

def get_assets(session: Session):
  assets = session.query(
    Asset.id.label("id"), Asset.name.label("name")
  ).all()
  return assets

def check_valid_asset_ids(session: Session, asset_ids: list[int]) -> bool:
  valid_assets_count = session.query(
    func.count(Asset.id)
  ).filter(
    Asset.id.in_(asset_ids)
  ).scalar()
  return valid_assets_count == len(asset_ids)
  