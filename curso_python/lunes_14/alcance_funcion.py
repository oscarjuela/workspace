"""variable = 60
def funcion():
    variable = 30
    if variable < 100:
        print(variable)
print(variable)
funcion()
print(variable)"""

variable = 60
def funcion():
    global variable
    if variable < 100:
        print(variable)
print(variable)
funcion()
print(variable)