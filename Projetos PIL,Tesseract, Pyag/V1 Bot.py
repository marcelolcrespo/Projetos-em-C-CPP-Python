import pyautogui as pyag, PIL, time, keyboard
import os, threading

pontoStartX = 0
pontoStartY = 0
x = 0
y = 0

timerG = 0

minimapX = 0
minimapY = 0
mapResX = 0
mapResY = 0

'''def finalizar():
        while True:
            if keyboard.is_pressed('q'):
                os._exit(0)'''

def forceExit():
    if keyboard.is_pressed('k'):
        pyag.alert('Programa encerrado!')
        keyboard.press('esc')
        os._exit()


def alert():
    msg = 'Configure o Script'
    print('_'*len(msg))
    print(msg)
    print('_' * len(msg))


def configsBattle():
    global x, y, pontoStartX, pontoStartY
    print('OBS:: A primeira configuração pode ser observada no paint, no canto inferior esquerdo\n'
          'é a primeira sequencia de números que aparecem ao posicionar o mouse na tela.\n')
    pontoStartX = int(input('Ponto de inicio do pixel X: '))
    pontoStartY = int(input('Ponto de inicio do pixel Y: '))
    print('\nAgora digite a area que deverá ser verificada.')
    x = int(input('X: '))
    y = int(input('Y: '))
    #print(x,y)
    pyag.alert(f'Configurações [Ponto de Start] X = {pontoStartX}, Y = {pontoStartY}\n'
               f' Resolução [Area de Verificação]: X = {x}, Y = {y}')


def configMinimap():
    global minimapX, minimapY, mapResX, mapResY
    minimapX = int(input('Local do minimapa - posX: '))
    minimapY = int(input('Local d minimapa - posY: '))
    print('Agora você precisa digitar o tamanho do minimap. utilize a'
          ' ferramenta Selecionar para pegar o X e Y do minimap')
    mapResX = int(input('Resolução area minimapa X: '))
    mapResY = int(input('Resolução area minimapa Y: '))
    pyag.alert(f'Configuração: X = {minimapX}, Y = {minimapY}\n'
               f'Resolução [Area de Verificação]: X = {mapResX}, Y = {mapResY}')
    pyag.alert('BOT CONFIGURADO!')


def antiBug():
    while True:
        if pyag.locateOnScreen('mid2.png', region=(minimapX, minimapY, mapResX, mapResY)):
            #1150, 28, 205, 201
            time.sleep(1)
        else:
            keyboard.press('w')
            #time.sleep(1)
            keyboard.press('esc')
            #time.sleep(1)
            keyboard.press('s')
            keyboard.press('esc')


def lure():
    global timerG
    #470, 208, 530, 455
    #(92, 149, 200, 363)
    quantidade_mobVerdelife = 0
    #Listas para encontrar todos na tela c/ regioes especificadas
    local_todosStage1seg = list(pyag.locateAllOnScreen('stage1seg.png', region=(470, 208, 530, 455)))
    local_todosStage1 = list(pyag.locateAllOnScreen('stage1.png', region=(470, 208, 530, 455)))
    local_todosStage2 = list(pyag.locateAllOnScreen('stage2.png', region=(470, 208, 530, 455)))
    local_todosStage3 = list(pyag.locateAllOnScreen('stage3.png', region=(470, 208, 530, 455)))
    local_todosStage4 = list(pyag.locateAllOnScreen('stage4.png', region=(470, 208, 530, 455)))
    local_todosStage5 = list(pyag.locateAllOnScreen('stage5.png', region=(470, 208, 530, 455)))
    local_todosStage6 = list(pyag.locateAllOnScreen('stage6.png', region=(470, 208, 530, 455)))
    local_todosStage7 = list(pyag.locateAllOnScreen('stage7.png', region=(470, 208, 530, 455)))
    local_todosStage8 = list(pyag.locateAllOnScreen('stage8.png', region=(470, 208, 530, 455)))
    local_todosStage9 = list(pyag.locateAllOnScreen('stage9.png', region=(470, 208, 530, 455)))
    local_todosStage10 = list(pyag.locateAllOnScreen('stage10.png', region=(470, 208, 530, 455)))
    #, region = (470, 208, 530, 455))

    #Variaveis que guardam as imagens encontradas em cada tipo (verde, verde claro, yellow, red e black)
    quant_stage1 = len(local_todosStage1)
    quant_stage1seg = len(local_todosStage1seg)
    quant_stage2 = len(local_todosStage2)
    quant_stage3 = len(local_todosStage3)
    quant_stage4 = len(local_todosStage4)
    quant_stage5 = len(local_todosStage5)
    quant_stage6 = len(local_todosStage6)
    quant_stage7 = len(local_todosStage7)
    quant_stage8 = len(local_todosStage8)
    quant_stage9 = len(local_todosStage9)
    quant_stage10 = len(local_todosStage10)
    quantMob = 0
    quantMob = quant_stage1 + quant_stage2 + quant_stage3 + quant_stage4 + quant_stage5 + quant_stage6 + quant_stage7 + quant_stage8 + quant_stage9 + quant_stage10 + quant_stage1seg
    print(quantMob)
    if quantMob >= 1 and quantMob <=3:
        keyboard.press('esc')
        time.sleep(0.2)
    elif quantMob > 3:
        regBattle()


