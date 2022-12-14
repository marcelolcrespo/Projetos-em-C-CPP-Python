#Calcular a % equivalente aos pixels de uma barra de vida/mana


barra = 117             #Valor de pixels de uma barra de vida/mana full
conta = 0
i = 2                  #== valor de i é equivalente a quantidade de pixels na barra. i = 10 -> 10% cara pedaço de pixel
for c in range(50):     #Loop de 10x para calcular de 10 em 10% da vida/mana. Para calcular de 1 em 1, alterar: var i, loop for, calculo primeira linha for para 1
    conta = barra * i/100
    i += 2
    #if c < 0:

    if i % 25 == 0:    #Usar quando precisar calcular % menores de vida/mana
        print('\n')
    print(f'{conta.__ceil__()}', end='  ')    #==== Arredondar o resultado pra cima
#138, 2