import pandas as pd
from sqlalchemy import create_engine, DateTime, Integer, String, Connection
from models.db_schemas import Asset, Measurement, Base


db = create_engine("postgresql+psycopg2://root:password@localhost:5431/turbines")

def load_assets_table(conn: Connection):
  df = pd.read_csv("./data_sources/assets.csv")

  df.rename(columns={"asset_id": "id"}, inplace=True)
  df.to_sql(Asset.__tablename__, conn, if_exists="append", index=False, dtype={"id": Integer(), "name": String(50)})

def load_measurements_table(conn: Connection):
  df = pd.read_csv("./data_sources/measurements.csv")
  df.dropna(inplace=True)
  df.to_sql(Measurement.__tablename__, conn, if_exists="append", index=True, index_label="id",
    dtype={"timestamp": DateTime, "asset_id": Integer()},
  )

def load_all():
  with db.connect() as conn:
    try:
      Base.metadata.create_all(conn)  
      load_assets_table(conn)
      load_measurements_table(conn)
      conn.commit()
    except Exception as err:
      print("Failed to load csv into database", err)
      print("Rolling back transaction")
      conn.rollback()


  db.dispose()