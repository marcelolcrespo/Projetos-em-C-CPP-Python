import pyautogui as pyag
#import PIL
import keyboard
import time, cv2
import psutil
import threading

"""

"""
# ============================ VARS =================================
janela = False
vida = list()
close = 0
healManaG = 0
healVidaG = 0
#healTotal = 0
#hpConfig = 0
hp = ''
valor = 0
"""lista = [
         'HP2%.png', 'HP4%.png', 'HP6%.png', 'HP8%.png', 'HP10%.png',
         'HP12%.png', 'HP14%.png', 'HP16%.png', 'HP18%.png', 'HP20%.png',
         'HP22%.png', 'HP24%.png', 'HP26%.png', 'HP28%.png', 'HP30%.png',
         'HP32%.png', 'HP34%.png', 'HP36%.png', 'HP38%.png', 'HP40%.png',
         'HP42%.png', 'HP44%.png', 'HP46%.png', 'HP48%.png', 'HP50%.png',
         'HP52%.png', 'HP54%.png', 'HP56%.png', 'HP58%.png', 'HP60%.png',
         'HP62%.png', 'HP64%.png', 'HP66%.png', 'HP68%.png', 'HP70%.png',
         'HP72%.png', 'HP74%.png', 'HP76%.png', 'HP78%.png', 'HP80%.png',
         'HP82%.png', 'HP84%.png', 'HP86%.png', 'HP88%.png', 'HP90%.png',
         'HP92%.png', 'HP94%.png', 'HP96%.png', 'HP98%.png', 'HP100%.png',
         ]"""

"""while close == 0:
    while healVidaG >= 0:
        if healTotal <= 0:
            healTotal += hpConfig
        else:
            hp = f'HP{healTotal}%.png'
            healTotal -= 2
            time.sleep(0.5)
            print(hp)
            break
    if pyag.locateOnScreen(hp):
        print(f'Config pausada{hp}')
        if pyag.locateOnScreen(hp):
            pyag.keyDown('f3')
            time.sleep(9)
            pyag.keyUp('f3')
        break"""

# ============================ DEF =================================
def fecharJogo():
    global close
    if keyboard.is_pressed('o'):  # === Checar se o jogador deseja finalizar o programa
        time.sleep(0.5)
        close = 1
        pyag.alert('Finalizado!')  # == Alerta de programa finalizado


def checkJogoAberto():
    global janela  # === Var Global para espelhar se o game ta aberto ou fechado
    a = "client.exe" in (i.name() for i in psutil.process_iter())  # Verificar no sistema se o programa está aberto
    if not a == True:
        print('Aguardando inicialização do jogo...')
        time.sleep(2)
        janela = False
    else:
        print('Jogo inicializado!')
        janela = True


def configs():      #Input de config global ======== Curar Mana a partir dos valores digitados
    global healVidaG, hpConfig, healManaG, vida
    print('[2%]~[100%] HP -- escolher um número Par')
    healVida = int(input(':: '))
    healVidaG = healVida
    hpConfig = healVida
    for i in range(0, hpConfig+2, 2):
        vida.append(f'HP{i}%.png')
    print('[2%]~[100%] Mana -- escolher um número Par')
    healMana = int(input(':: '))
    healManaG = healMana
    """for i in range(0, healMana+2, 2):
        mana.append(f'MP{i}%.png')""" #Não existem imagens com valores em mana na mesma pasta.
    print(vida)
    #print(mana)



def healVida():
    """global valor, healVidaG, hp, healTotal, hpConfig
    healTotal = healVidaG   #Receber valor total declarado em config para resetar o contador
    hp = pyag.locateOnScreen(f'HP{healTotal}%.png')
    hpCheck = hp
    hpConfig = healTotal
    while True:
        hp = f'HP{healTotal}%.png'
        print(hp)
        healTotal -= 2
        #time.sleep(2)"""
    global healVidaG, hp
    #hp = pyag.locateOnScreen(f'HP{healVidaG}%.png')
    #if hp == pyag.locateOnScreen(f'HP{healVidaG}%.png'):
        #pyag.keyDown('f3')
        #time.sleep(0.2)
        #pyag.keyUp('f3')
    #print(hp)
    #print(healVidaG, healManaG)
    img = pyag.screenshot('vidaTempoReal.png', region=(234, 78, 117, 2))
    time.sleep(2)
    i = 0
    guardar_valor = healVidaG
    while i <= len(vida):           #Não funcionou
        if 'vidaTempoReal.png' == f'HP{healVidaG}%.png':
            print('True')
            print(vida)
            healVidaG -= 2
            if healVidaG == 0:
                healVidaG = guardar_valor
        else:
            print('False')
        i += 1


# ============================ Programa =================================

#RGB vida blood - 195, 41, 41

# Testar se o processo está ativo

configs()       #=== Configuração do heal Vida | Mana nessa ordem


threading.Thread(target=fecharJogo()).start()
while janela == False:
    checkJogoAberto()

while close == 0:                   #Rodar o sistema
    threading.Thread(target=fecharJogo()).start()
    try:
        if pyag.locateOnScreen('perfilBlood.png'):
            threading.Thread(target=healVida()).start()
    except:
        print('Aguardando img...')

