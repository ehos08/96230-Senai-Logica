import os
os.system("cls")

soma = 0
for i in range (5):
    numero =  int(input("Digite um número para somar: "))
    #soma = soma + numero
    soma += numero

print()
print(f"A soma dos números é igual a {soma}.")