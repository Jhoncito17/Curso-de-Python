from tkinter import *
from tkinter import filedialog


raiz=Tk()

def AbrirArchivo():
    fichero=filedialog.askopenfile(title="Abrir",initialdir="Documentos",filetypes=(("Fichero excel",".xlsx"),("Fichero de textos",".txt"),("Todos los archivos","*.*")))
    
    print(fichero)
    
Button(raiz,text="Abrir Fichero",command=AbrirArchivo).pack()


raiz.mainloop()