#def soma(a, b):
#    print(f'O A = {a} e o B = {b}')
#    s = a + b
#    print(f'A soma de a + b = {s}')

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='') #=== Quebrar o valor apenas ao final do siclo for
    print('Fim!')


def contador2(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1



#Programa Principal:
#soma(b=4, a=5)

contador(1, 2, 3, 4, 5)
contador(1,2,3,4,5,6,7,8,9,9)

contador2(2,3,4,5)
contador2(1,2,6,5,7)

valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)



