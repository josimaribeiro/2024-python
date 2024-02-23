# validar_cpf.py


def validar_cpf(cpf):
    # Implemente a lógica de validação do CPF aqui
    # Retorna True se o CPF for válido, False caso contrário
    # Este exemplo é bastante simplificado e não cobre todas as regras de validação do CPF

    if len(cpf) != 11 or not cpf.isdigit():
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0

    if resto != int(cpf[9]):
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True
