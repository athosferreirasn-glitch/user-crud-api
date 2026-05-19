from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str


class UserData(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None