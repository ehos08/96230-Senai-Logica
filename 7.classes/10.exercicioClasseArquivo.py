import os
from dataclasses import dataclass
os.system("cls||clear")
list_livros = []
QUANTIDADE_LIVROS = 3

@dataclass 
class classe_livro:
    nome: str
    autor: str
    categoria: float
    preco: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.autor}\n Categoria:{self.categoria}\n Preço: {self.preco}")

for i in range(QUANTIDADE_LIVROS):

    cadastrado = classe_livro(
                        nome = input("Digite o nome do livro: "), 
                        autor = input("Digite o autor do livro: "),
                        categoria = input("Digite a categoria do livro: "),
                        preco = float(input("Digite o preço do livro: "))
                        
                             )
    list_livros.append(cadastrado)
    
print("Exibindo dados:")
for cadastrado in list_livros:
   cadastrado.exibir_dados()

nome_arquivo = "catalogo_livros.txt"
with open(nome_arquivo, "a") as arquivo_cadastro:
    for cadastrado in list_livros:
        arquivo_cadastro.write(f"{cadastrado.nome}, {cadastrado.autor}, {cadastrado.categoria}, {cadastrado.preco}\n")