'''
Crear un archivo
Elegir la ruta más adecuada donde desee crearlo
Elegir la opción de:
    Write (escribir) --> 'w'
    Read (leer) --> 'r'
    Abrir --> 'a'

Escribir los nombres de 5 personas a traves de variables

No olvidar cerrar el archivo con el nombre_Del_archivo.clase()
'''

from io import open

archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/ejercicio1.txt', 'w')

frase = 'Daniela Romero Cordova \nOscar Juela Sivisaca \nFabian Sotomayor Vivanco'

archivo_texto.write(frase)



archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/ejercicio1.txt', 'r')

texto = archivo_texto.read()



archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/ejercicio1.txt', 'a')

texto = archivo_texto.write('\nAnibal Gonzalez Gonzalez \nJose Merino Alverca \nJuan Perez')



archivo_texto = open('C:/workspace/curso_python/miercoles_23_archivos/ejercicio1.txt', 'r')

texto = archivo_texto.readlines()

archivo_texto.close()

print(texto[4])

archivo_texto.close()
