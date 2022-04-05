'''Multiplicar 2 numeros sin usar el simbolo del multiplicación'''

a = int(input('Por favor ingrese el primer valor numérico: '))
b = int(input('Por favor ingrese el segundo valor numérico: '))

resultado = 0

for x in range(a):
    resultado = resultado + b
print(resultado)

