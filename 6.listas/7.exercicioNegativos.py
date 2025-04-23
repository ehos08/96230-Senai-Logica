import os
os.system("cls||clear")

lista = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
        numero = 0  
    lista.append(numero)

print("Valores no vetor:", lista)