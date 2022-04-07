# Escribe un programa que pida un nombre de usuario y una contraseña y 
# si se ha introducido <pepe> y <passwd#> se indica <Has entrado al sistema>, sino se da un error.

user_ = "pepe"
pwd_ = 'passwd#'
print("Bienvenido, ingrese sus datos")
print("Usuario: ")
user = input()
print("Contrasena: ")
pwd = input()
if user == user_ and pwd == pwd_:
    print("Bienvenido al programa")
else :
    print("Usiario o contraseña invalido")