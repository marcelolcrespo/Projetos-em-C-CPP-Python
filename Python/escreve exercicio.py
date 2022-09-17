#Faça um programa que tenha uma função escreva() que recebe um texto qualquer como
#parametro e mostre uma mensagem com tamanho adaptavel.

def escreva(txt):
    tam = len(txt)
    print('-'*tam)
    print(txt)
    print('-'*tam)


#Programa Principal:
escreva('OI')