"""Encontrar el mayor de 3 numeros ingresados por teclado

caso 1: Si el primero es el mayor
caso 2: si el segundo es el mayor
caso 3: si el tercero es el mayor
"""

"""x = input("Por favor ingrese el primer numero: ")
y = input("Por favor ingrese el segundo numero: ")
z = input("Por favor ingrese el tercer numero: ")

if x > y and x > z:
    print("El mayor es: ", x)
elif  y > x and y > z:
    print("El mayor es: ", y) 
elif  z > x and z > y:
    print("El mayor es: ", z) 
else:
    print("Los valores ingresados son iguales o no son valores enteros")"""


#print(f"Me alegro de conocerlo, {nombre}")

x = input("Por favor ingrese el primer numero: ")
y = input("Por favor ingrese el segundo numero: ")
z = input("Por favor ingrese el tercer numero: ")

if x > y and x > z:
    print(f"El mayor es {x}, y pertenece al primer numero")
elif  y > x and y > z:
    print(f"El mayor es {y}, y pertenece al segundo numero") 
elif  z > x and z > y:
    print(f"El mayor es {z}, y pertenece al tercer numero") 
else:
    print(f"Los valores ingresados: {x}, {y}, {z} son iguales o no son valores enteros")
