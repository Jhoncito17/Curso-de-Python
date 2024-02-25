for i in [1,2,3,4,5]:
    print("Hola")
    

for estaciones in ["Verano","Invierno","Otoño","Primavera"]:
   print(estaciones)
    
    
    
contador = 0
miemail=input("Introduce tu email: ")


for i in miemail:
    if (i == "@" or i =="."):
        contador=contador + 1

if contador<=2:
    print("Correo valido")

else:
    print("Correo invalido")
    
    
    
    
 #Ejemplo con range   
for i in range(5):
    print("Hola Como va todo")
    



for i in range(2,100,5):
    print(f"El valor de la variable {i}")







valido = False
email=input("Introduce tu email: ") 

for i in range(len(email)):
    if email[i]=="@":
        valido=True
        
if valido:
    print("correo correcto")
    
else:
    print("correo incorrecto")