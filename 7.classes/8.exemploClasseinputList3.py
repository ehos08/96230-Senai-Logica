import os
from dataclasses import dataclass
os.system("cls || clear")
list_pacientes = []
QUANTIDADE_PACIENTES = 2
@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")
for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(
                        nome = input("Digite seu nome: "), 
                        idade = int(input("Digite sua idade: "))
                       )
    paciente.exibir_dados()

print("\nExibindo dados:")
for paciente in list_pacientes:
   paciente.exibir_dados()