import os 
os.system ("cls||clear")

list = []
for i in range (1,6):
 numero = input(f"informe o {i}º número: ")
 list.append(numero)

min_numero = min(list)
max_numero = max(list)
#Ordem numérica
list.reverse()   
#================
for i, numero in enumerate(list, start=1):
 print(f"{i}º número: {numero}")
print(f"Menor número: {min_numero}")
print(f"Maior número: {max_numero}") 