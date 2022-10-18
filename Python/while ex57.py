#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F"
#Caso esteja errado, peça a digitação novamente até ter um valor correto


sex = str(input('Qual seu sexo? [M/F]:: ')).upper()
while sex != 'M' and sex != 'F':
    sex = str(input('Dados inválidos. Digite seu sexo: ')).upper()
print(f'Sexo {sex} registrado com sucesso!')
print('Fim')