

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos você tem: VOTO NEGADO!')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos você tem: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos você tem: VOTO OBRIGATORIO')


#Programa Principal:
ano = int(input('Digite o ano em que você nasceu: '))
voto(ano)