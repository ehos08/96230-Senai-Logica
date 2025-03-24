import os 
os.system("cls||clear")

opcao = int(input(""" 
Código\t\t Prato \t\t\t valor
1 \t\t Picanha \t\t R$ 44,90 
2  \t\t Lasanha \t\t R$ 25,38
3 \t\t Strogonoff \t\t R$ 17,60
4 \t\t Bisteca acebolada \t R$ 13,70
5 \t\t Misto \t\t\t R$ 5,00 

\nDigite a opção desejada:                                                                                      
"""))
laco = (input("Você deseja pedir mais alguma coisa?(Sim ou Não)\n")).lower()
soma = 0.0
while True:
    opcao = int(input(""" 
    Código\t\t Prato \t\t\t valor
    1 \t\t Picanha \t\t R$ 44,90 
    2  \t\t Lasanha \t\t R$ 25,38
    3 \t\t Strogonoff \t\t R$ 17,60
    4 \t\t Bisteca acebolada \t R$ 13,70
    5 \t\t Misto \t\t\t R$ 5,00 

    \nDigite a opção desejada:                                                                                      
    """))
    laco = (input("Você deseja pedir mais alguma coisa?(Sim ou Não)\n")).lower()
    match opcao:
        case 1:
            produto = 44.90
            print(f"Sua escolha foi: Picanha, no valor de R$ 44,90.")
        case 2:
                produto = 25.38
                print (f"Sua escolha foi: Lasanha, no valor de R$ 25,38.")
        case 3:
            produto = 17.60
            print(f"Sua escolha foi: Strogonoff, no valor de R$ 17,60.")    
        case 4:
            produto = 13.70
            print(f"Sua escolha foi: Bisteca acebolada, no valor de R$ 13,70.")
        case 5:
                produto = 5.00
                print(f"Sua escolha foi: Misto, no valor de R$ 5,00.")
        case _:
                print("inválido")
    laco = (input("Você deseja pedir mais alguma coisa?(Sim ou Não)\n")).lower()
    soma += produto 
    if laco == "não":
     break
print(f"O total é {soma}")








