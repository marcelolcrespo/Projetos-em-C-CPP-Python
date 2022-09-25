#Mostrar a tabuada de um numero inteiro digitado pelo usuario utilizando laço for

num = int(input('Digite um valor inteiro: '))
valor = num        #=== Guarda o valor de num para iterar no loop
tabuada = []       #=== Lista primária para receber valores
tabuada.append(valor) #=== passar o primeiro valor para a tabuada (Num * 1)
for c in range(1, 10):
    num = num + valor
    tabuada.append(num)
print(tabuada)