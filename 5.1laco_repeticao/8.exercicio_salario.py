import os
import time
os.system("cls||clear")

salario = 0
salario_f = 0
total_pessoas = 0
soma_salario = 0
quantidade_f = 0
idade_maior = 0
idade_menor = 200

while True:
    print("""
        Código | Descrição  
        1    | Adicionar pessoa
        2    | Exibir resultado
        3    | Sair                        
    \t""")
    menu = int(input("Informe o que deseja: "))
    match menu:
        case 1:
            idade = int(input("\nDigite a idade para cadastro: "))
            sexo = input("Digite o sexo para novo cadastro(M/F): ").lower()
            salario = float(input("Informe seu salário para novo cadastro: "))
           
            if sexo == "f" and salario >= 5000:
                quantidade_f += 1
                salario = float(input("Digite o salário para novo cadastro: "))
                total_pessoas += 1
                soma_salario += salario
            if idade > idade_maior:
                    idade_maior = idade
            if idade < idade_menor:
                    idade_menor = idade
            print("Cadastrando usuário...")
            time.sleep(2)
            print("Usuário cadastrado.")
            time.sleep(1)
            os.system("clear")    
        case 2:
                if total_pessoas > 0:
                 print(f"\nMédia salarial do grupo: R$ {soma_salario / total_pessoas:.3f}")
                 print(f"Maior idade do grupo: {idade_maior}")
                 print(f"Menor idade do grupo: {idade_menor}")
                 print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_f}")
                else:
                      print("\nCadastre uma pessoa primeiro.")  
                time.sleep(2)    
                os.system("clear")
        case 3: 
                print("Encerrando programa...") 
                time.sleep(3)
                print("programa encerrado.")
                break
          