from tkinter import *
from tkinter import messagebox


def InfoAdicional():
    messagebox.showinfo("Procesador Jhon","Procesador de texto 2024")
    
def AvisoLicencia():
    messagebox.showwarning("Licencia","Producto Bajo licencia GNU")
    
def SalirApp():
    #valor=messagebox.askquestion("Salir","¿Deseas Salir de la aplicacion?")
    valor=messagebox.askokcancel("Salir","¿Deseas Salir de la aplicacion?")
    if valor==True:
        raiz.destroy()
        
def CerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar el documento en estos momentos,Documento bloqueado")
    
    if valor==False:
     raiz.destroy()
    
    

raiz=Tk()
BarraMenu=Menu(raiz)
raiz.config(menu=BarraMenu,width=600,height=350)


ArchivoMenu=Menu(BarraMenu,tearoff=0)
ArchivoMenu.add_command(label="Nuevo")
ArchivoMenu.add_command(label="Guardar")
ArchivoMenu.add_command(label="Guardar Como")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Cerrar",command=CerrarDocumento)
ArchivoMenu.add_command(label="Salir",command=SalirApp)


ArchivoEdicion=Menu(BarraMenu,tearoff=0)
ArchivoEdicion.add_command(label="Cortar")
ArchivoEdicion.add_command(label="Copiar")
ArchivoEdicion.add_command(label="Pegar")


ArchivoHerramientas=Menu(BarraMenu,tearoff=0)


ArchivoAyuda=Menu(BarraMenu,tearoff=0)
ArchivoAyuda.add_command(label="Licencia", command=AvisoLicencia)
ArchivoAyuda.add_command(label="Acerca de....", command=InfoAdicional)



BarraMenu.add_cascade(label="Archivo",menu=ArchivoMenu)
BarraMenu.add_cascade(label="Edicion",menu=ArchivoEdicion)
BarraMenu.add_cascade(label="Herramienta",menu=ArchivoHerramientas)
BarraMenu.add_cascade(label="Ayuda",menu=ArchivoAyuda)



raiz.mainloop()