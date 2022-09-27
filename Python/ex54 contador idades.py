#Crie um programa que leia o ano de nascimento de 7 pessoas
#mostre quantas pessoas são maiores de idade e quantas não são

from datetime import date

ano = date.today().year
grupoMaior = []     #Poderia ser um contador simples 'grupoMaior = 0' e somar +1 a cada valor encontrado
grupoMenor = []     #Poderia ser um contador simples
valor = 1
#idade = int(input('Valor: '))
for c in range(7):
    idade = int (input (f'Ano de nascimento da {valor}º pessoa: '))
    if ano - idade >= 21:
        grupoMaior.append(idade)
    else:
        grupoMenor.append(idade)
    valor += 1
print(f'Foram encontrados {len (grupoMaior)} pessoas maiores de idade')
print(f'Foram encontrados {len(grupoMenor)} pessoas menores de idade')
