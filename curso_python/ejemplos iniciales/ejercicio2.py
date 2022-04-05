"""
Crear unas dos variables con cada tipo de datos
numerico(entero, flotante)
cadenas de caracteres (string)
boleano (true o  false)

Listas que se representan por corchetes [] y son mutables
Tuplas que se representan por parentesis () y son inmutables
Diccionarios que se representan por llaves {} y se asiganan mediante clave y valor (solo el valor modificable)

Set que se representa con llaves {} y mueestr datos de forma ordenada, sin repetir valores

utilizar el print para conocer el valor del dato
utilizar el type para conocer el tipo de dato al que le pertenece 

Ejemplo
"""
#Numerico
entero = 5
flotante = 36.4

print(entero)
print(flotante)
print(type(entero))
print(type(flotante))

#String
cadena1 = "Oscar"
cadena2 = "Juela"

concatenar = cadena1 + ' '+ cadena2

print(concatenar)
print(type(concatenar))

#Listas
lista1 = [1, 'Juan', 2,'Maria', 3,'Daniela', 4,'Jose']
print(lista1)
print(type(lista1))

lista1.append(5)
lista1.append("Martha")
print(lista1)

lista1.remove(1)
lista1.remove("Juan")
print(lista1)

#Tuplas
casa1 = (1, 'rosado', 2, 'amarillo', 3, 'blanco')
print(casa1)
print(type(casa1))

#Diccionario
carrera = {'universidad':'Universidad Nacional de Loja', 'Facultad':'Agropecuaria y de Recursos Naturales Renovables', 
        'carrera':'Ingenieria Forestal'}
print('universidad')
print('Facultad')
print(carrera)
print(type(carrera))

#Set
valores = {1, 'a', 2, 2, 'a', 3, 'b', 4, 4, 'b', 'c'}
print(valores)
print(type(valores))

