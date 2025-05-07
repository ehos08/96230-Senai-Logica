import os 
from dataclasses import dataclass
os.system("cls||clear")
funcionarios = []
clientes = []
QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3

@dataclass 
class funcionario:
    nome: str
    admissao: int
    matricula: int
    endereco: str
    def exibir_dadosF(self):
        print(f"\nNome: {self.nome} \nData de admissão: {self.admissao}\n Número de matrícula: {self.matricula}\n Endereço: {self.endereco}")
class cliente:
    nome: str
    nascimento: str
    endereco: str
    def exibir_dadosC(self):
        print(f"\nNome: {self.nome} \nData de nascimento: {self.nascimento}\n Endereço: {self.endereco}")

opcao = input("Informe se deseja cadastrar funcionários ou  clientes (F/C): ").lower()
match opcao:
    case "f":
        for i in range(QUANTIDADE_FUNCIONARIOS):

            cadastrado = funcionario(
                                nome = input("Digite seu nome: "), 
                                admissao = int(input("Digite a sua data de admissão (DD/MM/AAAA): ")),
                                matricula = int(input("Digite o número de matrícula: ")),
                                endereco = input("Digite o seu endereco: ")
                                )
            funcionarios.append(cadastrado)
        print("\nExibindo dados dos funcionários:")
        for cadastrado in funcionarios :
         cadastrado.exibir_dadosF()
        nome_arquivo = "funcionarios.txt"
        with open(nome_arquivo, "a") as arquivo_cadastro:
            for cadastrado in funcionarios:
                arquivo_cadastro.write(f"\n{cadastrado.nome}, {cadastrado.admissao}, {cadastrado.endereco}, {cadastrado.matricula}\n")
    case "c":
        for i in range(QUANTIDADE_CLIENTES):

            cadastrado = cliente(
                                nome = input("Digite seu nome: "), 
                                nascimento = input("Digite a sua data de nascimento (DD/MM/AAAA): "),
                                endereco = input("Digite o seu endereco: ")
                                )
            clientes.append(cadastrado)
            print("\nExibindo dados dos clientes:")
        for cadastrado in clientes :
         cadastrado.exibir_dadosC()
        nome_arquivo = "clientes.txt"
        with open(nome_arquivo, "a") as arquivo_cadastro:
            for cadastrado in clientes:
                arquivo_cadastro.write(f"\n{cadastrado.nome}, {cadastrado.nascimento}, {cadastrado.endereco}\n")
    case"_":
        print("Informe apenas dados válidos.")