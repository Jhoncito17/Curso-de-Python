#def numeros_pares(num):
#    if num % 2 == 0:
#        return True
    
#numeros_lista=[12,456,8,6,89,13,71]    

#print(list(filter(lambda numeros_par: numeros_par%2==0,numeros_lista)))


class empleado:
    
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario 
    
    def __str__(self):
        
        return"{} trabaja como {} y tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
    
    
ListaEmpleado=[
    empleado("Juan"," Director",850000),
    empleado("ana"," Presidenta",950000),
    empleado("fredy"," repartidor",8500),
    empleado("sofia"," secretaria",5000),         
              
    ]

Salarios_Altos=filter(lambda empleado:empleado.salario>50000,ListaEmpleado)

for salarioss in Salarios_Altos:
    print(salarioss)