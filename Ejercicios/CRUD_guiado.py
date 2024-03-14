from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------Funciones--------------
def ConexionBBDD():
    Miconexion=sqlite3.connect("Usuarios")
    Micursor=Miconexion.cursor()
    
    try:
        Micursor.execute('''
            CREATE TABLE DATOSUSUARIO(
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOMBRE_USUARIO VARCHAR(50),
             PASSWORD VARCHAR (50),
             APELLIDO VARCHAR (20),
             DIRECCION VARCHAR (50),
             COMENTARIOS VARCHAR (100))
        ''')
    
        messagebox.showinfo("BBDD","BBDD creada con exito")           
    
    except:
        messagebox.showwarning("¡Atencion!","La BBDD ya existe")
        
    
def SalirApp():
    valor=messagebox.askokcancel("Salir","¿Deseas Salir de la aplicacion?")
    if valor==True:
        raiz.destroy()
        
    #valor=messagebox.askquestion("Salir","¿Deseas Salir de la aplicacion?")
    #if valor==YES:
        #raiz.destroy()   
    
    
def limpiarCampos():
    MiId.set("")
    MiNombre.set("")
    MiPassword.set("")
    MiApellido.set("")
    Midireccion.set("")
    Textocomentario.delete(1.0, END)

def crear():
    miconexion=sqlite3.connect("Usuarios")
    micursor=miconexion.cursor() 
    
    datos=MiNombre.get(),MiPassword.get(),MiApellido.get(),Midireccion.get(),Textocomentario.get("1.0",END)
    
    #micursor.execute("INSERT INTO DATOSUSUARIO VALUES(NULL, '"+ MiNombre.get() +
    #     "','" + MiPassword.get() +
    #     "','" + MiApellido.get() +   
    #     "','" + Midireccion.get() +
    #     "','" + Textocomentario.get("1.0",END) + "')")       
    
    micursor.execute("INSERT INTO DATOSUSUARIO VALUES(NULL,?,?,?,?,?)",(datos))
    
    miconexion.commit()
    
    messagebox.showinfo("BBDD","Registro insertado con exito")
    
    
def leer():
    miconexion=sqlite3.connect("Usuarios")
    micursor=miconexion.cursor() 
    micursor.execute("SELECT * FROM DATOSUSUARIO WHERE ID=" + MiId.get())
    
    Elusuario=micursor.fetchall()
     
    for usuario in Elusuario:
        MiId.set(usuario[0])
        MiNombre.set(usuario[1])
        MiPassword.set(usuario[2])
        MiApellido.set(usuario[3])
        Midireccion.set(usuario[4])
        Textocomentario.insert(1.0,usuario[5])
        
    miconexion.commit()
     
    
def actualizar():
    miconexion=sqlite3.connect("Usuarios")
    micursor=miconexion.cursor() 
    
    datos=MiNombre.get(),MiPassword.get(),MiApellido.get(),Midireccion.get(),Textocomentario.get("1.0",END)
    #micursor.execute("UPDATE DATOSUSUARIO SET NOMBRE_USUARIO='" + MiNombre.get()+
    #                 "',PASSWORD='" + MiPassword.get()+
    #                 "',APELLIDO='" + MiApellido.get()+
    #                 "',DIRECCION='" + Midireccion.get()+
    #                 "',COMENTARIOS='" + Textocomentario.get("1.0",END)+
    #                 "' WHERE ID=" + MiId.get())
    
    micursor.execute("UPDATE DATOSUSUARIO SET NOMBRE_USUARIO=?, PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?" + 
                     "WHERE ID=" + MiId.get(),(datos))
    #
    miconexion.commit()
    
    messagebox.showinfo("BBDD","Registro actualizado con exito")




def eliminar():
    miconexion=sqlite3.connect("Usuarios")
    micursor=miconexion.cursor()    
    micursor.execute("DELETE FROM DATOSUSUARIO WHERE ID="+ MiId.get())
    
    miconexion.commit() 
    
    messagebox.showinfo("BBDD","Registro se borro con exito")
    


raiz=Tk()
BarraMenu=Menu(raiz)
raiz.config(menu=BarraMenu,width=300,height=300)


bbdd=Menu(BarraMenu,tearoff=0)
bbdd.add_command(label="Conectar ",command=ConexionBBDD)
bbdd.add_command(label="Salir",command=SalirApp)


BorrarMenu=Menu(BarraMenu,tearoff=0)
BorrarMenu.add_command(label="Borrar campos",command=limpiarCampos)


crudMenu=Menu(BarraMenu,tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)



ayudaMenu=Menu(BarraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de....")


BarraMenu.add_cascade(label="BBDD",menu=bbdd)
BarraMenu.add_cascade(label="Borrar",menu=BorrarMenu)
BarraMenu.add_cascade(label="CRUD",menu=crudMenu)
BarraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#------------------COMIENZO DE CAMPO-------------------

Miframe=Frame(raiz)
Miframe.pack()

MiId=StringVar()
MiNombre=StringVar()
MiPassword=StringVar()
MiApellido=StringVar()
Midireccion=StringVar()



CuadroID=Entry(Miframe,textvariable=MiId)
CuadroID.grid(row=0,column=1,padx=10,pady=10)


CuadroNombre=Entry(Miframe,textvariable=MiNombre)
CuadroNombre.grid(row=1,column=1,padx=10,pady=10)
CuadroNombre.config(fg="red",justify="right")


CuadroPass=Entry(Miframe,textvariable=MiPassword)
CuadroPass.grid(row=2,column=1,padx=10,pady=10)
CuadroPass.config(show="*")


CuadroApellido=Entry(Miframe,textvariable=MiApellido)
CuadroApellido.grid(row=3,column=1,padx=10,pady=10)


CuadroDireccion=Entry(Miframe,textvariable=Midireccion)
CuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

Textocomentario=Text(Miframe)
Textocomentario.grid(row=5,column=1,padx=10,pady=10)
scrollvert=Scrollbar(Miframe, command=Textocomentario.yview)
scrollvert.grid(row=5,column=2,sticky=NSEW)

Textocomentario.config(yscrollcommand=scrollvert.set)



#---------------Comienzo de label----------------

idlabel=Label(Miframe,text="ID: ")
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombrelabel=Label(Miframe,text="Nombre: ")
nombrelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passlabel=Label(Miframe,text="Password: ")
passlabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)


apellidolabel=Label(Miframe,text="Apellido: ")
apellidolabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)


direccionlabel=Label(Miframe,text="Direccion: ")
direccionlabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)


comentariolabel=Label(Miframe,text="Comentario: ")
comentariolabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)


#--------------------Aqui los botones-----------------------
Miframe2=Frame(raiz)
Miframe2.pack()

Botoncrear=Button(Miframe2,text="Create", command=crear)
Botoncrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)


Botonleer=Button(Miframe2,text="Read",command=leer)
Botonleer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

Botonactualizar=Button(Miframe2,text="Update",command=actualizar)
Botonactualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

Botonborrar=Button(Miframe2,text="Delete",command=eliminar)
Botonborrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

raiz.mainloop()