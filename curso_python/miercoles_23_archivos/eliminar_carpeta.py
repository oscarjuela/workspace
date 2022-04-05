import os

if os.path.exists('C:/workspace/curso_python/mi_carpeta'):
    os.rmdir('C:/workspace/curso_python/mi_carpeta')
else:
    print('Directorio no existe')

