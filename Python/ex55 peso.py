#Faça um programa que leia o peso de 5 pessoas
#No final ele deve mostrar qual foi o maior e o menor peso encontrado
valor = 1
pesoGrupo = []

for c in range(5):
    peso = int(input(f'{valor}º peso: '))
    pesoGrupo.append(peso)
    valor += 1
#print(pesoGrupo)
maxNoGrupo = max(pesoGrupo)
minNoGrupo = min(pesoGrupo)
print(f'Maior peso encontrado no grupo: {maxNoGrupo}')
print(f'Menor peso encontrado no grupo: {minNoGrupo}')