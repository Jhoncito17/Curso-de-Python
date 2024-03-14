from tkinter import *

raiz=Tk()
opcion=IntVar()

def imprimir():
    #print(opcion.get())
    
    if opcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")
        
    elif opcion.get()==2:
        etiqueta.config(text="Has elegido femenino")
        
    else:
        etiqueta.config(text="Has elegido otras opciones")

Label(raiz,text="Genero: ").pack()
Radiobutton(raiz,text="Masculino",variable=opcion,value=1,command=imprimir).pack()
Radiobutton(raiz,text="Femenino",variable=opcion,value=2,command=imprimir).pack()
Radiobutton(raiz,text="Otras opciones",variable=opcion,value=3,command=imprimir).pack()

etiqueta=Label(raiz)
etiqueta.pack()

raiz.mainloop()