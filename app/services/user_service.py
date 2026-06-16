from fastapi import HTTPException
from app.utils.validators import validator_number, validator_cpf
from app.database.repositories.user_repository import (
    create_user_repo,
    get_user_by_id_repo, 
    update_user_repo,
    delete_user_repo,
    get_users_repo)
from app.utils.utils import data_conversion_crypt
from app.security.password import get_data_hash, verify_password
import phonenumbers as ph



def create_user_service(db, user):


    if not validator_number(phone=user.phone):
        raise HTTPException(
            status_code=400,
            detail='Número de telefone inválido'
        )

    if validator_number(phone=user.phone):
        user.phone = ph.format_number(
            numobj=ph.parse(number=user.phone, region="BR"),
            num_format=ph.PhoneNumberFormat.NATIONAL
        )

    verify_cpf = validator_cpf(cpf=user.cpf)

    if not verify_cpf:
        raise HTTPException(
            status_code=400,
            detail='Número de CPF inválido'
        )

    user.password = get_data_hash(data=user.password)

    user.hash_phone = get_data_hash(data=user.phone)

    user.hash_cpf = get_data_hash(data=user.cpf)

    user_encrypt = data_conversion_crypt(data=user)

    create_user_repo(db=db, user=user_encrypt)


def update_user_service(db, id_user, user_data):

    user = get_user_by_id_repo(db=db, id=id_user)

    update_data = user_data.dict(
        exclude_unset=True
    )

    if not verify_password(plain_password=user_data.password, hashed_password=user.password):
        raise HTTPException(
            status_code=401,
            detail='Senha incorreta'
        )

    if not update_data:
        raise HTTPException(status_code=400, detail='Nenhum dado enviado')

    updated_user = update_user_repo(
        db=db,
        user=user,
        update_data=update_data
    )

    return updated_user



def delete_user_service(db, user_id):

    delete_data = get_user_by_id_repo(db=db, id=user_id)

    if not delete_data:
        raise HTTPException(status_code=400, detail='Nenhum dado enviado')

    user_delete_data = delete_user_repo(db=db, delete_data=delete_data)

    return user_delete_data



def get_users_service(db, option):

    if option == 0:
        users_data = get_users_repo(db=db)
        return users_data
    else:
        user = get_user_by_id_repo(db=db, id=option)
        return user