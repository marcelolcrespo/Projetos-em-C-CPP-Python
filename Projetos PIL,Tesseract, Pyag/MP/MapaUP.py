import pyautogui as bot
import PIL
from PIL.Image import Image
import time as delay
#localManaUP = str(input('DIgite um valor em Mana: Ex: MP56%.png'))
lista = [
         'MP2%.png', 'MP4%.png', 'MP6%.png', 'MP8%.png', 'MP10%.png',
         'MP12%.png', 'MP14%.png', 'MP16%.png', 'MP18%.png', 'MP20%.png',
         'MP22%.png', 'MP24%.png', 'MP26%.png', 'MP28%.png', 'MP30%.png',
         'MP32%.png', 'MP34%.png', 'MP36%.png', 'MP38%.png', 'MP40%.png',
         'MP42%.png', 'MP44%.png', 'MP46%.png', 'MP48%.png', 'MP50%.png',
         'MP52%.png', 'MP54%.png', 'MP56%.png', 'MP58%.png', 'MP60%.png',
         'MP62%.png', 'MP64%.png', 'MP66%.png', 'MP68%.png', 'MP70%.png',
         'MP72%.png', 'MP74%.png', 'MP76%.png', 'MP78%.png', 'MP80%.png',
         'MP82%.png', 'MP84%.png', 'MP86%.png', 'MP88%.png', 'MP90%.png',
         'MP92%.png', 'MP94%.png', 'MP96%.png', 'MP98%.png', 'MP100%.png',
         ]

valor = bot.locateOnScreen('MP100%.png')     #Valor de mana
num = 50                    #25 == 50/2, sendo 50 itens na lista, estou mostrando 25 (50/2), indo até MP50%.png
#print(lista[0:num])
while True:
    if valor == lista:       #condicional -- precisará de um for para iterar cada elemento
        bot.press('f3')
        print('existe')
    else:
        delay.sleep(1)
        print('nao existe!')

#print(localManaUP)
#if localManaUP in lista or lista[localManaUP:]:
#    print('\nExiste')
#else:
#    print('Não existe!')


#while True:
    #for pos in lista:
        #if bot.locateCenterOnScreen (localManaUP):
            #print ('Existe')
        #else:
            #print ('Nao existe')
