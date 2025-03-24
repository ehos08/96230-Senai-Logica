import os
os.system ("clear")

print("\t\tCalcule sua média\n")
nota = 0
contador = 0
while True:
    nota += float(input("Digite sua nota: "))
    if nota < 0 or nota > 10:
        print("formato de nota inválido!")
    notas = (input("você deseja adicionar mais uma nota? ('S' ou 'N') "))
    contador += 1
    if notas == "n":
        print(f"A média é igual a {nota/contador}.")
        break

     