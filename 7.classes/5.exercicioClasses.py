import os
os.system("cls||clear")

from dataclasses import dataclass

@dataclass
class endereco:
    logradouro: str
    numero: str
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    Endereco: endereco

    def exibir_dados(self):
        print("\nExibindo dados:")
        print(f"""
        Dados:
        pessoa 
         nome: {self.nome}| email: {self.email}| endereço: {self.Endereco.logradouro}, {self.Endereco.numero}, {self.Endereco.cidade}
        """)

nome = input("Digite seu nome: ")
email = input("Digite seu E-mail: ")
logradouro = input("Informe o logradouro de onde você mora: ")
numero = input("Informe o número da sua casa: ")
cidade = input("Informe a cidade onde seu endereço está localizado: ")
endereco1 = endereco(logradouro, numero, cidade)
pessoa = Pessoa(nome, email, endereco1)
pessoa.exibir_dados()