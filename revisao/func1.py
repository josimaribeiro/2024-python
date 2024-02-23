def soma(num1,num2):
    soma = num1 + num2
    return soma

def subtracao(num1,num2):
    dif = num1 - num2
    return dif


def multiplicao(num1,num2):
    mult = num1 * num2
    return mult

def divisao(num1,num2):
    div = num1 / num2
    return div



valor1 = float(input("Digite um valor.....: "))
valor2 = float(input("Digite outro valor..: "))

print("A soma é....... %.4f" % soma(valor1,valor2))
print("A diferenca é.. %.4f" % subtracao(valor1,valor2))
if valor2 !=0:
    print("A divisao é.... %.4f" % divisao(valor1,valor2))
else:
    print("Impossivel dividor por zero")
    
