import os 
os.system("cls||clear")

lista = []
for i in range(1,4):
 nota = float(input(f"Digite sua {i}º nota: "))
 lista.append(nota)
media = sum(lista) / i
 
print()
for nota in lista:
 print(nota)
print(f"Sua média foi {media}.")

#aprovado?
if media <= 4:
 print("Reprovado, se esforce mais na próxima.")
elif media > 10 or media < 0:
 print("Informe uma nota válida.")
else:
 print("Parabéns, você está aprovado.")