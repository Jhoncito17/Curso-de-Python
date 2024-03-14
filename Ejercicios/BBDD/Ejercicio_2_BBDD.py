import sqlite3

MiConexion=sqlite3.connect("GestionProductos")
MiCursor=MiConexion.cursor()


#MiCursor.execute("""
# CREATE TABLE PRODUCTOS(
    # CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    # NOMBRE_ARTICULOS VARCHAR(50), 
    # PRECIO INTEGER, 
    # SELECCION VARCHAR(20))
    # 
    # 
    # """)

#productos=[
   # ("AR01","Pelota",21,"Deportes")    
   # ("AR02","pantalon",123,"Ropa")  
   # ("AR03","martillo",34,"Ferreteria")  
   # ("AR04","jarron",65,"Ceramica")   
#]


#MiCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)"productos)


#MiCursor.execute('''
#     CREATE TABLE PRODUCTOS (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NOMBRE_ARTICULOS VARCHAR(50) UNIQUE, 
#     PRECIO INTEGER, 
#     SELECCION VARCHAR(20))
#''')

#productos=[
#    ("Pelota", 21, "Deportes"),    
#    ("pantalon", 123, "Ropa"),  
#    ("martillo", 34, "Ferreteria"),  
#    ("jarron", 65, "Ceramica"),
#    ("pantalones",56,"Ropa")   
#]


#MiCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)


#-----------------PARA VER LOS ARTICULOS DE LA SECCION ROPA-------------
#MiCursor.execute("SELECT * FROM PRODUCTOS WHERE SELECCION='Ropa'")
#productos=MiCursor.fetchall()
#print(productos)


#----------------PARA ACTUALIZAR USAMOS LA INSTRUCCION UPDATE----------------
MiCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULOS='Pelota'")

#----------------PARA ELIMINAR USAMOS LA INSTRUCCION DELETE----------------
MiCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


MiConexion.commit()
MiConexion.close()