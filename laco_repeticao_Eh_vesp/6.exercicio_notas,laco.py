import os
os.system("cls")

media = 0
for i in range (4):
    nota =  float(input("Digite suas notas: "))
    media += nota
print()
print(f"A soma das  notas é igual a : {media/4}")
