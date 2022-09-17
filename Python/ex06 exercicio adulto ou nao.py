#Perguntar ao usuario o ano que ele nasceu
#checar se ele é adulto ou não

idade = int(input('Digite o ano em que você nasceu: '))
ano = 2022
checar = ano - idade

if checar >= 18:
    print('Adulto')
else:
    print('Menor de idade')