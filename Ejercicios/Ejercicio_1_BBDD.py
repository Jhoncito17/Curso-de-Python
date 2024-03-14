import sqlite3

MiConexion=sqlite3.connect("PrimeraBase")
MiCursor=MiConexion.cursor()

#MiCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULOS VARCHAR(50), PRECIO INTEGER, SELECCION VARCHAR(20) )")
#MiCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")


#VariosProductos=[
    
#    ("Camisa",15,"Deportes"),
#    ("Jarron",95,"ceramica"),
#    ("Carro",25,"JUgueteria")
#]

#MiCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", VariosProductos)

MiCursor.execute("SELECT * FROM PRODUCTOS")
Variosproductos=MiCursor.fetchall()

for productos in Variosproductos:
    print("El nombre del producto es: ", productos[0] , "El producto seleccionado es :", productos[2])




MiConexion.commit()






MiConexion.close()