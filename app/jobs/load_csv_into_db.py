import pandas as pd
from sqlalchemy import create_engine, DateTime, Integer, String
from app.models.db_schemas import Asset, Measurement, Base


db = create_engine("postgresql+psycopg2://root:password@localhost:5431/turbines")

def load_assets_table():
  df = pd.read_csv("./data_sources/assets.csv")

  try:
    df.rename(columns={"asset_id": "id"}, inplace=True)
    df.to_sql(Asset.__tablename__, db, if_exists="append", index=False, dtype={"id": Integer(), "name": String(50)})
  except Exception as err:
    print("Failed to load csv into DB", err)

def load_measurements_table():
  df = pd.read_csv("./data_sources/measurements.csv")

  try:
    df.to_sql(Measurement.__tablename__, db, if_exists="append", index=True, index_label="id",
      dtype={"timestamp": DateTime, "asset_id": Integer()},
    )
  except Exception as err:
    print("Failed to load csv into DB", err)

def load_all():
  Base.metadata.create_all(db)  
  load_assets_table()
  load_measurements_table()

  db.dispose()