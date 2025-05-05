import os
os.system ("cls||clear")
from dataclasses import dataclass

@dataclass
class autor:
    nome: str
    biografia: str

class livro:
    titulo: str
    ano: int
    autor_livro = autor
    def preencher_dados(self):
        nome_autor = input("Informe o nome do autor: ")
        biografia_autor = input("Informe a biografia do autor: ")
        self.autor_livro = autor(nome=nome_autor, biografia=biografia_autor)
        self.titulo = input("Informe o título do livro: ")
        self.ano = int(input("Informe o ano de publicação do livro: "))
    def exibir_dados(self):
        print(f"Livro: {self.titulo}\nAno: {self.ano}\nAutor: {self.autor_livro.nome}\nBiografia: {self.autor_livro.biografia}")

livro = livro()
livro.preencher_dados()
livro.exibir_dados()


 

