from app.database.repositories.user_repository import get_user_by_email_repo
from app.security.password import verify_password, get_password_hash
from fastapi import HTTPException


def auth_login_service(db, user_data_login):

    user = get_user_by_email_repo(db=db, email=user_data_login.email)

    if not user:
        raise HTTPException(
            detail='Usuário não encontrado'
        )

    hashed_pwd = get_password_hash(password=user_data_login.password)

    user_data_login.password = hashed_pwd

    if verify_password(plain_password=user_data_login.password, hashed_password=user.password):
        raise HTTPException(
            status_code=401,
            detail='Senha incorreta'
        )


    return user