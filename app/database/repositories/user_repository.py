from app.database.models import Usuario


def create_user(db, nome, email, phone):
    usuario = Usuario(
        nome=nome,
        email=email,
        phone=phone
    )

    db.add(usuario)

    db.commit()

    db.refresh(usuario)

    return usuario