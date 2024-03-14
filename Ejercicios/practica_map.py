class empleado:
    
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario 
    
    def __str__(self):
        
        return"{} trabaja como {} y tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
    
    
ListaEmpleado=[
    empleado("Juan"," Director",6700),
    empleado("ana"," Presidenta",7500),
    empleado("fredy"," repartidor",2100),
    empleado("sofia"," secretaria",2150),         
              
    ]

def calculo_comision(empleado):
    if(empleado.salario<=3000):
     empleado.salario=empleado.salario*1.03
    return empleado


ListaEmpleadosComision=map(calculo_comision,ListaEmpleado)

for empleado in ListaEmpleadosComision:
    print(empleado)