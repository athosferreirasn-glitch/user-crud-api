from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str


class UserData(BaseModel):
    name: str
    email: EmailStr
    phone: str