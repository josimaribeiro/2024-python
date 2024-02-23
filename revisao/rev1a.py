// criar uma lista
lista = []

CONT = 10
// preencher uma lista
for i in range(CONT):
    lista.append(int(input("Digite um valor : ")))
    
// exibir lista
print(lista)
qtd = 0

// solicitar um numero a ser pesquisado
numero_contar = int(input("Digite valor  a ser contado: "))
for i in range(CONT):
    // comparar cada posicão com o numero digitado
    if (lista[i] == numero_contar):
        qtd +=1

print("O numero " , str(numero_contar) ," aparece" ,  str(qtd), " vez(es)")





