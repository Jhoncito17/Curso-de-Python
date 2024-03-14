class persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
        
    def descripcion(self):
        print("Nombre: ",self.nombre, "edad: ", self.edad, "residencia: ", self.lugar_residencia)
        
class empleado(persona):
    def __init__(self,sueldo,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.sueldo=sueldo
        self.antiguedad=antiguedad
        
    def descripcion(self):
        super().descripcion()
        print("El sueldo es de: ",self.sueldo,"la antiguedad es: ", self.antiguedad)
        
        
antonio=empleado(1500,12,"antonio",45,12)
antonio.descripcion()
print(isinstance(antonio,empleado))
 
    