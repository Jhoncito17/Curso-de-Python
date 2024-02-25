i = 1

while i <= 10:
    print("ejecucion: " + str(i))
    i = i +1
    
print("termino la ejecucion")


edad = int(input("Introduce tu edad: "))

while edad < 0 or edad > 100:
    print("Has introducido mal la edad vuelve a intentarlo")
    edad = int(input("Introduce tu edad: "))
    
print("gracias por colaborar")
print("edad del aspirante ingresado: " + str(edad))


import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("introduce un numero por favor: "))

intento = 0

while numero<0:
    print("No se puede hallar valor negativo en la razi cuadrada")
    
    if intento==2:
        print("Has consumido demasiados intentos el programa a finalizado")
        break;
    
    numero=int(input("introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1
        
        
if intento<2:
    solucions=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucions))
    
        