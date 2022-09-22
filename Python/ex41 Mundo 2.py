#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:

#- ate 9 anos: Mirim
#- até 14 anos: Infantil
#- até 19 anos: Junior
#- até 20 anos: Sênior
#- acima: Master

#Função:
def recebe_num(num): #==== Recebe a data de nascimento (ano)
    from datetime import date
    ano = date.today().year
    calculo = ano - num
    if 1 < calculo <= 9:
        print(f'Com {calculo} anos você está na classificação Mirim!')
    elif 9 < calculo <= 14:
        print(f'Com {calculo} anos você está na classificação Infantil!')
    elif 14 < calculo <= 19:
        print(f'Com {calculo} anos você está na classificação Junior!')
    elif 19 < calculo <= 20:
        print(f'Com {calculo} anos você está na classificação Sênior!')
    elif calculo < 20:
        print(f'Com {calculo} anos você está na classificação Master!!')

#Programa Principal:
nascimento = int(input('Digite o ano em que você nasceu: '))
recebe_num(nascimento)