# main.py

from operacoes import adicao, subtracao, multiplicacao, divisao

# Ler dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Chamar as funções e imprimir os resultados
print(f"Adição: {adicao(num1, num2)}")
print(f"Subtração: {subtracao(num1, num2)}")
print(f"Multiplicação: {multiplicacao(num1, num2)}")
print(f"Divisão: {divisao(num1, num2)}")