def battle():
    #global timerG
    #timer = 0
    #(92, 149, 200, 363) testando target on
    #region = (92, 149, 200, 363)) and \ - testar battle
    #region=(374, 167, 530, 440)) - testar tela
    while pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage1seg.png', region=(374, 167, 530, 440)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage1.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage2.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage3.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage4.png', region=(450, 254, 357, 294)) or\
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage5.png', region=(374, 167, 530, 440)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage6.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage7.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage8.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage9.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage10.png', region=(450, 254, 357, 294)):
        """pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) and\
        pyag.locateOnScreen('verdeLife.png', region=(470, 208, 530, 455)) or \
        pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) and \
        pyag.locateOnScreen('yellowLife.png', region=(470, 208, 530, 455)) or \
        pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) and \
        pyag.locateOnScreen('blackLife.png', region=(470, 208, 530, 455)) or \
        pyag.locateOnScreen('targetOnBattle.png', region=(92, 149, 200, 363)) and \
        pyag.locateOnScreen('redLife.png', region=(470, 208, 530, 455)) or\
        pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) and \
        pyag.locateOnScreen('verdeClaroLife.png', region=(450, 254, 357, 294)):"""
        #keyboard.press('space')
        time.sleep(0.5)
        buff()
        time.sleep(0.2)
        spells()
        if pyag.locateOnScreen('targetOnBattle.png'):
            continue
    loot()

        #time.sleep(0.1)67


def regBattle():        #Verificar sem tem mob perto do personagem
    #while pyag.locateOnScreen('stage1.png', region=(pontoStartX, pontoStartY, x, y)):
        #if pyag.locateOnScreen('stage1.png', region=(pontoStartX, pontoStartY, x, y)):  #Região ao redor do personagem
        #470, 208, 530, 455
    while pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage1seg.png', region=(374, 167, 530, 440)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage1.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage2.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or\
            pyag.locateOnScreen('stage3.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage4.png', region=(450, 254, 357, 294)) or\
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage5.png', region=(374, 167, 530, 440)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage6.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage7.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage8.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage9.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) or \
            pyag.locateOnScreen('stage10.png', region=(450, 254, 357, 294)):

        """if pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) and\
            pyag.locateOnScreen('verdeLife.png', region=(374, 167, 530, 440)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) and\
            pyag.locateOnScreen('yellowLife.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) and\
            pyag.locateOnScreen('redLife.png', region=(450, 254, 357, 294)) or \
            pyag.locateOnScreen('targetOffBattle2.png', region=(92, 149, 200, 363)) and\
            pyag.locateOnScreen('blackLife.png', region=(450, 254, 357, 294)):"""
            #lure()
        battle()
            #loot()
#470, 208, 355, 355


def walkW1():
                # ===============================    W1    ==================================
    #while pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
    #while pyag.locateOnScreen('exclamacao.png', region=(minimapX, minimapY, mapResX, mapResY)):
        #if pyag.locateOnScreen('exclamacao.png', region=(minimapX, minimapY, mapResX, mapResY)):
    while pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
        if pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
            #time.sleep(1)
            pyag.leftClick('exclamacao.png')
            if lure():
                keyboard.press('esc')
                battle()
            else:
                pass
            #time.sleep(10)
            continue
        #else:
            #time.sleep(1)
        elif not pyag.locateOnScreen('exclamacao.png'):
            time.sleep(1)
            pass


def walkW2():
                #===============================    W2    ===================================
        #if not pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
    while pyag.locateOnScreen('bolsa.png', region=(1150, 28, 205, 201)):
        if pyag.locateOnScreen('bolsa.png', region=(1150, 28, 205, 201)):
            #time.sleep(1)
            pyag.leftClick('bolsa.png')
            if lure():
                keyboard.press('esc')
                battle()
            else:
                pass
            # time.sleep(10)
            continue
            # else:
            # time.sleep(1)
        elif not pyag.locateOnScreen('bolsa.png'):
            time.sleep(1)
            pass


def walkW3():
    # ===============================    W2    ===================================
    # if not pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
    while pyag.locateOnScreen('cash.png', region=(1150, 28, 205, 201)):
        if pyag.locateOnScreen('cash.png', region=(1150, 28, 205, 201)):
            #time.sleep(1)
            pyag.leftClick('cash.png')
            if lure():
                keyboard.press('esc')
                battle()
            else:
                pass
            # time.sleep(10)
            continue
            # else:
            # time.sleep(1)
        elif not pyag.locateOnScreen('cash.png'):
            time.sleep(1)
            pass


def walkW4():
    # ===============================    W2    ===================================
    # if not pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
    while pyag.locateOnScreen('cruz.png', region=(1150, 28, 205, 201)):
        if pyag.locateOnScreen('cruz.png', region=(1150, 28, 205, 201)):
            #time.sleep(1)
            pyag.leftClick('cruz.png')
            if lure():
                keyboard.press('esc')
                battle()
            else:
                pass
            # time.sleep(10)
            continue
            # else:
            # time.sleep(1)
        elif not pyag.locateOnScreen('cruz.png'):
            time.sleep(1)
            pass


