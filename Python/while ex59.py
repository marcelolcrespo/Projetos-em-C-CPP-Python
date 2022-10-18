#Crie um programa que leia dois valores e mostre um menu:

#[1]Somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
import time as delay
maior = []
n1 = int(input('Primeiro numero: '))
maior.append(n1)
n2 = int(input('Segundo numero: '))
maior.append(n2)
opc = 0

while opc != 5:
    print('[1]-Somar\n'
          '[2]-Multiplicar\n'
          '[3]-Maior Valor\n'
          '[4]-Novos Valores\n'
          '[5]-Sair do Programa\n'
          )
    opc = int(input('Escolha uma opção:: '))
    if opc == 1:
        soma = n1 + n2
        print(f'Soma dos valores digitados: {soma}')
        delay.sleep(5)
    if opc == 2:
        mult = n1 * n2
        print(f'Multiplicação dos valores digitados: {mult}')
    if opc == 3:
        print(f'Maior valor entre os dois numeros digitados: {max(maior)}')
        delay.sleep(5)
    if opc == 4:
        n1 = int(input('Atualize o primeiro valor: '))
        n2 = int(input('Atualize o segundo valor: '))
        print('\tValores atualizados!!')
        delay.sleep(1)

print('Programa encerrado!')