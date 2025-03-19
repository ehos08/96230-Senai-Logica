import os
os.system("clear")
import getpass
EMAIL = "enzo"
senha = "12345"

while True:
    for i in range (3):
        EMAIL = input("Digite seu email: ")
        senha = getpass.getpass("Digite sua senha: ")
        if EMAIL != "enzo" and senha != "12345":
         print("Acesso negado.")
        else:
         break
print("programa encerrado.")