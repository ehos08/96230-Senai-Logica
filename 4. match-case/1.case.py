import os 
os.system("clear")

dia = input("Digite o dia da semana: ")

match dia:
    case "segunda":
     print("hoje é Segunda-feira.")
    case "terça":
     print("hoje é Terça-feira.")
    case "quarta":
     print("hoje é Quarta-feira.")
    case "quinta":
     print("hoje é Quinta-feira.")
    case "sexta":
     print("hoje é Sexta-feira.")
    case "sábado" :
     print("hoje é Sábado.")
    case "domingo":
     print("hoje é Domingo.")
    case _:
     print("Dia inválido")

     print(dia)
     print("===FIM===")
