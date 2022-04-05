#ejercicio 1: Imprimir en pantalla los números pares del 1 al 500
#ejercicio 2: Imprimir en pantalla los numeros primos del 1 al 100

"""contador = 2
while contador <=498:
    print(contador)
    contador +=2
print(contador)"""

'''contador = 1'''

"""for num in range(1,501):
    #print(num)
    if num % 2 == 0:
        print(num)"""

"""for num in range(1,500):
    if num % 2 == 0:
        print(num)"""
    
contador = 1
limite = 100
for a in range(1, limite+1):
    c = 0
    for b in range(1, contador+1):
        a = contador % b
        if a == 0:
            c = c  +1
    if c == 2:
        print(contador)
    else:
        a = a -1
    contador += 1
    
