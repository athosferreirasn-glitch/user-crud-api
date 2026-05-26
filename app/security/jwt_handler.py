from datetime import datetime, timedelta, timezone
import jwt
from app.database.repositories.user_repository import get_user_by_id_repo
from app.database.connection import get_db
from fastapi import Depends



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



def get_current_user(token, db: Session = Depends(get_db)):

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    user = get_user_by_id_repo(id=user.id, db=db)
    
    user.id = payload.get("id")

    return user