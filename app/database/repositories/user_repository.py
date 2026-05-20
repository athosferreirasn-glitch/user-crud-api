from app.database.models import Usuario


def create_user_repo(db, user):
    db_user = Usuario(
        nome=user.name,
        email=user.email,
        phone=user.phone,
        password=user.password
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def get_user_by_id_repo(db, id):
    user = db.query(Usuario).filter(Usuario.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user


def get_users_repo(db):

    users_data = db.query(Usuario).all()

    if not users_data:
        HTTPException(
            status_code=204,
            detail='Não há usuários cadastrados'
        )

    return users_data


def update_user_repo(db, user, update_data: dict):

    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user



def delete_user_repo(db, delete_data):

    if delete_data:
        db.delete(delete_data)

        db.commit()

        return delete_data