#List Comprehensions

#Lista normal:
lista = [] #============ Usou o 3 linhas para popular a lista
for v in range(10):
    lista.append(v+1)
print(lista)

#lista = []
#for v in 'asdasdaf'    =============== iterar letras na lista
    #lista.append(v)
#print(lista)


    # For dentro de for ===== #Resultado: (1,4);(1,5);(1,6);(2,4)...
#lista = []
#for v in [1,2,3]:
#    for b in [4,5,6]:
#        if v % 2 == 0:
#           lista.append((v,b))


#======================= List Comprehension \/ \/

#lista2 = [ v for in 'asdafasf' ] ========== iterar letras na lista com List Comprehensios
#print(lista2)

#lista2 = [ (v,b) for v in [123] for b in [4,5,6] ] if v % 2 == 0
#print(lista2)

lista2 = [ v+1 for v in range(10)] ## Usou 1 linha para popular a lista
print(lista2)

