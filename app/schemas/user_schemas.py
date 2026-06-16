from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Any


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    hash_phone: Any | None = None
    cpf: str = Field(min_length=11, max_length=11)
    hash_cpf: Any | None = None
    password: str = Field(min_length=8, max_length=32)


class UserData(BaseModel):
    name: str
    email: EmailStr
    phone: str
    cpf: int = Field(min_length=11, max_length=11)
    password: str = Field(min_length=8, max_length=32, default=None) 



class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=32, default=None) 