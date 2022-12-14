#Testar se existe um pixel vermelho na posição X, Y pré-configurada
import time

from PIL import Image
import pyautogui as pyag, keyboard

valorG = 0
pixelG = 0


def menu():
    msg = 'Bem vindo!'
    print('-'*len(msg)*2)
    print(f'{"Bem vindo!":^20}')
    print('-'*len(msg)*2)


def curar_vida():
    global valorG
    valores_vida = [3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29, 31,
                    33, 36, 38, 40, 43, 45, 47, 50, 52, 54, 57, 59, 61,
                    64, 66, 68, 71, 73, 75, 78, 80, 82, 85, 87, 89, 92,
                    94, 96, 99, 101, 103, 106, 108, 110, 113, 115, 117]     #Valores p/ vida 2%~100% / 50 valores
    print(f'Valores disponíveis: \n{valores_vida[:25]}\n{valores_vida[25:]}\n')
    num = int(input('Valor: '))
    valorG = num
    print(num)
    if num in valores_vida:
        print(f'{num} equivale a {(valores_vida.index(num)*2)+2}% de vida.')
        print('True')
    elif not num in valores_vida:
        print('Esse valor não consta na lista')
    #img = pyag.screenshot('vidaTempoReal.png', region=(234, 78, 117, 2)) -- local da barra


def checarPixel():
    global valorG, pixelG
    x = valorG
    y = 0
    im = pyag.screenshot ('vidaTempoReal.png', region=(234, 78, 117, 1))
    time.sleep(0.3)
    pix = im.getpixel((x, y))
    pixelG = pix[0]
    #print(pix[0])
    print(pixelG)
    if pix[0] >= 160:
        pass
        #print('165 ou maior')
    elif pix[0] <= 159:
        pyag.keyDown('f3')
        pyag.keyUp('f3')


"""img = 'HPBattleList100%.png'
print (rgb(img, 5, 0))"""

op = ' '

menu()
curar_vida()
while True:
    checarPixel()
    #op = str(input('Deseja testar novamente? [S/N]: ')).upper()
