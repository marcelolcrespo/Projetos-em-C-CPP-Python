import pyautogui as pyag
import PIL
import keyboard
import time


#def
def target():
    while pyag.locateOnScreen('targetOffBattle.png'):
        if pyag.locateOnScreen('targetOffBattle.png'):
            time.sleep(0.1)
            pyag.leftClick('targetOffBattle.png')
        while pyag.locateOnScreen('targetOnBattle.png'):
            time.sleep(0.1)

while not keyboard.is_pressed('c'):
    target()