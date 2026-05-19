from fastapi import HTTPException
from app.utils.validators import validator_number
from app.database.repositories.user_repository import get_user_by_id_repo, update_user


def create_user_service(db, user):

    user.phone = validator_number(phone=user.phone)

    create_user_repo(db=db, user=user)


def update_user_service(db, id_user, user_data):

    user = get_user_by_id_repo(db=db, id=id_user)

    update_data = user_data.dict(
        exclude_unset=True
    )

    if not update_data:
        raise HTTPException(status_code=400, detail='Nenhum dado enviado')

    updated_user = update_user(
        db=db,
        user=user,
        update_data=update_data
    )

    return updated_user