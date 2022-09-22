#Escreva um programa que leia 2 numeros inteiros e compare-os mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Os valores sao igual

#Função:
def compararValores(a, b):
    if a > b:
        print(f'O primeiro valor: {a} é maior que o segundo valor: {b}')
    elif b > a:
        print(f'O segundo valor: {b} é maior que o primeiro valor: {a}')
    elif a == b:
        print(f'Os valores {a} e {b} são iguais')
    else:
        print('Algum valor está inválido!')


#Programa Principal:
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

compararValores(valor1, valor2)
