#Crie um programa que mostre todos os pares entre o numero 1 até o numero 50

num = []
for c in range(1, 50):
    if c %2 == 0:
        num.append(c)
print(num, end='')
print(f'\nQuantidade de numeros pares encontrados no range: {len(num)}')