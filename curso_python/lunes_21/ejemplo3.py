import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")

#Cajas de texto
#cajaTexto = tkinter.Entry(ventana)
#cajaTexto = tkinter.Entry(ventana, font="Arial 50")
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack()

def textoCajadeTexto():
    textoA = cajaTexto.get()
    print(textoA)
    etiqueta["text"]= textoA

boton = tkinter.Button(ventana, text="click", command=textoCajadeTexto)
boton.pack()

ventana.mainloop()