
import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")

etiqueta = tkinter.Label(ventana, text="Hola cuates", bg = "yellow")
etiqueta.grid(row=0, column=7)


cajaTexto = tkinter.Entry(ventana)
cajaTexto.grid(row=2, column=0)

etiqueta = tkinter.Label(ventana)
etiqueta.grid(row=2, column=4)

def textoCajadeTexto():
    textoA = cajaTexto.get()
    print(textoA)
    etiqueta["text"]= textoA

boton1 = tkinter.Button(ventana, text="Nombre", command=textoCajadeTexto)
boton1.grid(row=2, column=2)

cajaTexto1 = tkinter.Entry(ventana)
cajaTexto1.grid(row=3, column=0)

etiqueta1 = tkinter.Label(ventana)
etiqueta1.grid(row=3, column=4)

def textoCajadeTexto1():
    textoB = cajaTexto1.get()
    print(textoB)
    etiqueta1["text"]= textoB

boton2 = tkinter.Button(ventana, text="Apellido", command=textoCajadeTexto1)
boton2.grid(row=3, column=2)





cajaTexto2 = tkinter.Entry(ventana)
cajaTexto2.grid(row=4, column=0)

etiqueta2 = tkinter.Label(ventana)
etiqueta2.grid(row=4, column=4)

def textoCajadeTexto2():
    textoC = cajaTexto2.get()
    print(textoC)
    etiqueta2["text"]= textoC

boton3 = tkinter.Button(ventana, text="Pseudonimo", command=textoCajadeTexto2)
boton3.grid(row=4, column=2)

#boton1 = tkinter.Button(ventana, text="Boton1")
#boton2 = tkinter.Button(ventana, text="Boton2")
#boton3 = tkinter.Button(ventana, text="Boton3")

ventana.mainloop()