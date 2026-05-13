from fastapi import APIRouter, Depends
from app.services.user_service import create_user_service, update_user_service
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
def update_user(
    id_user: int,
    user_data: UserData,
    db: Session = Depends(get_db)
):


    return update_user_service(db=db, id_user=id_user, user_data=user_data)