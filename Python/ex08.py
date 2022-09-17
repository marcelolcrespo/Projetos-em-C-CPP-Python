#while e break
import time as delay


contador = 0
while contador < 10:
   print('Ainda nao deu...')
   contador = contador + 1
   delay.sleep(1)
   if contador == 6:
       break
print('Agora deu!!')



