class carro():
    def __init__(self):
        self.__largochasis=249
        self.__anchochasis=150
        self.__ruedas=4
        self.__enmarcha=False 
        
    
    
    def arranchar(self,arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        
        if (self.__enmarcha and chequeo):
         return "el coche esta en marcha"
     
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. no podemos arrancar" 
        
        else:
            return "el coche esta parado"
        
    def estado(self):
        print("el coche tiene", self.__ruedas, " ruedas. un ancho de ", self.__anchochasis," y un largo de ", self.__largochasis)
    
    
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puerta="cerradas"
        
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puerta=="cerradas"):
            return True
        else:
            return False
        
    
    
        

Micarro=carro()
print(Micarro.arranchar(True))
Micarro.estado()
print("------------------------A continuacion creamos el segundo objeto-------------------")

Micarro2=carro()
print(Micarro2.arranchar(False))
Micarro2.estado()
