

#palavra = str(input('Palavra/Frase:: '))
palavra = "apos a sopa".strip().upper()
palavra_separada = palavra.split()
mesclar = ''.join(palavra_separada)
inverso = ''
#print(f'Palavra digitada: {mesclar}')
for letra in range(len(mesclar)-1,-1,-1):
    inverso += mesclar[letra]
if inverso == mesclar:
    print('É um palindromo')
else:
    print('Não é um palindromo')

