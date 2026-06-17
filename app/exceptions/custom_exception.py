class BusinessException(Exception):
    status_code=400
    detail="Erro de negócio"


class UserNotFoundError(BusinessException):
    status_code=404
    detail="Usuário(s) não encontrado(s)"


class DataAlreadyRegisteredError(BusinessException):
    status_code=409
    detail="Dados ja cadastrados"


class InvalidCPFError(BusinessException):
    status_code=400
    detail="CPF inválido"


class InvalidPhoneError(BusinessException):
    status_code=400
    detail="Número de telefone inválido"


class IncorrectPasswordError(BusinessException):
    status_code=400
    detail="Senha incorreta"


class InvalidDataError(BusinessException):
    status_code=422
    detail="Dados inválidos"


class TokenNotSentError(BusinessException):
    status_code=401
    detail="Token de autenticação não enviado"


class UnauthorizedError(BusinessException):
    status_code=401
    detail="Ação não autorizada"