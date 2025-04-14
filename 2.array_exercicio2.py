import os 
os.system("cls||clear")

lista = []
for i in range(1,5):
 nota = float(input(f"Digite sua {i}º nota: "))
 lista.append(nota)

media = sum(lista) / i
def aprovacao(media):
 if media < 5:
  print("Reprovado, se esforce mais na próxima.")
 elif media > 10 or media < 0:
  print("Informe uma nota válida.")
 elif 5 <= media < 7:
  print("Recuperação, você ainda tem chances.") 
 else:
  print("Parabéns, você está aprovado.") 
  return media

print(f"Sua média foi {media:.1f}")
aprovacao(media)
