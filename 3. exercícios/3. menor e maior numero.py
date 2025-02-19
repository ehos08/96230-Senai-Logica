import os 
os.system("clear")
numero1 = float(input ("Digite um número: "))
numero2 = float(input ("Digite um número: "))
soma = (numero1 + numero2)
media = (numero1 + numero2)/2
produto = (numero1 * numero2)

if numero1 > numero2: 
    print (f"\nEsse é o maior número: {numero1}")
else:
    print (f"Esse é o maior número:{numero2}")
print("\nMostrando resultados:")    
print (f"Soma entre os números: {soma}")
print (f"Média entre os números: {media}")
print (f"Produto entre os números: {produto}")