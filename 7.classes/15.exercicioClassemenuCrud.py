import os 
from dataclasses import dataclass
os.system ("cls||clear")

@dataclass
class usuario: 
    nome: str
    nascimento: int
    cpf: int
    funcao: str
    def exibir_dados(self):
        print(f"\nNome: {self.nome} \nData de nascimento: {self.nascimento} \nCPF: {self.cpf} \nFunção: {self.funcao}")

