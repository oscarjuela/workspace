"""Ejemlos con if, elif y else

Una persona necesita ingresar por teclado 1 valor numerico este valor necesita comprobar los siguiente

    caso 1: si este valor es positivo
    caso 2: si este valor es negativo
    caso 3: si este valor es 0"""

"""print("¿Cómo se llama?")
nombre = input()
print(f"Me alegro de conocerle, {nombre}")"""

numero = int(input("Por favor ingrese un valor numerico: "))


#print(f"Me alegro de conocerle, {nombre}")
# -2, -1, 0, 1, 2, 3, 4, 5.....

if numero > 0:
    print("Es un valor positivo")

elif numero < 0:
    print("Es un valor negativo")

else:
    print("El valor es 0")
