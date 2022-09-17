#Faça um programa que tenha uma função chamada área(), que receba as dimensões
#de um terreno retangular (largura e comprimento) e mostre a area do terreno.

def area(a, b):
    s = a * b
    print(f'A area de um terreno com {a}m de largura e {b}m de comprimento é: {s}m²')




#Programa Principal:
lar = int(input('Digite a largura: '))
comp = int(input('Digite o comprimento: '))
area(lar, comp)
