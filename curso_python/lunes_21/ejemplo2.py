
import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")

#Botones
"""def saludo():
    print("Hola mundo")"""

def saludo(nombre):
    print("hola "+nombre)

#boton1 = tkinter.Button(ventana, text="Presionar", padx=50, pady=50)
boton1 = tkinter.Button(ventana, text="Presionar", command= lambda: saludo("python"))

boton1.pack()


ventana.mainloop()