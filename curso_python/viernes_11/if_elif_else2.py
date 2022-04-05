"""Saber rango de edad de una persona

por ejemplo
    Si es menor o igual a 12 anos, es un nino
    Si es mayor o igual  12 anos pero menor a 18, es un adolesente
    Si es mayor a 18 anos pero menor a 60, es un adulto
    Si es mayor o igual a 60 anos, es un adulto"""

edad = int(input("Por favor ingrese su edad: "))
if edad <= 12:
    print("Es un nino")

elif edad < 18:
    print("Es un adolecente")

elif edad <= 60:
    print("Es un adulto")
else:
    print("es un adulto mayor")

#elif edad > 60 and edad <= 105:
#    print("Es un adulto mayor")
#else:
#    print("Usted es un extraterrestre")
