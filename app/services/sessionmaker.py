from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

db = create_engine("postgresql+psycopg2://root:password@localhost:5431/turbines")

def get_session_dependency() -> Generator:
    with Session(db) as session:
      yield session