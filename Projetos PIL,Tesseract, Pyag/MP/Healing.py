import pyautogui as see
import time as delay
import PIL

mp = see.locateOnScreen('MP90%.png')

while True:
    if mp == see.locateOnScreen('MP90%.png'):
        see.keyDown('f3')
        see.keyUp('f3')