from app.utils.validators import validator_cpf, validator_number


def test_valid_cpf():
    assert validator_cpf('12481457633') == True


def test_invalid_cpf():
    assert validator_cpf('12481457621') == False

def test_valid_number():
    assert validator_number('+5531971871761') == True

def test_invalid_number():
    assert validator_number('+55319874578521') == False