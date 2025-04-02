import os 

def logo():#função sem retorno
 os.system("cls||clear")
 print("========")

logo() #chamando a função
nome = input("Digite seu nome: ")

logo() #chamando a função
idade = input("Digite sua idade: ")

logo() #chamando a função
print(f"Nome: {nome}")
print(f"Idade: {idade}")

#===============================================
import os 
os.system("cls||clear")

print("========")
nome = input("Digite seu nome: ")
os.system("cls||clear")
print("========")
idade = input("Digite sua idade: ")
os.system("cls||clear")
print("========")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
