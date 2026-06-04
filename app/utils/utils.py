from pydantic import BaseModel, EmailStr, Field
import json


SENSITIVE_FIELDS = {
    'email',
    'phone'
}

def data_conversion_crypt(data: object):

    data_str = data.model_dump_json(indent=0)

    data_json = json.loads(data_str)

    data_crypt = {}

    for c, v in data_json.items():
        if c in SENSITIVE_FIELDS:
            data_crypt[c] = data_json[c]

    return data_crypt.values()