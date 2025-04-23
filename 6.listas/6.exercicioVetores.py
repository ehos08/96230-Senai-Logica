import os
os.system ("cls||clear")

positivo = 0
negativo = 0
list = []
QUANTIDADE_NUMEROS = 5

def positivo_negativo(lista):
    positivo = 0
    negativo = 0
    for numero in lista:
        if numero > 0:
            positivo += 1
        else:
            negativo += 1
    return positivo, negativo
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    list.append(numero)

positivo, negativo= positivo_negativo(list)
soma_positivos= sum(numero for numero in list if numero > 0) 
print("\nMostrando números:")
for i, numero in enumerate(list, start=1):
    print(f"{i}º número: {numero}")

print(f"\nQuantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
print(f"Soma dos números positivos: {soma_positivos}")