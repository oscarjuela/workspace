#Escribe un programa que lea un número e indique si es par o impar.

numero = 0

numero = int(input("Indique un número: "))

if (numero % 2) == 0:
  print(numero, " es par")
else:
  print(numero, " es impar")