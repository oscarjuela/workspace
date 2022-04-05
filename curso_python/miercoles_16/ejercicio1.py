"""
Crear 1 clase llamada animal
de la cual vamos a crear 5 objetos
razonar cuales son los metodos y atributos genéricos que tienen los animales
"""

class Animales:
    def __init__(self, especie, genero):
        self.especie = especie
        self.genero = genero
    
    def correr(self):
        print("Estoy corriendo")
   
    def sonido(self):
        print("Estoy rugiendo")

    def dormir(self):
        print("Estoy durmiendo")

    def tipo_pelaje(self):
        print("soy lanudo")

    def comer(self):
        print("estoy con hambre")

perro = Animales("perro", "hembra")
print(perro.especie)
print(perro.genero)
perro.comer()
perro.correr()
perro.dormir()
perro.tipo_pelaje()
perro.sonido

gato = Animales("gato", "macho")
print(gato.especie)
print(gato.genero)
gato.comer()
gato.correr()
gato.dormir()
gato.tipo_pelaje()
gato.sonido

caballo = Animales("caballo", "macho")
print(caballo.especie)
print(caballo.genero)
caballo.comer()
caballo.correr()
caballo.dormir()
caballo.tipo_pelaje()
caballo.sonido

tigre = Animales("tigre", "hembra")
print(tigre.especie)
print(tigre.genero)
tigre.comer()
tigre.correr()
tigre.dormir()
tigre.tipo_pelaje()
tigre.sonido

oso = Animales("oso", "macho")
print(oso.especie)
print(oso.genero)
oso.comer()
oso.correr()
oso.dormir()
oso.tipo_pelaje()
oso.sonido