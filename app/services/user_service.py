from app.database.repositories.user_repository import create_user_repo
from fastapi import HTTPException
from app.utils.validators import validator_number


def create_user_service(db, user):

    user.phone = validator_number(phone=user.phone)

    create_user_repo(db=db, user=user)