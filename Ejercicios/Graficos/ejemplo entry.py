from tkinter import *

raiz=Tk()
miframe=Frame(raiz, width=1200,height=600)
miframe.pack()

minombre=StringVar()

cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=1,column=1,padx=10,pady=10)
cuadronombre.config(fg="red",justify="right")

cuadropass=Entry(miframe)
cuadropass.grid(row=0,column=1,padx=10,pady=10)
cuadropass.config(show="*")


cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=2,column=1,padx=10,pady=10)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=3,column=1,padx=10,pady=10)


textocomentario=Text(miframe, width=16,height=5)
textocomentario.grid(row=4,column=1,padx=10,pady=10)

scrollvert=Scrollbar(miframe, command=textocomentario.yview)
scrollvert.grid(row=4,column=2,sticky=NSEW)


textocomentario.config(yscrollcommand=scrollvert.set)

nombrelabel=Label(miframe,text="Nombre: ")
nombrelabel.grid(row=1,column=0,sticky="w",padx=10,pady=10)

apellidolabel=Label(miframe,text="Apellido: ")
apellidolabel.grid(row=2,column=0,sticky="w",padx=10,pady=10)

direccionlabel=Label(miframe,text="Direccion: ")
direccionlabel.grid(row=3,column=0,sticky="w",padx=10,pady=10)

passlabel=Label(miframe,text="Password: ")
passlabel.grid(row=0,column=0,sticky="w",padx=10,pady=10)

comentarioslabel=Label(miframe,text="Comentarios: ")
comentarioslabel.grid(row=4,column=0,sticky="w",padx=10,pady=10)

def codigoboton():
    minombre.set("Juan")

boton=Button(raiz,text="Enviar",command=codigoboton)
boton.pack()


raiz.mainloop()