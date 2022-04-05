def saludar():
    print("Hola soy una funcion")

def super_funcion(funcion):
    funcion()

funcion = saludar

super_funcion(funcion)