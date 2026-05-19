from fastapi import APIRouter, Depends
from app.services.user_service import create_user_service, update_user_service, delete_user_service, get_users_service
from app.schemas.user_schemas import UserCreate, UserData
from app.database.connection import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user')


@router.post('/create_users')
def create_user_router(
    user: UserCreate,
    db: Session = Depends(get_db) 
):
    
    create_user_service(db=db, user=user)


@router.patch('/update_user/{id_user}')
def update_user_router(
    id_user: int,
    user_data: UserData,
    db: Session = Depends(get_db)
):


    return update_user_service(db=db, id_user=id_user, user_data=user_data)



@router.delete('/delete_user/{user_id}')
def delete_user_router(
    user_id: int,
    db: Session = Depends(get_db)
):

    return delete_user_service(db=db, user_id=user_id)



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