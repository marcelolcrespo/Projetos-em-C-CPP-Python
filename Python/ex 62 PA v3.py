#Melhore o exercício 61 de while para acrescentar mais termos na lista final

lista_pa = []
p = int(input('Digite o primeiro valor: '))
lista_pa.append(p)
raz = int(input('Razão: '))
c = 1
while c < 10:
    p += raz
    lista_pa.append(p)      #Adicionar cada termo da PA em uma lista
    c += 1
    if c == 10:     #Se o contador estiver em 10:
        print(lista_pa)     #printar a lista com termos gerados com 10 primeiros termos
        n = int(input('Mostrar mais quantos valores? '))    #input para acrescentar mais termos
        c -= n      #Vai diminuir o contador em x vezes, obrigando o contador a rodar esse numero de vezes novamente. Ex: input n -> 6, c -= n == 4, entao o contador precisa andar + 6 casas para mostrar os 6 novos termos (input de n)
print(f'Progressão finalizada com {len(lista_pa)} termos mostrados') #Pegar a quantidade de termos gerados


#====Resuloção do professor=====  (While aninhado)

#   print('Gerador de PA')
#   print('-='*10)
#   primeiro = int(input('Primeiro termo: '))
#   razão = int(input('Razão da PA: '))
#   termo = primeiro
#   cont = 1
#   total = 0
#   mais = 10
#   while mais != 0:
#       total = total + mais
#       while cont <= total:
#           print('{} -> '.format(termo), end='')
#           termo += razão
#           cont += 1
#       print('PAUSA')
#       mais = int(input('Quantos termos você quer mostrar a mais? '))
#   print('Progressão finalizada com {} termos mostrados'.format(total))