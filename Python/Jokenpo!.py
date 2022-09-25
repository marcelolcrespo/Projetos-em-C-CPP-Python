#Fazer um game "Pedra - Papel - Tesoura":


#Funções::
#============================== Display ======================================
def display():
    import random as sort, time
    while True:
        print('\n|[1]-- Pedra\t|\n'
              '|[2]-- Papel\t|\n'
              '|[3]-- Tesoura\t|\n'
              '')
        a = int(input(':: '))
        range = 3
        jogador = a
        maquina = sort.randint(1, range)

        if jogador >= 4 or jogador < 1:
            print('\tValor inválido!\n')
        else:
            contagemTimer()
            if maquina == jogador:         #=== EMPATE [Jogador == Maquina]
                print(f'Maquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tEmpate!!')
                time.sleep(5)
            #=================================================================
            elif maquina == 1 and jogador == 3:         #=== Maquina Win [PedraxTesoura]
                print(f'\nMaquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tMaquina venceu!!\n')
                time.sleep(5)
            elif jogador == 1 and maquina == 3:         #=== Jogador Win [PedraxTesoura]
                print(f'Maquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tJogador venceu!!\n')
                time.sleep(5)
            #=================================================================
            elif jogador == 1 and maquina == 2:         #=== Maquina Win [PedraxPapel]
                print(f'Maquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tMaquina venceu!!\n')
                time.sleep(5)
            elif maquina == 1 and jogador == 2:         #=== Jogador Win [PedraxPapel]
                print(f'Maquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tJogador venceu!!\n')
                time.sleep(5)
            #==================================================================
            elif jogador == 2 and maquina == 3:         #=== Maquina Win [PapelxTesoura]
                print(f'Maquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tMaquina venceu!!\n')
                time.sleep(5)
            elif maquina == 2 and jogador == 3:         #=== Jogador Win [PapelxTesoura]
                print(f'Maquina escolheu: {maquina}')
                print(f'Jogador escolheu: {jogador}')
                print('\tJogador venceu!!\n')
                time.sleep(5)
#============================== Timer ======================================
def contagemTimer():
    import time
    jokenpo = 'JOKENPO'
    print('\t'+ jokenpo[:2]);     time.sleep(1)
    print('\t'+ jokenpo[2:5]);    time.sleep(1)
    print('\t'+ jokenpo[5:7] + '!!');    time.sleep(1)


#Programa Principal::
display()