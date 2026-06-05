from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, LargeBinary

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nome = Column(String(100), unique=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(LargeBinary(225), nullable=False)
    cpf = Column(LargeBinary(225), nullable=False)
    password = Column(String(225), unique=False, nullable=False)