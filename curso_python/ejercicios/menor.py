lista = [2,3,4,-6,8,9,-1]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x
        if x < menor:
            menor = x 
        else:
            menor = menor
print(menor)