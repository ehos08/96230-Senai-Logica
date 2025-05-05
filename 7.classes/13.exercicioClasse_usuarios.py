import os
from dataclasses import dataclass
os.system("cls||clear")

usuarios = []
QUANTIDADE_USUARIOS = 5

@dataclass 
class usuario:
    nome: str
    nascimento: str
    RG: int
    CPF: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.nascimento}\n RG: {self.RG}\n Preço: {self.CPF}")

for i in range(QUANTIDADE_USUARIOS):

    cadastrado = usuario(
                        nome = input("Digite seu nome: "), 
                        nascimento = input("Digite a sua data de nascimento (DDMMAAAA): "),
                        RG = input("Digite o seu RG: "),
                        CPF = float(input("Digite o seu CPF: "))
                        
                             )
    usuarios.append(cadastrado)
    

nome_arquivo = "Usuários.txt"
with open(nome_arquivo, "a") as arquivo_cadastro:
    for cadastrado in usuarios:
        arquivo_cadastro.write(f"{cadastrado.nome}, {cadastrado.nascimento}, {cadastrado.RG}, {cadastrado.CPF}\n")
try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileExistsError:
    print("Arquivo não encontrado.")
