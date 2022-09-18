#Faça um programa que tenha uma função maior() que recebe varios parametros com valores inteiros
#Seu programa tem que analisar todos os valores e dizer qual é o maior deles

    #LIB
import time as delay

    #Funções
def maior(*num):
    delay.sleep(0.3)
    print(f'Lista de valores: {num} e o maior valor é: {max(num)}')


    #Programa Principal:
maior(92,73,44,5,36)
maior(32,13,54,45,76)
maior(32,13,24,25,36)
maior(12,53,44,35,26)