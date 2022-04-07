# Pedir un número por teclado y mostrar la tabla de multiplicar

numero=int(input('ingrese un número: '))

for f in range(1,13):
	multiplicacion = f * numero 
	print(numero, "x", f, "=",multiplicacion)
