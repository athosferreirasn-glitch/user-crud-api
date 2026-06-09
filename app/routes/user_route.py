from fastapi import APIRouter, Depends
from app.services.user_service import create_user_service, update_user_service, delete_user_service, get_users_service
from app.schemas.user_schemas import UserCreate, UserData, UserLogin
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.services.auth_service import auth_login_service
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(prefix='/user')

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="user/token"
)

def header_auth(token: str = Depends(oauth2_scheme)):

    from app.services.auth_service import auth_autorization_request

    token = auth_autorization_request(token=token)

    if token:

        return token

@router.post('/token')
def login_for_acess_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):

    token = auth_login_service(db=db, user_data_login=form_data)

    return {
        "acess_token": token,
        "type_token": "bearer"
    }



@router.post('/create_users')
def create_user_router(
    user: UserCreate,
    db: Session = Depends(get_db), 
):
    
    create_user_service(db=db, user=user)

    return {
        'message': 'usuário criado e cadastrado com sucesso'
    }


@router.patch('/update_user/{id_user}')
def update_user_router(
    id_user: int,
    user_data: UserData,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):

    if token:
        hashed_pwd = get_password_hash(password=user_data.password)

        user_data.password = hashed_pwd


        update_user_service(db=db, id_user=id_user, user_data=user_data)

        return {
            'message': 'dados atualizados com sucesso'
        }



@router.delete('/delete_user/{user_id}')
def delete_user_router(
    user_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):

    if token:
        delete_user_service(db=db, user_id=user_id)

        return {
            'message': 'usuário deletado com sucesso'
        }



@router.get('/get_users/{option}')
def get_users_router(
    option: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme) 
):

    if token:
        users_data = get_users_service(db=db, option=option)

        if option == 0:

            users = []

            for user in users_data:
                users.append({
                    'name': user.nome,
                    'email': user.email,
                })

            return users

        return {
            'name': users_data.nome,
            'email': users_data.email,
        }


