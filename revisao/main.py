# main.py


from validar_cpf import validar_cpf

# Pedir o CPF
cpf = input("Digite seu CPF (apenas números): ")

# Validar o CPF e imprimir o resultado
if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido.")
