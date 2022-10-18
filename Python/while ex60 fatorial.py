#Calcule o fatorial de um numero com python


num = int(input('Digite um valor: '))
fatorial = num
#n = num        #var para fazer o Fatorial c/ For

while fatorial != 1:
    fatorial -= 1
    num *= fatorial
print(num)


#Fatorial c/ For
#for c in range(1, n):
#    fatorial -= 1
#    num *= fatorial
#print(num)
