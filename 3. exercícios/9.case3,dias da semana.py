import os
os.system("clear")

numero = int(input("""

1- Domingo
2- Segunda-feira
3- Terça-feira
4- Quarta-feira
5- Quinta-feira
6- Sexta-feira
7- Sábado
   \nInforme o número do dia:

"""))
match numero: 
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("número inválido")

if numero == 1 or numero== 7:
    print(f"{numero}. Este dia é um final de semana")
if numero >= 2 and numero<= 6:
    print(f"{numero}. Este dia é um dia útil.")