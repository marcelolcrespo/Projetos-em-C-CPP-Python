#Escreva um programa, utilizando o for, que leia 6 numeros inteiros e some os pares

import random as sort

pares = []
for c in range(6):
    valor = sort.randint(1, 100)
    if valor % 2 == 0:
        pares.append(valor)
print(f'Lista de valores = {pares}')
pares = sum(pares)
print(f'Soma dos valores gerados: {pares}')