

"""while True:
    try: #Intenta ejecutar el codigo
        x = int(input("Por favor ingrese un numero"))
        break
    except ValueError: #Maneja el error
        print("Ops! No era valido. Por favor intenta de nuevo")"""

"""def suma():
    try: #El codigo a ejecutarse es el siguiente
        a = int(input("Por favor ingrese un valor: "))
        b = int(input("Por favor ingrese un segundo valor: "))
        sum = a + b
        return sum
    except ValueError: #En caso de error
        print("Por favor ingrese un valor numerico #ValueError")
    except UnboundLocalError: #Otro error
        print("Por favor ingrese un valor numerico #UnboundLocalError")  
print(suma())"""



"""def resta():
    try: #El codigo a ejecutarse es el siguiente
        a = int(input("Por favor ingrese un valor: "))
        b = int(input("Por favor ingrese un segundo valor: "))
        rest = a - b
        return rest
    except ValueError: #En caso de error
        print("Por favor ingrese un valor numerico #ValueError")
    except UnboundLocalError: #Otro error
        print("Por favor ingrese un valor numerico #UnboundLocalError")  
print(resta())"""


"""def multiplicar():
    try: #El codigo a ejecutarse es el siguiente
        a = int(input("Por favor ingrese un valor: "))
        b = int(input("Por favor ingrese un segundo valor: "))
        mult = a - b
        return rest
    except ValueError: #En caso de error
        print("Por favor ingrese un valor numerico #ValueError")
    except UnboundLocalError: #Otro error
        print("Por favor ingrese un valor numerico #UnboundLocalError")  
print(resta())"""


def lee_entero():
    """ Solicita un valor entero y lo devuelve.
        Si el valor ingresado no es entero, lanza una excepción. """
while True:
    valor = int(input("Por favor ingrese un número entero: "))
     try:
     valor = int(valor)
     return valor
        except ValueError:
            print("Atención: debe ingresar un numero entero")