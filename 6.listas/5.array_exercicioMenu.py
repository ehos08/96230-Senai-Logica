import os
os.system("clear")

pedidos = []
soma = 0
while True:
    opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanha \t\t R$ 20,00
3 \t Strognoff \t\t R$ 18,00
4 \t Bife Acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00

Digite a opção desejada: """))
    
    if opcao == 0:
        print(f"\nPedido encerrado. O valor total é R$ {soma:.2f}")
        break
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25.00
        case 2:
            prato = "Lasanha"
            preco = 20.00
        case 3:
            prato = "Strognoff"
            preco = 18.00
        case 4:
            prato = "Bife Acebolado"
            preco = 15.00
        case 5:
            prato = "Pão com ovo"
            preco = 5.00
        case _:
            print("Opção Inválida")
            preco = 0

    soma += preco
    pedidos.append(prato, preco)
    print(f"Sua escolha foi: {prato}, no valor de R$ {preco:.2f}.\n\t")
    continuar = input("Deseja informar outro prato? (S/N): ").lower()

    if continuar == 'n':
        break

for prato, preco in pedidos:
    print(f"- {prato}: R$ {preco:.2f}")
print(f"\nTotal a pagar: R$ {soma:.2f}")