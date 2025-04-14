import os
os.system("cls||clear")

contador_impar = 0
contador_par = 0
list = []
for e in range(1,7):
 numeros = int(input(f"Informe o {e} número: "))
 list.append(numeros)

 if numeros % 2 == 0:
    contador_par += 1
 else:
    contador_impar +=1
print(f"\nQuantidade total de números: {list} ")
print(f"Quantidade de números pares informados: {contador_par}.\n\t")
print(f"Quantidade de números ímpares informados: {contador_impar}.\n\t")

