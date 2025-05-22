import os
os.system("clear")

EMAIL = "enzo"
SENHA = "12345"
contador = 0
while True:
        EMAIL = input("Digite seu email: ")
        SENHA = input("Digite sua senha: ")
        if EMAIL == "enzo" and SENHA == "12345":
         print("Acesso concedido.")
         break
        else:
         print("Acesso negado.\n")
         contador += 1
        if contador == 3:
           print("Limite de tentativas excedido")
        break
