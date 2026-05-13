from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://Athos:mbAth0307@localhost:3306/banco_users"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

conn = engine.connect()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()