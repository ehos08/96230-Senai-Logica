import os
import time
os.system("cls || clear")

def verificar_lista_vazia(list_funcionario):
    if not list_funcionario:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar_funcionario(list_funcionario):
    nome = input("Digite o nome que deseja adicionar: ")
    nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF: ")
    funcao = input("Digite a função: ")
    funcionario = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "funcao": funcao
    }
    list_funcionario.append(funcionario)
    print(f"\n{nome} adicionado com sucesso.")

def mostrar_funcionarios(list_funcionario):
    if verificar_lista_vazia(list_funcionario):
        return

    print("\n - Lista de funcionários - ")
    for i, funcionario in enumerate(list_funcionario, start=1):
        print(f"{i}. Nome: {funcionario['nome']}, Nascimento: {funcionario['nascimento']}, CPF: {funcionario['cpf']}, Função: {funcionario['funcao']}")

def atualizar_funcionario(list_funcionario):
    if verificar_lista_vazia(list_funcionario):
        return

    mostrar_funcionarios(list_funcionario)
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")
    for funcionario in list_funcionario:
        if funcionario["nome"] == nome_antigo:
            funcionario["nome"] = input(f"Digite o novo nome para {nome_antigo}: ").lower() or funcionario["nome"]
            funcionario["nascimento"] = input("Digite a nova data de nascimento (DD/MM/AAAA): ") or funcionario["nascimento"]
            funcionario["cpf"] = input("Digite o novo CPF: ")or funcionario["cpf"]
            funcionario["funcao"] = input("Digite a nova função: ").lower() or funcionario["funcao"]
            print(f"\n{nome_antigo} foi atualizado com sucesso.")
            return
    print(f"\nO funcionário {nome_antigo} não foi encontrado.")

def excluir_funcionario(list_funcionario):
    if verificar_lista_vazia(list_funcionario):
        return

    mostrar_funcionarios(list_funcionario)
    nome_remover = input("Digite o nome do funcionário que deseja remover: ")
    for funcionario in list_funcionario:
        if funcionario["nome"] == nome_remover:
            list_funcionario.remove(funcionario)
            print(f"\n{nome_remover} foi removido com sucesso.")
            return
    print(f"\nO funcionário {nome_remover} não foi encontrado.")

funcionarios = []
while True:
    print("""
    - Gerenciador de Funcionários -
    1 - Adicionar
    2 - Listar funcionários
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_funcionario(funcionarios)
        case 2:
            mostrar_funcionarios(funcionarios)
        case 3:
            atualizar_funcionario(funcionarios)
        case 4:
            excluir_funcionario(funcionarios)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente...")
            time.sleep(3)
            os.system("cls||clear")
    if opcao != 1:
        time.sleep(2)
    os.system("cls || clear")