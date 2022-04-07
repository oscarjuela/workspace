# Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.

#from string import upperc
#from string import lowercase
 
 
let=str(input('ingrese una letra: '))
 
if let=='a'<=let<='z':
    print ('la letra es miniscula')
elif let=='A'<=let<='Z':
    print ('la letra es mayuscula')
else:
    print ('No es una letra')
