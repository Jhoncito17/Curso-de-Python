from tkinter import *

raiz=Tk()
raiz.title("Ejemplo con check button")

playa=IntVar()
montaña=IntVar()
turismorural=IntVar()

def opcionesviaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+="  Playa" 
        
    if(montaña.get()==1):
        opcionEscogida+="  Montaña" 
        
    if(turismorural.get()==1):
        opcionEscogida+="  Turismo rural" 
        
    textofinal.config(text=opcionEscogida)


frame=Frame(raiz)
frame.pack()

Label(frame,text="Elige destinos: ",width=50).pack()


Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesviaje).pack()
Checkbutton(frame,text="Montaña",variable=montaña,onvalue=1,offvalue=0,command=opcionesviaje).pack()
Checkbutton(frame,text="Turismo rural",variable=turismorural,onvalue=1,offvalue=0,command=opcionesviaje).pack()

textofinal=Label()
textofinal.pack()

raiz.mainloop()