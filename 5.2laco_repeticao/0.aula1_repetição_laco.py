import os 
os.system("cls")

print("SOLICITANDO OS NÚMEROS")
numero =  int(input(f"Digite o número que você deseja saber a tabuada: "))
for i in range (11):
   print(f"{numero} x {i} = {numero * i}")
    