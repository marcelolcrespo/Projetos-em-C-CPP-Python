#Calcular o uso de itens brancos para criar 1 item de raridade especifica

'''
        Evoluir pra raro:
    40k gold
    60x Sucata do tier

        Evoluir pra epico:
    80k gold
    180x Sucata do tier
    54x pó raro do tier

        Evoluir para mitico:
    160k gold
    300x sucatas do tier
    18x pó magico raro do tier
    42x pó epico do tier

        Evoluir para lendário:
    320k gold
    420x sucata do tier
    12x po epico
    32x po mitico

        Evoluir para supremo:
    960k gold
    12x po mitico do tier
    18x po lendário do tier

   === Qualquer item dá 12 sucatas - do tier ===

    - item raro - 9 pó raro + 12 sucata
    - item epico - 6 pó epico + 12 sucata
    - item mitico - 4 pó mitico + 12 sucata
    - item lendário - 2 pó lendário + 12 sucata
'''
import time as delay
#========== Variaveis ===============
sucatas = 12        #Valor em sucatas que um player recebe ao quebrar um equipamento
sucatasQuant = 0
branco = 0
qtitem_branco = 0
qtitem_raro = 0
qtitem_epico = 0
qtitem_mitico = 0
qtitem_lendario = 0

po_raro = 0
po_epico = 0
po_mitico = 0
po_lendario = 0
#======= Var p/ Guardar valores ============
itemRaro = 0
itemEpico = 0
itemMitico = 0
itemLendario = 0
#====== Contadores para o processo ============
sucataUpRaro = 60
sucataUpEpico = 180
sucataUpMitico = 300
sucataUpMitico += sucataUpEpico + sucataUpRaro          #Calcular a qt de sucattas para a melhoria
goldUpRaro = 40
goldUpEpico = 80
goldUpMitico = 160
goldUpMitico = goldUpMitico + goldUpRaro + goldUpEpico  #Calcular o gold para fazer todo o processo
#===== Input's =======
valorRaro = int(input('Quantidade de itens raros:: '))
valorEpico = int(input('Quantidade de itens épicos:: '))
valorMitico = int(input('Quantidade de itens míticos:: '))
valorLendario = int(input('Quantidade de itens lendário:: '))
while True:
    branco += sucatas       #atualizar a var branco para girar o programa
    sucatasQuant += sucatas #contar o total de sucatas utilizadas no processo
    qtitem_branco += 1      #contar quantos itens brancos foram utilizados para gerar o item final
    if po_mitico == 12 and po_lendario == 18:             # Condição para pausar o programa: Criar um item lendário
        print('\tItem Supremo Criado!!!')
        break
    else:
        if branco == 60:            # IF === valor branco = 60 -> add +1 item no count de item raro e remover 60 da var branco
            qtitem_raro += 1            #adiciona +1 item no contador de itens raros
            branco -= sucatas * 5       #remove a quantidade de sucatas do contador para continuar girando
            if qtitem_raro >= 1:            # IF === se tiver 1 item raro no contador:
                po_raro += 9                #po_raro recebe +9 no contador
                itemRaro += qtitem_raro     #Armazena a quantidade de itens na var itemRaro
                qtitem_raro = 0             #Zera a variavel qtitem_raro para receber outro valor
                if po_raro > 54:        # IF ==== se tiver mais de 54 po raro:
                    po_epico += 6                       #somar +6 no pó épico
                    po_raro -= 54                       #remove o valor da var po_raro
                    qtitem_epico += 1                   #adiciona o item epico criado
                    if qtitem_epico >= 1:       # IF === Se tiver 1 item epico no contador:
                        itemEpico += qtitem_epico               #Armazena a quantidade de itens na var itemEpico
                        qtitem_epico = 0                        #Zera a variavel qtitem_epico para receber outro valor
                        if po_epico == 42:              # IF === se tiver mais de 42 po epico:
                            po_mitico += 4                      #=== soma +4 no po mitico
                            po_epico -= 12                      #=== remove a diferença do valor que sobrou para criar um item mitico
                            qtitem_mitico += 1                  #Adiciona o item mitico criado
                            if qtitem_mitico >= 1:      # IF == Se tiver 1 item mitico no contador
                                itemMitico += qtitem_mitico     #Armazena a quantidade de itens na var itemMitico
                                qtitem_mitico = 0               #Zera a variavel qtitem_mitico para receber outro valor
                                if po_mitico > 22 + 10:
                                    po_lendario += 2
                                    po_mitico -= 32
                                    qtitem_lendario += 1
                                    if qtitem_lendario >= 1:
                                        itemLendario += qtitem_lendario
                                        qtitem_lendario = 0

    #print(branco)          #Utilizado para estruturar
    #print(qtitem_branco)   #Utilizado para estruturar
    #delay.sleep(0.2)

if po_raro == 9:        # IF == vale 1 raro -> 60 sucatas -> 5 itens brancos
    po_raro -= 9                #remove 9 po raro da conta final
    qtitem_branco -= 5          #remove 5 itens brancos da calculo final
    itemRaro -= 1               #remove 1 item raro da calculo final
    sucatasQuant -= 60          #remove 60 sucatas da calculo final
if po_epico == 30:       # IF == vale 3 epicos -> 18 itens raros ->  1080 sucatas -> 90 item branco
    qtitem_branco -= 90         #remove 90 itens brancos do calculo final
    po_epico -= 18              #removendo a sobra de po epico
    itemRaro -= 18              #a sobra equivale a 18 itens raros
    sucatasQuant -= 1080        #a sobra equivale a 1080 sucatas
if valorRaro > 0:
    itemRaro -= valorRaro
    sucatasQuant -= valorRaro * 60
    qtitem_branco -= valorRaro * 5
if valorEpico > 0:
    itemEpico -= valorEpico
    sucatasQuant = sucatasQuant - valorEpico * 60
    qtitem_branco -= valorEpico * 30
if valorMitico > 0:
    itemMitico -= valorMitico
    sucatasQuant -= valorMitico * 60
if valorLendario > 0:
    itemLendario -= valorLendario
    sucatasQuant -= valorLendario * 2880
print(f'Sobras de sucatas: {branco}')
print(f'Quantidade de sucatas criadas: {sucatasQuant}')
print(f'Pó raro: {po_raro}')
print(f'Pó épico: {po_epico}')
print(f'Pó mítico: {po_mitico}')
print(f'Pó lendário: {po_lendario}')
print(f'QTitem branco: {qtitem_branco}')
print(f'QTitem raro: {itemRaro}')
print(f'QTitem epico: {itemEpico}')
print(f'QTitem mítico: {itemMitico}')
print(f'QTitem lendario: {itemLendario}\n')
print(f'Gold necessário para todos os Upgrades: xxx k')
print(f'Sucatas necessárias para o processo: {sucataUpMitico}')
print('\n\n')
#delay.sleep(0.2)

