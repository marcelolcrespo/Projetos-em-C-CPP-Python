#Melhorar o game da advinhação:
#O computador deve pensar em um número entre 0 e 10 e o jogador deve tentar advinhar até acertar
#O programa deve mostrar:
    #Numero de palpites utilizados para vencer o game

import random as sort

maquina = sort.randint(0, 10)
jogador = int(input('Digite um valor: '))   #1º input fora do while
tentativa = 1       #Tentativa começa em 1 pois o primeiro input é feito fora do while
while maquina != jogador:
    jogador = int(input('Errou! Digite outro valor: '))
    tentativa += 1
print(f'Numero de tentativas {tentativa}')
print('Acabou!')