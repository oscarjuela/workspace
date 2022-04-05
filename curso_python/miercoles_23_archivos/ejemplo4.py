''''
Leer ficheros o archivos
'''

from io import open

archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/archivo.txt', 'a')

texto = archivo_texto.write('\nSiempre es una buena ocación para aprender python')

archivo_texto.close()

