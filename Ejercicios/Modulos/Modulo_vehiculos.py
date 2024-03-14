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
  
class furgoneta(vehiculos): 
    def carga(self,cargar):
        self.cargado=True
        if self.cargado:
            return"La furgoneta esta cargada"
        else:
            return"la furgoneta no esta cargada"
  
   
class moto(vehiculos):
    hcaballito=""
    def hcaballito(self):
        self.hcaballito="Haciendo un caballito"
        
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelarando: ", self.acelera, "\nFrenado: ", self.frena, "\n", self.hcaballito)   


class Velectricos(vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
        
    def cargaEnergia(self):
        self.cargando=True


