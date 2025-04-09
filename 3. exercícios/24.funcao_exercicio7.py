import os 
os.system("cls||clear")

def inflacao(preco):
    if preco >= 100:
        preco = preco * 1.2
    else:
        preco = preco * 1.1
    return preco
def deflacao(preco):
    if preco >= 100:
        preco = preco * 0.2
    else:
        preco = preco * 0.1
    return preco
produto = float(input("Informe o preço do produto: \t\n"))
inflacaoF = inflacao(produto)
print(f"O preço do produto com a inflação é de R${inflacaoF:.2f}\t\n")
deflacaoF = deflacao(produto)
print(f"O preço do produto com a deflação é de R${deflacaoF:.2f}")