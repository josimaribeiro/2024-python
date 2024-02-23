# operacoes.py

def adicao(num1, num2):
    resultado = num1 + num2
    return resultado

def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado

def divisao(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        return resultado
    else:
        return "Erro: Divisão por zero não é permitida"
