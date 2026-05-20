# Nome: Sistema CRUD de gerenciamento de usuários


# CRUD de Usuários
API CRUD para gerenciamento de usuários desenvolvida com FastAPI, SQLAlchemy e MySQL, com foco em organização de arquitetura backend e integração com banco de dados relacional.


# Principais funcionalidades:
- Cadastro de usuários
- Alteração de dados
- Visualização de dados por filtragem
- Exclusão de usuários

Possíveis melhorias:
- Hash seguro de senha
- Sistema de autenticação JWT
- Controle de sessão
- Criptografia de dados sensíveis
- Controle de permissões


# Entidades:
- Usuários:
    id: int
    name: str
    email: str
    phone: str


# Pré-requisitos:
- Python 3.12+
- FastAPI
- MySQL
- SQLAlchemy



# Instalação e uso

git clone <https://github.com/athosferreirasn-glitch/user-crud-api>

cd crud_users

python -m venv .env

.env\Scripts\activate

pip install -r requirements.txt

Crie um banco MySQL chamado:
banco_users

uvicorn main:app --reload
