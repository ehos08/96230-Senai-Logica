import os
os.system("cls||clear")
nota = 0
for i in range(1,4):
    def media(media):
     media = nota / 3
     return media
    nota += float(input(f"Informe sua {i}º nota: "))
    mediaF = media(nota)

print(f"A sua média é igual a: {mediaF:.2f}")
if mediaF >= 7:
    print("Você está provado.")
elif mediaF >= 5:
    print("Você está em recuperação.")
else:
    print("Você está reprovado.")