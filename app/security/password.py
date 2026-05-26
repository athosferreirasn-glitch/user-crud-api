from passlib.context import CryptContext
from typing import Any
from fastapi import HTTPException

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password: str) -> str:

    if not password:
        raise HTTPException(
            status_code=422,
            detail='Senha inválida'
        )

    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)