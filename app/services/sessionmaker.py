import os
from dotenv import load_dotenv
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

load_dotenv()

db_user = os.environ.get("DB_USER", "root")
db_password = os.environ.get("DB_PASSWORD", "password")
db_host = os.environ.get("DB_HOST", "localhost")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "turbines")

db = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name))

def get_session_dependency() -> Generator:
    with Session(db) as session:
      yield session