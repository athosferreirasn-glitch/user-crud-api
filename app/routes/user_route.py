from fastapi import APIRouter, Depends
from app.services.user_service import create_user_service, update_user_service, delete_user_service, get_users_service
from app.schemas.user_schemas import UserCreate, UserData
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services.auth_service import get_password_hash

router = APIRouter(prefix='/user')


@router.post('/create_users')
def create_user_router(
    user: UserCreate,
    db: Session = Depends(get_db) 
):

    hashed_pwd = get_password_hash(password=user.password)

    user.password = hashed_pwd
    
    create_user_service(db=db, user=user)

    return {
        'message': 'usuário criado e cadastrado com sucesso'
    }


@router.patch('/update_user/{id_user}')
def update_user_router(
    id_user: int,
    user_data: UserData,
    db: Session = Depends(get_db)
):

    hashed_pwd = get_password_hash(password=user_data.password)

    user_data.password = hashed_pwd


    update_user_service(db=db, id_user=id_user, user_data=user_data)

    return {
        'message': 'dados atualizados com sucesso'
    }



@router.delete('/delete_user/{user_id}')
def delete_user_router(
    user_id: int,
    db: Session = Depends(get_db)
):

    delete_user_service(db=db, user_id=user_id)

    return {
        'message': 'usuário deletado com sucesso'
    }



@router.get('/get_users/{option}')
def get_users_router(
    option: int,
    db: Session = Depends(get_db)
):

    users_data = get_users_service(db=db, option=option)

    if option == 0:

        users = []

        for user in users_data:
            users.append({
                'name': user.nome,
                'email': user.email,
                'phone': user.phone
            })

        return users

    return {
        'name': users_data.nome,
        'email': users_data.email,
        'phone': users_data.phone
    }