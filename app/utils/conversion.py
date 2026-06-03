from pydantic import BaseModel, EmailStr, Field
import json


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str = Field(min_length=8, max_length=32)


SENSITIVE_FIELDS = {
    'email',
    'phone'
}

def data_conversion(data: object):

    data_str = data.model_dump_json(indent=0)

    data_json = json.loads(data_str)


user = UserCreate(name='Athos', email='athos@gmail.com', phone='31971871761', password='12345678')
data_conversion(data=user)