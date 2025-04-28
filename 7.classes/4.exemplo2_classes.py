import os 
os.system("cls||clear")
from dataclasses import dataclass
@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: int
    def exibir_dados(self):
        print("\nExibindo dados:")
        print(f"""
        Dados:
        pessoa 1
          nome: {self.nome}, email: {self.email}, telefone: {self.telefone}, endereço: {self.endereco}
        pessoa 2
          nome: {self.nome}, email: {self.email}, telefone: {self.telefone}, endereço: {self.endereco}
""")
nome = input("Digite seu nome: ")
email = input("Digite seu E-mail: ")
telefone = input("Informe seu telefone:")
endereco = input("Informe sua endereço: ")

pessoas= Pessoa(nome, email, telefone, endereco)
pessoas.exibir_dados()