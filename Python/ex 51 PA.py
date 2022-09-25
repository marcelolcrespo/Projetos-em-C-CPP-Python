#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
#10 primeiros termos que foram gerados

inicio = int(input('Digite o primeiro termo: '))
fim = inicio + 10
raz = int(input('Razão: '))
'''
inicio == onde vai começar a progressão
fim == vai printar os 10 primeiros termos da sequência
raz = a razão 
'''
for c in range(inicio, fim+1, raz):
    print(c, end=' -> ')
print('Acabou')