import os
os.system ("cls")

media = 0
for i in range (3):
    nota =  float(input("Digite suas notas: "))
    media += nota

if media >= 7:
     print (f"Sua nota foi: {media/3:.2f}, Reprovado(a)! Boa sorte na próxima.")
elif media <= 4:
     print (f"Sua nota foi: {media/3:.2f}, Parabéns! Você foi aprovado(a)")
else :
     print (f"Sua nota foi: {media/3:.2f}, Parabéns! você foi aprovado(a)")
