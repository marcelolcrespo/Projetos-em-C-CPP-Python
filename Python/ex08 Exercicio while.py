#Programa vai receber um valor e calcular o fatorial
import time as delay

num = int(input('Digite um valor a ser calculado: '))
fatorial = num
contador = 1
while (num-contador)>1:
    fatorial = fatorial * (num - contador)
    contador += 1
    delay.sleep(1)
print('{0}! = {1}'.format(num, fatorial))
