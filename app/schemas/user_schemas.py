from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str = Field(min_length=8, max_length=32)


class UserData(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str = Field(min_length=8, max_length=32, default=None) 



class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=32, default=None) 