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