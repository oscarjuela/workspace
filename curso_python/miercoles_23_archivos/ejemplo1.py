''''
Crear ficheros o archivos
'''
from io import open

archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/archivo.txt', 'w')

frase = 'Esto es una frase escrita desde Python \n esto es otra linea \n esto es una tercera linea'

archivo_texto.write(frase)

archivo_texto.close()
