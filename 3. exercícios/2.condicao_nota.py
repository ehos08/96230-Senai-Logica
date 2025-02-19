#limpar terminal
import os 
os.system ("clear")

nota1 = float(input ("digite sua primeira nota: "))
nota2 = float(input ("digite sua segunda nota: "))
nota3 = float(input ("digite sua terceira nota: "))
media : float
soma : float
 
soma = (nota1 + nota2 + nota3)
media = soma / 3
if media < 7:
    print (f"Sua nota foi: {media:.2f}, Reprovado(a)! Boa sorte na próxima.")
elif media == 7:
    print (f"Sua nota foi: {media:.2f}, Parabéns! Você foi aprovado(a)")
else :
    print (f"Sua nota foi: {media:.2f}, Parabéns! você foi aprovado(a)")
