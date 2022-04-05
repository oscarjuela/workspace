def factorial(n):
    """
    Calcula el factorial de n
    
    n int> 0
    return n!
    """
#Comenzamos con el caso base
    if n == 1:
        return 1
#Definicien matematica
    return n * factorial(n-1)
n = int(input("Escribe un entero: "))
print(factorial(n))
