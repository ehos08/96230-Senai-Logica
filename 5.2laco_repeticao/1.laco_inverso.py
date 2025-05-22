import os 
os.system ("cls")
import time
print("contagem regresiva!")
numero = int(input("configure o cronômetro da bomba: "))
for i in range(numero, 0, -1):
 print(f"Segundos até a explosão: {i}")
 time.sleep(1)

print("BOOM")