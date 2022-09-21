#Em resumo, essa funcionalidade consiste em atribuir o valor 0 quando definir parametros dentro de funções.
#Exemplo:


def soma(a,b,c):
#def soma(a, b, c=0) #==== o valor 0 funciona para garantir que o programa não acuse erro caso não receba
#um valor no terceiro parametro "C", tornando c=0 e aplicando a soma dos três valores
    s = a + b + c
    print(f'Valor da soma dos parametros: {s}')


#Ex 1:    ======= Recebendo três parametros
soma(1,2,3) #=== função que pede 3 parametros. Está indicado três valores na chamada da função
soma(1,2)   #=== função que pede apenas 2 parametros. Como a var C da função soma tem valor 0 atribuido, o
#programa vai rodar normalmente. Ex: a = 1, b = 2, c = 0 == resultado: 3
