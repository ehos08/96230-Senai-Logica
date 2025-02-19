import os 
os.system ("clear")
    
# Elaborar um algoritmo para solicitar ao usuário um valor
# Se valor lido for > 10, escrever mensagem "é maior que 10"
# Caso contrário, escrever "Não é maior que 10"
valor= int(input("Digite um valor maior que 10: "))
if valor > 10:
   print("valor é maior que 10")
elif valor == 10:
   print("valor é igual a 10")
else: 
   print("valor não é maior que 10") 