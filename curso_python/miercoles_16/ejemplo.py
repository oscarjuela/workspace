class Monster:

    def __init__(self,nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria

    def myFunc(self):
        print("Hey, yo soy "+self.nombre)

monstrito = Monster("Sullivan","Asustador")
#print(monstrito.nombre)
#print(monstrito.categoria)
monstrito.myFunc()

monstrito2 = Monster("Mike Wazowski", "Ayudante")
monstrito2.myFunc()

