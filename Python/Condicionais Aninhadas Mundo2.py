
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
#o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
#será negado.

#if - elif - else (condicionais aninhadas)

    #Programa Principal:
entrada = 0
salario = int(input('Digite o salário mensal: '))
casa = int(input('Valor da casa: '))
pergunta_entrada = str(input('Incluir valor de entrada? Digite: [s] ou [n]:: '))
tempo = int(input('Em quanto tempo o(a) senhor(a) pretende pagar a dívida: '))

tempo = tempo * 12
checarSalario = (salario * 30/100)
prestação = casa / tempo

if pergunta_entrada == 's':
    entrada = int(input('\nQual será o valor de ENTRADA: '))
prestação_com_entrada = (casa - entrada)/tempo

if pergunta_entrada == 's':
    if checarSalario < prestação_com_entrada:
        print(f'\nO valor da prestação é: R${prestação_com_entrada.__ceil__()},00 reais, e excede 30% do seu salário, que é: R${salario},00. \
        \nPortanto, o financiamento foi NEGADO.')
    else:
        print(f'\nVocê foi aprovado para o financiamento!\
        \nVocê escolheu pagar R${prestação_com_entrada.__ceil__()},00 em {int(tempo)} meses ({int(tempo/12)}) anos.')
else:
    if checarSalario < prestação:
        print(f'\nO valor da prestação é: R${prestação.__ceil__()},00 reais mensais, e excede 30% do seu salário, que é: R${salario},00. \
        \nPortanto, o financiamento foi NEGADO.')
    else:
        print(f'\nVocê foi aprovado para o financiamento!\
        \nVocê escolheu pagar R${prestação.__ceil__()},00 em {int(tempo)} meses ({int(tempo/12)}) anos.')


