import phonenumbers as ph
from fastapi import HTTPException



def validator_number(phone: str):
    try:
        phone = ph.parse(phone, "BR")

        if ph.is_valid_number(phone):

            return ph.format_number(
                phone,
                ph.PhoneNumberFormat.E164
            )
        
        raise HTTPException(
            status_code=400,
            detail='Número de telefone inválido'
        )
    except:
        raise HTTPException(
            status_code=400,
            detail='Número de telefone inválido'
        )