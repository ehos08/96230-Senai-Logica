import os 
os.system("cls||clear")
#Criando uma lista
lista = []
#Adicionando elementos a lista
for i in range(3):
 nota = float(input(f"Digite sua nota: "))
 lista.append(nota)
 #exibindo a lista
print()
for nota in lista:
 print(nota)