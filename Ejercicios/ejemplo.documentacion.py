from Modulos import Funciones_matematicas

class areas:
    """Esta clase calcula las areas de diferentes figuras geometricas"""
    
    
    def AreaCuadrado(lado):
     
       """Calcula el area de un cuadrado elevando al cuadrado el lado pasado por el perimtro"""
       return"El area del cuadrado es: " + str(lado*lado)
       


    def AreaTriangulo(base,altura):
        """Calcula el area de un triangulo utilizando los parametros base y altura"""
        return"El area del triangulo es: " + str((base*altura)/2)



#print(AreaCuadrado.__doc__)
help(Funciones_matematicas)