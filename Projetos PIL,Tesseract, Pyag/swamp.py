import pyautogui as pyag
import PIL
import keyboard
import time
# ==================================== Vars ==========================================::
close = 0
# ==================================== Loot ==========================================::
def Loot():
    if not pyag.locateOnScreen('caveira.png'):
        pyag.rightClick(628, 334)  # NE
        #Norte Esquerda -- Jades 1~3
        if pyag.locateOnScreen('jade1.png'): #==== Jade1
            pyag.moveTo('jade1.png')
            time.sleep(0.8)
            pyag.mouseDown('jade1.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp('backpack.png')
        elif pyag.locateOnScreen('jade2.png'): #==== Jade2
            pyag.moveTo('jade2.png')
            time.sleep(0.8)
            pyag.mouseDown('jade2.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp('backpack.png')
        elif pyag.locateOnScreen('jade3.png'): #3==== Jade3
            pyag.moveTo('jade3.png')
            time.sleep(0.8)
            pyag.mouseDown('jade3.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp('backpack.png')
        pyag.rightClick(687,321)  # N
        # Norte -- Jades 1~3
        if pyag.locateOnScreen('jade1.png'): #==== Jade1
            pyag.moveTo('jade1.png')
            time.sleep(0.8)
            pyag.mouseDown('jade1.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp('backpack.png')
        elif pyag.locateOnScreen('jade2.png'): #==== Jade2
            pyag.moveTo('jade2.png')
            time.sleep(0.8)
            pyag.mouseDown('jade2.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp('backpack.png')
        elif pyag.locateOnScreen('jade3.png'): #3==== Jade3
            pyag.moveTo('jade3.png')
            time.sleep(0.8)
            pyag.mouseDown('jade3.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp('backpack.png')
        pyag.rightClick(728, 336)  # ND
        # Norte Direita -- Jades 1~3
        if pyag.locateOnScreen('jade1.png'): #==== Jade1
            pyag.moveTo('jade1.png')
            time.sleep(0.8)
            pyag.mouseDown('jade1.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.leftClick('jade1.png')
        elif pyag.locateOnScreen('jade2.png'): #==== Jade2
            pyag.moveTo('jade2.png')
            time.sleep(0.8)
            pyag.mouseDown('jade2.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp()
        elif pyag.locateOnScreen('jade3.png'): #3==== Jade3
            pyag.moveTo('jade3.png')
            time.sleep(0.8)
            pyag.mouseDown('jade3.png')
            time.sleep(0.5)
            pyag.moveTo('backpack.png')
            time.sleep(0.8)
            pyag.mouseUp()
    else:
        time.sleep(0.3)

#================ Programa =====================
while close == 0:
    if keyboard.is_pressed('o'):
        time.sleep(0.5)
        close = 1
        pyag.alert('Finalizado!')
        break
    else:
        if pyag.locateOnScreen('caveira.png'):
            pyag.leftClick('caveira.png')
            time.sleep(0.5)
            pyag.moveTo('perfil.png')
            while pyag.locateOnScreen('NameMob.png'):
                time.sleep(1)
        elif not pyag.locateOnScreen('caveira.png'):
            print('Loading...')
            time.sleep(1)
        elif not pyag.moveTo('perfil.png'):
            print('MoveTo não encontrado!')
        elif not pyag.leftClick('caveira.png'):
            print('Target não encontrado!')
        else:
            print('Não encontrou as imagens')
        Loot()