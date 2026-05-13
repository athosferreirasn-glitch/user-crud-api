from app.database.repositories.user_repository import create_user_repo
from fastapi import HTTPException


def create_user_service(db, user):

    if user.name.replace(' ', '').isdigit():
        HTTPException(status_code=404, detail='Nome inválido, não pode conter números')

    create_user_repo(db=db, user=user)