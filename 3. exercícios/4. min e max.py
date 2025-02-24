import os
os.system("clear")
 
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o primeiro número: "))

menor = min(numero1,numero2)
maior = max(numero1,numero2)
if numero1 == numero2:
    print("Os números são iguais")
else: 
    print (f"Este é o maior número: {maior} - Este é o menor número: {menor}")