import os

if os.path.exists('C:/workspace/curso_python/miercoles_23_archivos/archivo.txt'):
    os.remove('C:/workspace/curso_python/miercoles_23_archivos/archivo.txt')
else:
    print("Archivo no existe")