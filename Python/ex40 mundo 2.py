#Crie um programa que receba 4 notas de um aluno e calcule a media
#Se media for menor que 5 == Reprovado
#Se media for entre 5 e 6.9 == Recuperação
#Se media for maior que 7 == Aprovado

    #Função:
def receber_valor(lista): #=== Receber os valores das notas em listas
    pos = 0
    for i in lista:
        lista[pos] = int(input('Digite um valor: '))
        pos += 1
def calculo(lista): #=== Calculo da média + Condicionais
    pos = 0
    media = 0
    for i in lista:
        media += lista[pos]
        pos += 1
    media = media / 4

        #===Condicionais:
    if media < 5:
        print(f'Reprovado. Nota: {media}')
    elif 5 <= media <= 6.9:
        print(f'Recuperação! Nota: {media}')
    elif media >= 7:
        print(f'Aprovado! Nota: {media}')


#Programa Principal:
nota = [1, 2, 3, 4]
receber_valor(nota)
calculo(nota)