import os
import time
os.system ("cls")

print("Os números ímpares entre 1 e 20 são: ")

for i in range(1, 21, 1):
    if i % 2 !=0:
     print(i)
    time.sleep(1)
