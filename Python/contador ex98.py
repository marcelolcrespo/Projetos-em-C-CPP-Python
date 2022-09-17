#Faça um programa que tenha uma função() que recebe três parametros: inicio, fim, passo e realiza uma contagem
#Seu programa precisa realizar três contagens a partir da função criada:

#a) De 1 até 10 indo de 1 em 1
#b) De 10 até 0, de 2 em 2
#c) uma contagem personalizada
import time as delay

# a -> Valor Inicial
# b -> Valor Final
# c -> Passos para caminhar até o range

def contador(a,b,c):
    if a == 1 and c == 1:    #==== Condicional para função com parametro range(1, 10, e pulando 1 casa)
        while a < b+1:
            print(f'{a} ', end='')
            a += c
        print('\n')
    elif a == 10 and c == 2: #=== Condicional para função c/ parametro range(10, 0, pulando 2 em 2)
        while b <= a+1:
            print(f'{a} ', end='')
            a -= c
    else:  #======================== Caso seja uma função personalizada:
        if c == 0:      #==== Passo Digitado = 0: Somar +1 até o range final
            for i in range(a, b):
                if a <= b:
                    print(f'{a} ', end='')
                    a += 1
        else:    #=========== Se o numero de passos (c) for diferente de 0:
            if a <= b: #=== valor Inicial menor que o valor Final: Somar cada passo com C (Input passos)
                while a <= b:
                    print(f'{a} ', end='')
                    a += c
            elif a >= b: #=== Valor Inicial maior que Final: Subtrair cada passo de c (Input passos)
                while a >= b:
                    print (f'{a} ', end='')
                    a -= c


    #Programa Principal:

#C/ Parametro
contador(1, 10, 1)
contador(10, 1, 2)

#Personalizado:
a = int(input('\nValor inicial: '))
b = int(input('\nValor final: '))
c = int(input('\nPassos: '))
contador(a, b, c)