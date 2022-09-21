#Manipulando Texto

#frase = 'Bom dia!'

        #Fatiamento::
    #frase[2] -- mostra apenas o caracter numero 2

        #Fatiamento com range::
    #frase[2:4] -- mostra as letras no range 2 a 3, cortando o ultimo valor

        #Fatiamento com pulos::
    #frase[2:4:2] -- vai pular o fatiamento de 2 em 2 casas


        #Fatiamento começando do inicio com range::
    #frase[:5]

        #Fatiamento com inicio e sem o fim:
    #frase[15:]

        #Fatiamento começa em uma posição indicada 9 e não tem fim, mas vai pular de 3 em 3::
    #frase[9::3]



    #=====================================================

            #Analise de string -- len

        #Comprimento da frase::
    #len(frase) -- Vai retornar o tamanho da string

        #Contar a repetição de letras::
    #frase.count('o') -- vai contar quantas vezes apareceu a letra na string

        #Encontrar::
    #frase.find('deo') -- Vai dizer em que momento começou o trecho de string definido na busca

        #Operador in::
    #'Curso' in frase -- vai dizer se existe a string 'Curso' na var frase


    #=======================================================

            #Transformação

        #Substituir alguma palavra dentro da frase por outra::
    #frase.replace('python', 'android')

        #Tornar maiúsculas::
    #frase.upper() -- Tornar uma string maiúscula

        #Tornar minúsculas::
    #frase.lower() -- Mantem os minúsculos e altera todo o resto para minúsculas

        #Capitalize - Mantem a primeira letra maiuscula e o resto minusculo::
    #frase.capitalize()

        #Title - Analisa a quantidade de palavras e faz o capitalize palavra por palavra
    #frase.title()

        #Strip - Remove os espaços inúteis no inicio e no fim das strings
    #frase.strip()
            #Para remover os espaços apenas do lado direito da string, usa-se: rstrip (right strip)
            #Para remover os espaços apenas do lado esquerdo da string, usa-se: lstrip (left strip)

        #Split - Dividir a string quebrando nos espaços dentro da frase
    #frase.split()

        #Unir nomes em listas - '-'.join(frase)::
    #'-'.join(frase) - vai juntar os elementos de uma string e usar o separador '-'. Ex:
    #Bom dia --> Bom-dia

