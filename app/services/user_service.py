from app.database.repositories.user_repository import create_user_repo, update_user_repo
from fastapi import HTTPException
from app.utils.validators import validator_number


def create_user_service(db, user):

    user.phone = validator_number(phone=user.phone)

    create_user_repo(db=db, user=user)


def update_user_service(db, id_user, user_data):

    if user_data.phone:
        user_data.phone = validator_number(phone=user_data.phone)

    update_user_repo(db=db, id=id_user, user_data=user_data)