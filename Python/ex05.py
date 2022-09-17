#format

#fruta = 'Laranja'
#a = 1

#print('Suco de %s é o meu favorito' %fruta) #format 1 // # %s é uma var tipo string

# %d - decimal
# %f - valor flutuante
# %s - string

#print('Suco de {} é o meu favorito nº{}!!'.format(fruta, a))
#Outro format

#cor = 'azul'
#cor2 = 'rosa'

#print('O céu é {0}, a flor é {1} e meu carro é {0}'.format(cor, cor2))
#o numero 0 indica o indice para saber qual var vai usar.
# ex: 0 é a cor azul e eu quero utilizar no inicio e no fim, então vou indicar o indice da cor.
# caso não especificado, o comando pediria 3 variaveis sequenciadas

conta = 17/3
print(conta)

print('O resultado da conta é: {:.2f}'.format(conta)) # para ficar apenas 2 casas depois da virgula

#forma mais simplificada:
a = 5
print(f'texto{a = }') #vai imprimir 'texto a = 5'