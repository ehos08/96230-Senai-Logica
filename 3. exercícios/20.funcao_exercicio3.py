import os
os.system("cls||clear")

numero = int(input("Digite um número e descubra se ele é par ou ímpar: "))

def resultado(numero):
    if numero == 0:
     return"neutro"
    elif numero %2 == 0:
      return "par"
    else:
     return"ímpar"
resultadofinal = resultado(numero)
print(f"O número {numero} é {resultadofinal}.")