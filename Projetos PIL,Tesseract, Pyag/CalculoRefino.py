import time, sys

#Globais:
atk = 0
raridade = 0
resultado = 0


#===================================================================================
#============================== #Funções: ==========================================
#====================== Recebendo valores ==========================================
def recebeValores(a, b):
    global atk, raridade
    atk = int(input('Ataque do item: '))
    raridade = int(input('Ataque do item c/ raridade: '))


#===================================================================================
#====================== Calcular o bonus de raridade ===============================
def bonus_de_raridade(a, b):
    global atk, raridade, resultado
    resultado = ((raridade - atk) / atk) * 100
    if 2 <= resultado <= 4:
        print('Porcentagem bonus: {:.2f}%'.format(resultado))
        print('Item Raro!')
    elif 4.2 <= resultado <= 7.1:
        print('Porcentagem bonus: {:.2f}%'.format(resultado))
        print('Item Épico!')
    elif 7.2 <= resultado <= 11.1:
        print('Porcentagem bonus: {:.2f}%'.format(resultado))
        print('Item Mítico!')
    elif 11.3 <= resultado <= 15:
        print('Porcentagem bonus: {:.2f}%'.format(resultado))
        print('Item Lendário!')
    elif 15.05 <= resultado <= 20:
        print('Porcentagem bonus: {:.2f}%'.format(resultado))
        print('Item Supremo!')


#===================================================================================
#====================== Calcular refino ============================================
def calculo_refino(a, b):
    global atk, raridade
    pos = 1
    refino = 11
    calculo = 0
    for i in range(refino):             #==== Range de refino (Refino novo vai até +11)
        calculo = (raridade * 5) / 100  #==== var Calculo recebe o dano (valor de raridade) e soma 5% por refino
        raridade = calculo.__ceil__() + raridade  #Atualizando o valor da arma, arredondando pra cima a var calculo
        print(f'Refino +{pos} -> \t{raridade}') #Print formatado do refino com contador personalizado
        pos += 1        #Contador de refinos


#===================================================================================
#================= Menu de opções c/ chamada de outras funções =====================
def menu_opções():
    while True:
        print("\t==[1]== Para saber o dano do item refinado (+1 ~ +11).")
        print("\t==[2]== Para saber a porcentagem do seu item.")
        rodar = 0
        escolha = int(input(':: '))
        if escolha == 1:
            recebeValores(atk, raridade)
            calculo_refino(atk, raridade)
        elif escolha == 2:
            recebeValores(atk, raridade)
            bonus_de_raridade(atk, raridade)
        else:
            print('Opção inválida!!')
        print('\nPara pausar o programa digite [1] == Para continuar, digite qualquer outro valor inteiro.')
        rodar = int(input(''))
        if rodar == 1:
            break
        else:
            #delay()
            print('\n')
            continue

#===================================================================================
#================================ Tela QTV:: =======================================


#===================================================================================
#========================== Programa Principal:: ===================================

menu_opções()

