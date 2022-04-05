''''
Leer ficheros o archivos
'''

from io import open

archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/archivo.txt', 'r')

texto = archivo_texto.readlines()

archivo_texto.close()

print(texto)
