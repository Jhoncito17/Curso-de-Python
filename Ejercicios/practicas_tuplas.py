mitupla=("Jose",1,16,1600,16)
print(mitupla)
print(mitupla.count(16))
print(len(mitupla))
#print(mitupla.index(1))


# tupla unitaria
Mitupla=("German",)
print(Mitupla)


#convertir una lista a tupla
milista1=["Django","rambo","tango","rango"]
mituplita=tuple(milista1)
print(mituplita)




#convertir una tupla a lista 
mitupla1=("Leonardo","donatelo","rafa","maiki")
milista=list(mitupla1)
print(milista)


#Desempaquetado de tupla
mitupla2 = ("Raul",57,1486,"Agosto")
nombre,edad,año,mes = mitupla2
print(mitupla2)
print(nombre)
print(edad)
print(año)
print(mes)