import PIL
import time as slp
import pyautogui as bot


img = 'resposta7.png'
while True:
    try:
        if bot.locateOnScreen('num7.png'):
            slp.sleep(1)
            bot.moveTo('resposta7.png')
            slp.sleep(1)
            bot.leftClick('resposta7.png')

    except:
        print('Nao encontrado!')
        slp.sleep(1)