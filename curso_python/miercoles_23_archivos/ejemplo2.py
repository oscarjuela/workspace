''''
Leer ficheros o archivos
'''

from io import open

archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/archivo.txt', 'r')

texto = archivo_texto.read()

print(texto)

archivo_texto.close()
