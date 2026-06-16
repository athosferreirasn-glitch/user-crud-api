from passlib.context import CryptContext
from typing import Any
from fastapi import HTTPException

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_data_hash(data: str) -> str:

    if not data:
        raise HTTPException(
            status_code=422,
            detail='Credenciais inválida'
        )

    return pwd_context.hash(data)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)