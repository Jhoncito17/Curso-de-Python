import pickle

class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
        
    def acelera(self):
        self.acelera=True
        
    def frena(self):
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelarando: ", self.acelera, "\nFrenado: ", self.frena)
        
carro1=vehiculos("renault","megane")
carro2=vehiculos("mazda","MX5")
carro3=vehiculos("seat","leon")

carros=[carro1,carro2,carro3]

#fichero=open("Loscarros","wb")
#pickle.dump(carros,fichero)
#fichero.close()
#del(fichero)

fichero_carritos=open("Loscarros","rb")
MisCarros=pickle.load(fichero_carritos)
fichero_carritos.close()

for c in MisCarros:
    print(c.estado())