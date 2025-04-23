import os
os.system("cls||clear")

list = []
QUANTIDADE = 5
def vetor():
 for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
        numero = 0
    list.append(numero)
vetor()
print("Valores na lista:", list)