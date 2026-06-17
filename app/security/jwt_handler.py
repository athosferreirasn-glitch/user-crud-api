from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "MSecKe&21022205"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30


def create_acess_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )

        return payload

    except ExpiredSignatureError:
        return None

    except InvalidTokenError:
        return None

