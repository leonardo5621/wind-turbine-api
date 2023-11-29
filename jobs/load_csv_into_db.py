import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, DateTime, Integer, String, Connection
from app.models.db_schemas import Asset, Measurement, Base

load_dotenv()

db_user = os.environ.get("DB_USER", "root")
db_password = os.environ.get("DB_PASSWORD", "password")
db_host = os.environ.get("DB_HOST", "localhost")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "turbines")


db = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name))

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