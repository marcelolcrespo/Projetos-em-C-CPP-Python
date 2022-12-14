import time

import PIL, pyautogui


time.sleep(1)
sc = pyautogui.screenshot()
sc.save('exemploo.png')

