def nombre(nombre="Nombre", apellido="Apellido"):
    yield nombre
    yield apellido
    print(nombre)
    print(apellido)

a = next(nombre())
print(a)
b = next(nombre())
print(b)

#print(next(nombre("Diego","Saavedra")))