import tkinter

ventana = tkinter.Tk()
ventana.geometry("800x600")

#etiqueta = tkinter.Label(ventana, text="Hola Mundo", bg = "red")

etiqueta = tkinter.Label(ventana, text="Hola Mundo", bg = "yellow")

#etiqueta.pack(side=tkinter.BOTTOM)
#etiqueta.pack(side=tkinter.RIGHT)
#etiqueta.pack(side=tkinter.LEFT)
#etiqueta.pack(side=tkinter.TOP)

#etiqueta.pack(fill=tkinter.X)
#etiqueta.pack(fill=tkinter.Y, expand=True)
etiqueta.pack(fill=tkinter.BOTH, expand=True)


ventana.mainloop()