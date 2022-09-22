#Faça um programa que recebe um valor {idade} de um jovem e informe:

#Se ele ainda vai se alistar
#Se está no momento de se alistar
#Se já passou do momento de se alistar

        #==Função==#

def receberIdade(a):
    from datetime import date
    ano = date.today().year
    resultado = ano - a #=== var (a) tem o valor do input (idade) como parametro
    alistamento = 18 #idade para alistamento em anos
    if resultado < alistamento:
        print(f'Você tem {resultado} anos. Ainda faltam {alistamento-resultado} anos para você se alistar.')
    elif resultado > alistamento:
        print(f'Você está {resultado - alistamento} anos atrasado!!')
        print(f'Você tem {resultado} anos. Já passou o prazo para você se alistar. \nVá até a junta militar e fique em dia com suas obrigações!!')
    elif resultado == alistamento:
        print(f'Você está no período de alistamento militar. Procure uma junta militar!')
    else:
        print('Ano digitado está inválido')

        #Programa Principal:
idade = int(input('Digite o ano de nascimento: '))
receberIdade(idade)