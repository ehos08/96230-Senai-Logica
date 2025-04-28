import os
os.system("cls||clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa("Proparoxitono", 780, 23.3, 5.87)
pessoa2 = Pessoa("Equilátero", 220, 230.6, 2.59)