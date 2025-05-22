import os 
os.system("clear")

contador = 0
par = 0
impar = 0
soma_par = 0
soma= 0

while True:
    numero = int(input(f"Digite o {contador+1}º número: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        par += 1
        soma_par = numero
    else:
        impar += 1

    contador += 1
    soma += numero    
media_par = soma_par/par
media_geral = soma/contador
print(f"\nQuantidade de números pares: {par}")
print(f"\n Quantidade de números ímpares: {impar}")
print(f"\n A média dos números pares é igual a: {media_par}")
print(f"A média total dos números é: {media_geral}")