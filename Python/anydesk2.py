import pyautogui as bot
import PIL
import os
import time as delay
#mouse pos 1 123,746 (em cima do primeiro icone da barra de tarefas)
#mouse pos 2 280,661 (em cima do icone de acesso do anydesk)

while True:
    #bot.alert ('Start')
    delay.sleep(1)
    if bot.locateOnScreen('anydesklogo.png'):
        delay.sleep(2)
        bot.moveTo(123, 746)
        delay.sleep(2)
        bot.moveTo(280,661)
        delay.sleep(2)
        bot.leftClick(280,661)
        delay.sleep(2)
        bot.moveTo('aceitar.png')
        delay.sleep (2)

