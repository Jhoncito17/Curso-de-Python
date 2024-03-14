def funcion_decorador(funcion_parametro):
    def funcion_interna(*args,**kwargs):
        #Acciones adicionales que decoran
        print("Se va realizar un calculo: ")
        
        funcion_parametro(*args,**kwargs)
        
        
        print("Se ha realizado el calculo con exito")

    return funcion_interna







@funcion_decorador
def suma(num1,num2,num3):
    print(num1+num2+num3)
   
    
@funcion_decorador   
def resta(num1,num2):
    print(num1-num2)
    
@funcion_decorador    
def potencia(base,exponente):
    print(pow(base,exponente)) 
    
    
suma(50,20,10)
resta(60,30)
potencia(base=5,exponente=3)