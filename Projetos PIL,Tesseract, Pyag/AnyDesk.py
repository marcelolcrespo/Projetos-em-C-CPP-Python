import pyautogui as see
import time as delay
import PIL
import win32api, win32con
import keyboard


# 240,53,43 RGB Logo
# 46,151,62 RGB Aceitar
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('c'):
    if see.locateOnScreen('alvo.png'):
        see.moveTo('alvo.png')
        see.leftClick('alvo.png')
        #delay.sleep(1)
        #click(413, 571)
    #else:
        #delay.sleep(3)
