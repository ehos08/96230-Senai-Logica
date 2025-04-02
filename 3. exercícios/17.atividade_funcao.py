import os
import time
def logo_senai():
 os.system("cls||clear")
 print("\n         ====SENAI DENDEZEIROS===")

def calculoS(numero1, numero2):
 soma = primeiro_numero + segundo_numero
 return soma
def calculoSub(numero1, numero2):
 subtracao = primeiro_numero - segundo_numero
 return subtracao
def calculoM(numero1, numero2):
 multi = primeiro_numero * segundo_numero
 return multi
def calculoDiv(numero1, numero2):
 div = primeiro_numero / segundo_numero
 return div
logo_senai()

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

resultadoS = calculoS(primeiro_numero, segundo_numero)
print(f"\tA soma dos dois números é igual a: {resultadoS:.1f}")
resultadoSub = calculoSub(primeiro_numero, segundo_numero)
print(f"\tA subtração dos dois números é igual a: {resultadoSub:.1f}")
resultadoM = calculoM(primeiro_numero, segundo_numero)
print(f"\tO produto dos dois números é igual a: {resultadoM:.1f}")
resultadoD = calculoDiv(primeiro_numero, segundo_numero)
print(f"\tA divisão entre os dois números é igual a: {resultadoD:.1f}")
