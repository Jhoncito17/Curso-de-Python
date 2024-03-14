class Carro():
    def desplazamiento(seft):
        print("me desplazo en cuatro ruedas")
        
        
class Moto():
    def desplazamiento(seft):
        print("me desplazo en dos ruedas")
        
        
class Camion():
    def desplazamiento(seft):
        print("me desplazo en seis ruedas")
        


def desplazamientovechiculo(vehiculo):
    vehiculo.desplazamiento()
    

Mivehiculo=Moto()

desplazamientovechiculo(Mivehiculo)
