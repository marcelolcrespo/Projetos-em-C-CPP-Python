import time
import pyautogui as pyag, PIL

def loginTela():
    if pyag.locateOnScreen('safebraLogo.png'):
        time.sleep(1)
        pyag.leftClick('safebraLogo.png')
        time.sleep(1)
        pyag.write('Mv345771')
        time.sleep(1)
        pyag.locateOnScreen('loginTela.png')
        time.sleep(1)
        pyag.leftClick('loginTela.png')


def logarChar():
    time.sleep(1)
    if pyag.locateOnScreen('dehLogin.png'):
        time.sleep(1)
        pyag.leftClick('clicarOK.png')

def usarSkills():

    while pyag.locateOnScreen('manaShield.png'):
        time.sleep(1)
        pyag.press('f5')
        time.sleep(15)


while True:
    try:
        if not loginTela():
            if not logarChar():
                usarSkills()
            else:
                logarChar()
        else:
            loginTela()
            time.sleep(1)
            usarSkills()
    except:
        print('Img não localizada. Tentando denovo!')