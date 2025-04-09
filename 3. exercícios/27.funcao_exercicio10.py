import os
os.system("cls||clear")
nota = 0
QUANTIDADE = 2
for i in range(1,QUANTIDADE + 1):
    nota += float(input(f"Informe sua {i}º nota: "))
    def media(media):
     media = nota / QUANTIDADE
     return media
    mediaF = media(nota)
print(f"A sua média é igual a: {mediaF:.1f}")
def aprovacao(mediaF):    
  if mediaF >= 7:
    print("Você está aprovado.")
  else:
    print("Você está reprovado.")
aprovar = aprovacao(mediaF)