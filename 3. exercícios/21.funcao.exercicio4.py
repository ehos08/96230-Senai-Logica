import os
os.system("cls||clear")
numero = int(input("Digite um número: "))

def FV(FV):
    if numero == 0:
        print(f"O número {numero} é neutro.")
    elif numero < 0:
     print(f"O número {numero} é negativo.")
    else:
        print(f"O número {numero} é positivo.")

resultado = FV(numero)