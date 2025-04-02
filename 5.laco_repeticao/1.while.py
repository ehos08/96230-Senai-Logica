import os 
os.system("cls|| clear")

contador = 0
continua = "s"

while continua == "s":
    print("Repetindo...")
    contador += 1
    continua = input("Tecle 's' se deseja continuar.\n").strip().lower()
if contador == 0:
    print("O bloco NÃO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes.")
    
#JEITO ALTERNATIVO:  
contador = 0 
while True:
    print("Repetindo...")
    contador += 1
    continua = input("Tecle 's' se deseja continuar.\n").strip().lower()
    if contador == 0:
     print("O bloco NÃO foi repetido.")

    if contador == 3:
    