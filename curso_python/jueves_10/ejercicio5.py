"""Ejercicios de diccionario """

dic1 = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
print(dic1)
moneda = input("Introduce una divisa: ")
print(dic1.get(moneda.title(),"La divisa no está"))