import os 
os.system("clear")

idade = int(input("Digite sua idade: "))

while idade < 18:
    print("Somente maiores de 18 anos são permitidos")
    idade = int(input("Digite sua idade: "))
print("FIM")

#JEITO ALTERNATIVO:
while True:
    idade = int(input("Digite sua idade: "))
    if idade < 18:
     print("Somente maiores de 18 anos são permitidos")
    else:
     break