import os 
os.system("cls||clear")

numero = int(input("Digite um número de 1 a 10: "))
def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} X {i} = {numero * i}")
print(f"\n TABUADA DO {numero}")
tabuada(numero)