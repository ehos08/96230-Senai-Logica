import os
os.system ("clear")

altura= float(input("Digite sua altura em metros: "))
print("Sua altura é:",altura)
sexo = input(""" Masculino: M   Feminino: F
Digite seu sexo: """).upper()
match sexo:
 case "M":
        print("Masculino")
        resultado = (72.7 * altura) - 58
        print(f"Este é o peso ideal para você: {resultado:.1f}kg.")
 case "F":
        print("F")
        resultado = (62.1 * altura) - 44.7
        print(f"Este é o peso ideal para você: {resultado:.1f}kg.")