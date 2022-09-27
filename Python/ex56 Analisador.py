#Desenvolva um programa que recebe:
# nome | idade | sexo -- 4 pessoas
#Mostrar a media de idade do grupo | Qual é o nome do homem mais velho | Quantas mulheres
#com menos de 20 anos

valor = 1           # contador personalizado
idadeLista = []     # lista com todas as idades
nomeLista = []      # lista de nomes
nomeHMaisVelho = '' # string vazia para receber o nome do Homem mais velho
soma = 0            #var para fazer o calculo da média de idades
sexoCount = 0       #contar quantas mulheres tem na lista
idadeFCount = 0     #contar a quantidade de mulheres com menos de 20 anos
maiorIdade = 0      #recebe a idade do homem mais velho

for c in range(4):
    print(f'--- {valor}º PESSOA ---')
    nome = str(input('Nome:: ')).title()
    nomeLista.append(nome)
    idade = int(input('Idade:: ')).__int__()
    idadeLista.append(idade)
    sexo = str(input('[M/F]:: ')).upper()
    valor += 1
    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeHMaisVelho = nome
    if sexo == 'F':
        sexoCount += 1
        if idade <= 20:
            idadeFCount += 1

soma = sum(idadeLista) / len(idadeLista)        #== Média das idades

print(f'Media das idades do grupo: {soma}')
print(f'Encontradas na lista: {sexoCount} mulheres e {idadeFCount} menores de 20 anos')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {nomeHMaisVelho}')