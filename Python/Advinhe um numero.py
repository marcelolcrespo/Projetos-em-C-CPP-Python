import random as sort

valor = sort.randint(1,10)
acerto = 0
chute = 0
#print(valor)
while valor != acerto:
    chute = int (input ('Digite um valor entre 1 ~ 10: '))
    if valor == chute:
        print('Acertou!')
        break
    else:
        print('Errou!')