#Faça um programa que mostre na tela uma contagem regressiva e
# conte de 10 ate 0 com uma pausa de 10s

import time

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)