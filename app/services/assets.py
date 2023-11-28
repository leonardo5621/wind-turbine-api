from sqlalchemy import select
from .sessionmaker import session_maker
from models.schemas import Asset

def get_assets():
  with session_maker() as session:
    assets = session.query(
      Asset.id.label("id"), Asset.name.label("name")
    ).all()
  return assets
  