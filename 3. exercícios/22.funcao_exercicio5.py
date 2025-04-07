import os
os.system("cls||clear")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

def mediaF(nota1, nota2):
    calculo = (nota1 + nota2)
    media_notas = calculo/2
    return media_notas
def aprovacao(media):
    if media <= 4:
        print("Você foi reprovado! Se esforce mais na próxima.")
    elif media < 6.9:
        print("Você caiu na recuperação! Se esforce para conseguir.")
    else:
        print("Parabéns! Você foi aprovado com êxito.")
    return media
media_final = mediaF(nota1, nota2)
aprovacao(media_final)