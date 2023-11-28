from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql+psycopg2://root:password@localhost:5431/turbines")

session_maker = sessionmaker(bind=db)