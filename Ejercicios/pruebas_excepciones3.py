def EvaluaEdad(edad):
    if edad<0:
        raise ValueError("No se permiten valores negativos ")    
    if edad<20:
        print("eres muy joven")
    elif edad<40:
        print("ya estas un poquito viejo")
    elif edad<60:
        print("ya tienes edad")
    elif edad<100:
        print("estas pasado de siglos")
        
print(EvaluaEdad(-203))









import math 
def calcularraiz(num1):
     if num1<0:
         raise ValueError("El numero no puede ser negativo")
     else:
         return math.sqrt(num1)
     
op=int(input("introduce un numero: "))

try:
    print(calcularraiz(op))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    
print("programa terminado")