def walkW5():
    # ===============================    W2    ===================================
    # if not pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
    while pyag.locateOnScreen('porta.png', region=(1150, 28, 205, 201)):
        if pyag.locateOnScreen('porta.png', region=(1150, 28, 205, 201)):
            #time.sleep(1)
            pyag.leftClick('porta.png')
            if lure():
                keyboard.press('esc')
                battle()
            else:
                pass
            # time.sleep(10)
            continue
            # else:
            # time.sleep(1)
        elif not pyag.locateOnScreen('porta.png'):
            time.sleep(1)
            pass


def walkW6():
    # ===============================    W2    ===================================
    # if not pyag.locateOnScreen('exclamacao.png', region=(1150, 28, 205, 201)):
    while pyag.locateOnScreen('monstro.png', region=(1150, 28, 205, 201)):
        if pyag.locateOnScreen('monstro.png', region=(1150, 28, 205, 201)):
            #time.sleep(1)
            pyag.leftClick('monstro.png')
            if lure():
                keyboard.press('esc')
                battle()
            else:
                pass
            # time.sleep(10)
            continue
            # else:
            # time.sleep(1)
        elif not pyag.locateOnScreen('monstro.png'):
            time.sleep(1)
            pass


def spells():
    #92, 149, 200, 363
    #if regBattle():
        time.sleep(0.2)
        keyboard.press('f9')
        time.sleep(0.2)
        keyboard.press('f7')
        time.sleep(0.2)
        keyboard.press('f8')
        time.sleep(0.2)
        keyboard.press('c')
        time.sleep(0.2)
        #pyag.leftClick(641, 380)


def caveBot():
    walkW1()
    time.sleep(0.5)
    pass
    walkW2()
    time.sleep(0.5)
    pass
    walkW3()
    time.sleep(0.5)
    pass
    walkW4()
    time.sleep(0.5)
    pass
    walkW5()
    time.sleep(0.5)
    pass
    walkW6()
    time.sleep(0.5)
    pass


def loot():
    """tentativa = 0
    local_todos = list(pyag.locateAllOnScreen('stirge.png', region=(450, 254, 357, 294)))
    quantidade_loot = len(local_todos)
    while pyag.locateOnScreen('stirge.png', region=(453, 247, 349, 299)):
        if pyag.locateOnScreen('stirge.png', region=(453, 247, 349, 299)):
            #print(local_todos)
            time.sleep(0.5)
            pyag.scroll('down')
            time.sleep(0.5)
            tentativa += 1
            keyboard.press('f')
        elif tentativa >= 2:
            pass
        else:
            pass
    tentativa = 0"""
    #== NE
    pyag.keyDown('shift')
    pyag.rightClick(587, 320)
    pyag.keyUp('shift')
    # == N67
    pyag.keyDown('shift')
    pyag.rightClick(641,321)
    pyag.keyUp('shift')
    # == ND
    pyag.keyDown('shift')
    pyag.rightClick(694,322)
    pyag.keyUp('shift')
    # == CD
    pyag.keyDown('shift')
    pyag.rightClick(696,378)
    pyag.keyUp('shift')
    # == SD
    pyag.keyDown('shift')
    pyag.rightClick(695,427)
    pyag.keyUp('shift')
    # == S
    pyag.keyDown('shift')
    pyag.rightClick(639,429)
    pyag.keyUp('shift')
    # == SE
    pyag.keyDown('shift')
    pyag.rightClick(588,427)
    pyag.keyUp('shift')
    # == CE
    pyag.keyDown('shift')
    pyag.rightClick(589,374)
    pyag.keyUp('shift')

def buff():
   # if regBattle():
    time.sleep(0.3)
    keyboard.press('5') #==== Def Mágica
    time.sleep(0.2)
    pyag.leftClick(641,380)
    time.sleep(0.2)
    keyboard.press('6')  # ==== Dano Mágico
    time.sleep(0.2)
    pyag.leftClick(641, 380)
    time.sleep(0.2)
    keyboard.press('7')  # ==== Heal
    time.sleep(0.2)
    pyag.leftClick(641, 380)
    time.sleep(0.2)
    """elif pyag.locateOnScreen('resEarth.png') or \
         pyag.locateOnScreen('resWater.png') or \
         pyag.locateOnScreen('resWind.png') or \
         pyag.locateOnScreen('resLight.png'):
        pass
        time.sleep(0.1)
        keyboard.press('f5')"""

#==================================== PROGRAMA ==========================================

#threading.Thread(target=finalizar()).start()    #1erificar ao msmo tempo
#threading.Thread(target=antiBug()).start()      #Verificar ao msmo tempo
#alert()
#configsBattle()
#configMinimap()


while True:
    threading.Thread(target=lure()).start()      #Verificar ao msmo tempo
    #threading.Thread(target=buff()).start()
    if keyboard.is_pressed('k'):
        forceExit()
    else:
        try:
            caveBot()
        except:
            #continue
            print('tentando dnv')