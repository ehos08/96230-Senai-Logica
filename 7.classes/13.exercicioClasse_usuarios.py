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
                        nome = input(f"Digite o {i+1}º nome: "), 
                        nascimento = input(f"Digite a {i+1}ºdata de nascimento (DD/MM/AAAA): "),
                        RG = input(f"Digite o {i+1}º RG: "),
                        CPF = float(input(f"Digite o {i+1}º CPF: "))
                             )
    usuarios.append(cadastrado)
    
#salvando arquivo em .txt
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
#==================================================================================================================