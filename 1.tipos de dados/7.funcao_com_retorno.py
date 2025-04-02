import os 
os.system("cls||clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma /2
    return media
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

media = calcular_media(primeiro_numero, segundo_numero)
print(f"Média: {media:.1f}")
