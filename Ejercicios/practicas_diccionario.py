midiccionario = {"Alemania": "Berlin","España" : "Madrid","Francia" : "Paris"}
midiccionario["Italia"] = "Lisboa"
print(midiccionario)
midiccionario["Italia"] = "Roma"
print(midiccionario)
del midiccionario["España"]
print(midiccionario)



#Usando tuplas para asignar las claves 
mitupla=("Alemania","Italia","Colombia")
midiccionario={mitupla[0]:"Berlin",mitupla[1]:"Roma",mitupla[2]:"Bogota"}


#Un Diccionario dentro de un diccionario
midiccionario1 = {23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillo":{"temporadas":[1991,1992,1993,1996]}}
print(midiccionario1.keys())
print(midiccionario1.values())
print(len(midiccionario1))