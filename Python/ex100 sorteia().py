#Faça um programa que tenha uma lista chamada numeros e duas funções chamadas:
#sorteia() & somaPar()
#A primeira função vai sortear 5 numeros e vai colocá-los dentro de uma lista e a segunda função
#vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

import random as sort

    #Funções:
def sorteia(lista):   #Sorteia um valor aleatorio. // Lista parametro para espelhar a lista do programa principal
    pos = 0
    for i in lista:     #Loop da lista para percorrer e sortear um valor aleatorio em cada posição
        lista[pos] = sort.randint(1, 100) #função que sorteia um valor aleatório em cada posição da lista
        pos += 1
    print(f'Valores gerados aleatoriamente: {lista}')

def somaPar(lista):  #Somar os valores PARES da lista // A lista de parametro espelha a lista do programa principal
    pos = 0     #=== Contador
    soma = 0    #=== Var que recebe e soma todos os valores PARES
    while pos < len(lista):  #=== Loop para correr toda a lista c/ condicional para identificar os PARES
        #print(f'numero par {lista[pos]%2==0}')
        if lista[pos]%2==0:     #=== Condicional para idenfiticar os PARES
            soma += lista[pos]  #=== Somar os valores PARES
        pos += 1
    print(f'Soma dos valores PARES: {soma}')


    #Programa Principal:
numero = [1, 2, 3, 4, 5]
sorteia(numero)
somaPar(numero)