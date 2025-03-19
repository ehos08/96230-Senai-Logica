import os
os.system ("clear")

nome = input("Digite seu nome completo: ")
nota1 = float(input ("digite sua primeira nota: "))
nota2 = float(input ("digite sua segunda nota: "))
media : float
soma : float
soma = (nota1 + nota2)
media = soma / 2

if media >= 9:
    print(f"{nome}. Parabéns! Sua media final foi {media:.1f}, media A")
elif media >=7.5 and media < 9:
    print (f"{nome}. Parabéns! Sua media final foi {media:.1f}, media B")
elif media >=6 and media < 7.5:
    print(f"{nome}. Parabéns! Sua media final foi {media:.1f}, media C")
elif media >=4 and media <6:
    print(f"{nome}. Boa sorte na próxima! Sua media final foi {media:.1f}, media D")
else:
    print(f"{nome}. Boa sorte na próxima! Sua media final foi {media:.1f}, media E") 
