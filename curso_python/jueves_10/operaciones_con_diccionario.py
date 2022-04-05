"""Operaciones con diccionario"""

from webbrowser import get


diccionario = {"nombre":"Juan", "apellido":"Perez", "cedula":1104097678, "f_nacimiento":"24/01/2015"}
"""lista1 = ["Juan", "Pedro", 'Maria']
lista2 = ["presona1", "persona2", "persona3"]

variable1 = zip(lista1, lista2)"""


print(diccionario.get("nombre"))
print(diccionario.get("cedula"))
print(diccionario.pop("f_nacimiento"))

print(diccionario)

diccionario.update({"f_nacimiento":"25/02/1994"})
print(diccionario)
print(diccionario.get("f_nacimiento"))

"""print("cedula" in diccionario)
print("edad" in diccionario)"""

print(1104097678 in diccionario.values())
print(1104097658 in diccionario.values())
