import os 
os.system("clear") 

opcao = int(input(""" 
Código\t\t Prato \t\t\t valor
1 \t\t Picanha \t\t R$ 44,90 
2  \t\t Lasanha \t\t R$ 25,38
3 \t\t Strogonoff \t\t R$ 17,60
4 \t\t Bisteca acebolada \t R$ 13,70
5 \t\t Misto \t\t\t R$ 5,00 

\nDigite a opção desejada:                                                                                      
"""))

match opcao:
    case 1:
        print("Sua escolha foi: Picanha, no valor de R$ 44,90.")
    case 2:
        print("Sua escolha foi: Lasanha, no valor de R$ 25,38.")
    case 3:
        print(" Sua escolha foi: Strogonoff, no valor de R$ 17,60.")    
    case 4:
        print("Sua escolha foi: Bisteca acbolada, no valor de R$ 13,70.")
    case 5:
        print("Sua escolha foi: Misto, no valor de R$ 5,00.")