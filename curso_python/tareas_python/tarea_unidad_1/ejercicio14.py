"""
Crea una aplicación que pida un número y calcule su factorial 
(El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa 
por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120
"""

num = int(input("Ingrese un numero: "))

def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)
print("El factorial de: " + str(num) + ", es " + str(factorial(num)))