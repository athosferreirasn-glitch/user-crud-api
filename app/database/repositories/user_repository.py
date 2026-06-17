from app.database.models import Usuario
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def create_user_repo(db, user):
    db_user = Usuario(
        nome=user.name,
        email=user.email,
        phone=user.phone,
        hash_phone=user.hash_phone,
        cpf=user.cpf,
        hash_cpf=user.hash_cpf,
        password=user.password
    )

    try:
        db.add(db_user)

        db.commit()

        db.refresh(db_user)

        return db_user
        
    except IntegrityError:
        return None


def get_user_by_id_repo(db, id):
    user = db.query(Usuario).filter(Usuario.id == id).first()

    if not user:
        return None

    return user
    

def get_user_by_email_repo(db, email):
    user = db.query(Usuario).filter(Usuario.email == email).first()

    if not user:
        return None
    return user


def get_users_repo(db):

    users_data = db.query(Usuario).all()

    if not users_data:
        return None

    return users_data


def update_user_repo(db, user, update_data: dict):

    for key, value in update_data.items():
        setattr(user, key, value)

    try:
        db.commit()
        db.refresh(user)

        return user
    except Exception:
        return None


def delete_user_repo(db, delete_data):

    if delete_data:
        db.delete(delete_data)

        db.commit()

        return delete_data