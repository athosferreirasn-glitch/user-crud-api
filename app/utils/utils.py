from types import SimpleNamespace
import json
from app.security.cryptocraphy import encrypt_data


SENSITIVE_FIELDS = {
    'cpf',
    'phone'
}

def data_conversion_crypt(data: object):

    data_json = data.model_dump_json(indent=0)

    data_dict = json.loads(data_json)

    data_crypt = {}

    for c, v in data_dict.items():
        if c in SENSITIVE_FIELDS:
            data_crypt[c] = data_dict[c]
        
    for c, v in data_crypt.items():

        if not v:
            return False

        nonce, tag, ciphertext = encrypt_data(data=v)

        data_dict[c] = ciphertext

    user = SimpleNamespace(**data_dict)

    if user:
        return user