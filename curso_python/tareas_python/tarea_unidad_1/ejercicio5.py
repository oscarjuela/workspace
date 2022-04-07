#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde

minutos =int(input('Ingrese los minutos> '))

h=int(minutos/60)
m2=int(minutos%60)
print('Corresponde a ',h,'horas y ',m2,'minutos')