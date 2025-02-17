import os 
os.system("clear")

idade = 12

if idade < 16:
    print("Acesso negado.")
elif idade < 18:
    print("somente com permissão dos pais")
else:
    print("Acesso permitido") 

print("fim")