#faça um programa que calcule a soma de todos os numeros impares que são multiplis de três
#e que se encontram no intervalo de 1 a 500

impar = []
soma = []
for c in range(1, 500):
    if c % 3 == 0:
        impar.append(c)  #=== adicionar valores na lista impar
print(impar, end='')
print(f'\nQuantidade de impares no range de 1 a 500: {len(impar)}') #== printar o tamanho da lista impar

soma = sum(impar) #=== Somar os valores da lista soma
print(f'Soma dos valores encontrados = {soma}', end='')
