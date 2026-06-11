from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_sucess():
    payload = {
        "name": "Teste",
        "email": "teste@gmail.com",
        "phone": "(31) 9 71871761",
        "cpf": "12481457633",
        "password": "12345678"
    }

    response = client.post("/create_users/", json=payload)