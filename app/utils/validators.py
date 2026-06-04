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



def validator_cpf(cpf):

    cpf_verify = str(cpf)

    cont = 10

    sum = 0

    for n in cpf_verify[:9]:
        sum += cont * int(n)
        cont -= 1

    resto = sum % 11

    if resto < 2:
        digit_1 = 0
    else:
        digit_1 = 11 - resto


    if digit_1 != int(cpf[9]):
        return False

    cpf_verify = cpf[:9] + str(digit_1)

    cont = 11

    sum = 0

    for n in cpf_verify:
        sum += cont * int(n)
        cont -= 1

    resto = sum % 11

    if resto < 2:
        digit_2 = 0
    else:
        digit_2 = 11 - resto

    if digit_2 != int(cpf[10]):
        return False
        
    return True