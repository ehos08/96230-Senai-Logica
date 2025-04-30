import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

paciente1 = Paciente(
                     nome = input("Digite seu nome: "), 
                     idade = int(input("Digite sua idade: "))
                     )

paciente1.exibir_dados()