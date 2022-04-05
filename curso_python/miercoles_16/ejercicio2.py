"""
Crear una clase de algún animal especifico

Ejemplo de clase
    Gato
    Caballo
    Loro
    Hamster
Definir en el método __init__ por lo menos 5 caracteristicas que lo identifiquen
Definir en el método __str__ un mensaje que resalte por lo menos 2 caracteristicas del método __init__

En la instancia poder tener diferencias entre objetos propios de la misma clase
"""
class Animales:
    def __init__(self, tipo, tamano, comen, sonidos, cola):
        self.tipo = tipo
        self.tamano = tamano
        self.comen = comen
        self.sonidos = sonidos
        self.cola = cola

    def __str__(self):
        return f"El animal es un {self.tipo}, de {self.tamano} tamano"

    def sonido(self):
        return f"El {self.sonido} relincha fuerte"

caballo_1 = Animales("caballo", "gran")
print(caballo_1)
