from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str = Field(min_length=8, max_length=32)


class UserData(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str = Field(min_length=8, max_length=32, default=None) 



class UserLogin:
    def __init__(
        self, email: EmailStr, 
        password: str = Field(
            min_length=8, 
            max_length=32, 
            default=None)):

        self.email = email
        self.password = password