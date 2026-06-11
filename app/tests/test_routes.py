from main import app
from conftest import client

def test_create_user_sucess():
    payload = {
        "name": "Teste",
        "email": "teste@gmail.com",
        "phone": "(31) 9 71871761",
        "cpf": "12481457633",
        "password": "12345678"
    }

    response = client.post("/create_users/", json=payload)

    assert response.status_code == 200


def test_create_user_failed():
    payload = {
        "name": "Teste",
        "email": "teste@gmail.com",
        "phone": "(31) 9 7187176",
        "cpf": "12481457633",
        "password": "12345678"
    }

    response = client.post("/create_users/", json=payload)

    assert response.status_code == 400
