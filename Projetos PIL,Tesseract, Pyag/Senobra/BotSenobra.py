import time
from PIL import Image
import pytesseract as pyt, pyautogui as pyag
import os, keyboard
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os, threading

value = ''
value2 = ''
converterLife = 0
converterMana = 0
life = ' '
mana = ' '

from subprocess import check_output
pyt.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-ocr\\tesseract.exe"

class Application:
    def __init__(self, master=None):
        pass


def spellsLife():
    # ===== Spells =====
    time.sleep(0.5)
    pyag.keyDown('f3')
    pyag.keyUp('f3')


def CheckLifePoints_Tesseract():
    from PIL import Image
    global life, converterLife
    if pyag.locateOnScreen('manaShield.png'):       #Verificar se tá na tela do Game
        time.sleep(1)
        img1 = pyag.screenshot('imgLifeHeal.png', region=(1306, 139, 52, 17))
        checkLifePoints = pyt.image_to_string(Image.open('imgLifeHeal.png'))
        life = checkLifePoints
        print(checkLifePoints)
                #=========== Condicional Vida =============
        if life == '' or life == ' ':
            pass
        else:
            converterLife = int(life[0:5])
    else:
        pass


def CheckManaPoints_Tesseract():
    from PIL import Image
    global mana, converterMana
    if pyag.locateOnScreen('manaShield.png'):       #Verificar se tá na tela do Game
        time.sleep(1)
        img2 = pyag.screenshot('imgManaHeal.png', region=(1306, 153, 52, 17))
        checkManaPoints = pyt.image_to_string(Image.open('imgManaHeal.png'))
        mana = checkManaPoints
        print(checkManaPoints)
                #=========== Condicional Mana =============
        if mana == '' or mana == ' ':
            pass
        else:
            converterMana = int(mana[0:5])
    else:
        pass


def store_value():      #Guardar valores de entrada
    global value, converterLife
    value = entry_vida.get()
    threading.Thread(target=CheckLifePoints_Tesseract()).start()
    threading.Thread(target=lifeHeal()).start()


def store_value2():      #Guardar valores de entrada
    global value2,converterMana
    value2 = entry_mana.get()
    threading.Thread(target=CheckManaPoints_Tesseract()).start()
    threading.Thread(target=manaHeal()).start()


def lifeHeal():
    global value, converterLife
    # ======= LIFE =========
    if converterLife == 0:
        pass
    elif int(value) < 0:
        pyag.alert('Você precisa digitar um valor maior que 0!')

    if int(value) >= converterLife:     #Curar (Exura vita)
        time.sleep(0.3)
        pyag.keyDown ('num1')
        pyag.keyUp ('num1')
        time.sleep (1)


def manaHeal():
    global value2, converterMana
    # ======= MANA =========
    if converterMana == 0:
        pass
    elif int (value2) < 0:
        pyag.alert('Você precisa digitar um valor maior que 0!')

    if int(value2) >= converterMana:  # Usar POT (Exura vita)
        time.sleep(0.3)
        pyag.keyDown('f2')
        pyag.keyUp('f2')
        time.sleep(2)


#================== Programa ======================
janela = tk.Tk()
janela.geometry("380x120")
janela.resizable(False,False)
janela.title('BOTSenobra')
logoIcon = PhotoImage(file='senobraIcon.png')
janela.iconphoto (False, logoIcon)

# === MenuBar ===
menubar = Menu(janela)
janela.config(menu=menubar)

filemenu = Menu(menubar)
menubar.add_cascade(label='Arquivo', menu=filemenu)

#=== BackGround ===

back = Label(janela)
back.la = PhotoImage(file = 'background2.png')
back['image'] = back.la
back.place(x=10,y=10)

#=== Labels ===

label_vida = tk.Label(janela, text='Vida', bg="red", fg="white", width=25)
label_vida.grid(row=0, column=0, padx=10, pady=10)

label_mana = tk.Label(janela, text='Mana', bg="blue", fg="white", width=25)
label_mana.grid(row=1, column=0, padx=10, pady=10)

#=== Entry ===
entry_vida = tk.Entry(janela, width_=10)            # === Vida
entry_vida.grid(row=0, column=1, padx=10, pady=10)

entry_mana = tk.Entry(janela, width_=10)            # === Mana
entry_mana.grid(row=1, column=1, padx=10, pady=10)

# === Button ===
botao_start_life = tk.Button(janela, text='Start', command_=store_value, height=1)
botao_start_life.grid(row=0, column=3, padx=10, pady=10, columnspan=2, ipadx=6)

botao_start_mana = tk.Button(janela, text='Start', command_=store_value2, height=1)
botao_start_mana.grid(row=1, column=3, padx=10, pady=10, columnspan=2, ipadx=6)

Application(janela)
janela.mainloop()