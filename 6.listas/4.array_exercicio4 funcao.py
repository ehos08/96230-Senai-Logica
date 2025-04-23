import os
os.system("clear")

list = []
QUANTIDADE_NUMEROS = 6
def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    list.append(numero)

pares, impares = pares_impares(list)
print("\nMostrando números")
for i, numero in enumerate(list, start=1):
    print(f"{i}º número: {numero}")

print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")