#Escreva um programa que leia um numero inteiro e peça para o usuario escolher qual sera
#a base de conversão: [1]Binário, [2]Octal, [3]Hexadecimal

#Programa feito c/ funções

    #Função:
def recebeNum(a): #=== Recebe o numero
    s = bin(a)
    print('Qual será a base de conversão: \n[1]-Binário\n[2]-Octal\n[3]-Hexadecimal\n')


def converter(a): #=== Conversor de Numero para --> [1]Binário - [2]Octal - [3]Hexadecimal
    conversão = int(input('Digite o número correspondente a sua escolha: '))
    if conversão == 1:
        a = str(bin(a))
        a = a[2:]
        print(a)
    elif conversão == 2:
        a = str(oct(a))
        a = a[2:]
        print(a)
    elif conversão == 3:
        a = str(hex(a))
        a = a[2:]
        print(a)
    else:
        print('Opção inválida!')


    #Programa Principal::
num = int(input('Valor: '))
recebeNum(num)
converter(num)
