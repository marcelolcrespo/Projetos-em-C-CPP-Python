#Modulos, Bibliotecas e Funções


#

#import math
#num = int(input('Digite um valor: '))
#fatorial = math.factorial(num)
#print(fatorial)

import datetime
from datetime import date #importar uma função dentro do modulo para reduzir o tamanho da função
# ex: datetime.date.today() --> date.today()
dia = datetime.date.today()
print(dia)

dia2 = datetime.date.isoformat(dia) #formatar a data para ficar mais legivel
print(dia2)
