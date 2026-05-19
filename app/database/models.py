from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nome = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(14), unique=True, nullable=False)