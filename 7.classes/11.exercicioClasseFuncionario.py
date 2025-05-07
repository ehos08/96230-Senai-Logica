import os
from dataclasses import dataclass
os.system("cls||clear")

funcionarios = []
QUANTIDADE_FUNCIONARIOS = 5

@dataclass 
class funcionario:
    nome: str
    nascimento: str
    RG: int
    CPF: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.nascimento}\n RG: {self.RG}\n Preço: {self.CPF}")

for i in range(QUANTIDADE_FUNCIONARIOS):

    cadastrado = funcionario(
                        nome = input("Digite seu nome: "), 
                        nascimento = input("Digite a sua data de nascimento (DDMMAAAA): "),
                        RG = input("Digite o seu RG: "),
                        CPF = float(input("Digite o seu CPF: "))
                        
                             )
    funcionarios.append(cadastrado)
    
print("Exibindo dados:")
for cadastrado in funcionarios :
   cadastrado.exibir_dados()

nome_arquivo = "Funcionários.txt"
with open(nome_arquivo, "a") as arquivo_cadastro:
    for cadastrado in funcionarios:
        arquivo_cadastro.write(f"{cadastrado.nome}, {cadastrado.nascimento}, {cadastrado.RG}, {cadastrado.CPF}\n")
    
    