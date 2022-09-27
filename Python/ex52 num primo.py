#Faça um programa que leia um numero inteiro e diga se ele é um numero primo
#ou não

num = int(input("Verificar numeros primos ate: "))
checar = 0

for c in range(2,num):
    if num % c == 0:
        print(f'Múltiplo de {c}')
        checar += 1
if checar == 0:
    print('Numero primo')
else:
    print(f'Tem {checar} múltiplos acima de 2 e abaixo de {num}')