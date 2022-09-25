valor = []
soma = []
for c in range(1, 500):
    valor.append(c)
    if c % 3 == 0:
        soma.append(c)
#print(f'\n{valor}')
print(f'\n\n{soma}')
for i in range(1):
    soma = sum(soma)
print(f'soma: {soma}')