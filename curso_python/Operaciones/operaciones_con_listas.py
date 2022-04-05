"""Ejemplos de operaciones con listas"""

lista = ['a', 'e', 'i', 'o', 'u','e']
print(len(lista))
print("La cantidad de valores de listas es:",len(lista))
print(lista[4])
lista2 = lista[0:3]
print(lista2)

lista.append('j')
print(lista)
print(len(lista))

lista.remove('j')
print(lista)
print(len(lista))

lista.insert(4,'Juan')
print(lista)

"""lista.remove('x')
print(lista)
print(len(lista))"""

print('j' in lista)

print(lista.index("e"))

lista3 = lista + lista2
print(lista3)

lista[0:5]
print(lista[0:5])

print(lista3[0:9:2])

print(max(lista))
print(min(lista))

print(lista3.index)