#Aula de funções

#def

def parabens():
    print(' Parabens pra você\n Nessa data querida\n Muitas felicidades\n Muitos anos de vida!!')

def temLetrau():
    frase = input('Digite uma frase: ')
    if 'u' in frase:
        print('Tem letra U')
    else:
        print('Não tem letra U')

def somaQ(a,b):
    somaQ = a**2 + b**2
    return somaQ

somaQ(2,3)