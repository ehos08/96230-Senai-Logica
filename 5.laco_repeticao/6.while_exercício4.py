import os
os.system ("clear")

nota = 0
while True:
    nota += int(input("Digite sua nota: "))
    if nota > 0:
     laco = (input("Deseja inserir outra nota? (S/N): "))
     if laco != "n":
       soma = nota + nota
       contador = 0
       contador += soma
       media = nota/contador
     else:
      print(f"A média total dos números é {media:.1f}")
    else:
       print(f"Formato inválido, a média total dos números é {media:.1f}.") 
       break
      