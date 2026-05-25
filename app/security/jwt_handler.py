from datetime import datetime, timedelta, timezone
import jwt



SECRET_KEY = "MSecKe&21022205"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30


def create_acess_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt