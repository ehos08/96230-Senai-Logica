import os 
os.system("clear")

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")

match operador:
     case "+":
          resultado = numero1 + numero2
     case "-":
          resultado = numero1 - numero2
     case "*":
          resultado = numero1 * numero2
     case "/":
          resultado = numero1 / numero2
     case _:
          resultado ="Opção inválida"
          
print(f"Primeiro número: {numero1}")
print(f"Segundo número: {numero2}")
print(f"Operação escolhida: {operador}")
print(f"Resultado: {resultado:.2f}")