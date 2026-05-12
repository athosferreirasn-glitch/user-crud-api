from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://Athos:mbAth0307@localhost:3306/banco_users"

engine = create_engine(DATABASE_URL)

conn = engine.connect()
