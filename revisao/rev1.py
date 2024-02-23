lista = []

for i in range(5):
    valor = int(input(f"Digite o valor para a posição {i}: "))
    lista.append(valor)

print("Lista final:", lista)

# Solicitar o número a ser pesquisado
numero_pesquisar = int(input("Digite o número a ser pesquisado na lista: "))

# Verificar se o número está na lista
if numero_pesquisar in lista:
    # Obter a posição do número usando o método index
    posicao = lista.index(numero_pesquisar)
    print(f"O número {numero_pesquisar} está na posição {posicao} da lista.")
else:
    print(f"O número {numero_pesquisar} não está na lista.")
