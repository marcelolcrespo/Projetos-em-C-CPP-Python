#PA com while

c = 1
lista_pa = []
p = int(input('Primeiro termo: '))
lista_pa.append(p)
raz = int(input('Qual a razão: '))

while c < 10:
    p += raz
    lista_pa.append(p)
    c += 1
print(lista_pa)