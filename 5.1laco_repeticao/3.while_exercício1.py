import os
os.system("clear")


while True:   
   nota = int(input("Digite sua nota: "))
   if nota < 0 or nota > 10 :
      print(f"Informe sua nota corretamente, {nota} é um número inválido")
   else:
     break
   