import os
from dataclasses import dataclass
os.system("cls || clear")
list_pacientes = []
QUANTIDADE_USUARIOS = 2

@dataclass
class cadastro:
    nome: str
    idade: int
    peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n Peso:{self.peso}\n Altura: {self.altura}")

for i in range(QUANTIDADE_USUARIOS):


    cadastrado = cadastro(
                        nome = input("Digite seu nome: "), 
                        idade = int(input("Digite sua idade: ")),
                        peso = float(input("Digite seu peso: ")),
                        altura = float(input("Digite sua altura: "))
                        
                     )
    list_pacientes.append(cadastrado)
    
print("Exibindo dados:")
for cadastrado in list_pacientes:
   cadastrado.exibir_dados()

#salvando em .txt
nome_arquivo = "dados usuário.txt"
with open(nome_arquivo, "a") as arquivo_cadastro:
    for cadastrado in list_pacientes:
        arquivo_cadastro.write(f"{cadastro.nome}, {cadastro.idade}, {cadastro.peso}, {cadastro.altura}")