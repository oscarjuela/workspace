#Escribir un programa que lea un año indicar si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

agnio = int(input("Ingrese el año: "))

def es_bisiesto(agnio):
    if agnio % 400 ==0:
        return True
    elif agnio % 100 == 0:
        return False
    elif agnio % 4 == 0:
        return True
    else:
        return False
print(es_bisiesto(agnio))
           