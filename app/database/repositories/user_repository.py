from app.database.models import Usuario


def create_user_repo(db, user):
    db_user = Usuario(
        nome=user.name,
        email=user.email,
        phone=user.phone
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



def update_user_repo(db, id, user_data):

    user = get_user_by_id_repo(db=db, id=id)

    if user_data.name:
        user.nome = user_data.name

    if user_data.email:
        user.email = user_data.email

    if user_data.phone:
        user.phone = user_data.phone

    db.commit()
    db.refresh(user)

    return user