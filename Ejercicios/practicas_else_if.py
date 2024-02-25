print("Verificacion de acceso")

edad_usuario= int(input("Introdusca su edad: "))

if edad_usuario<18:
    print("Eres menor de edad no puedes pasar")
    
elif edad_usuario>100:
   print("Edad incorrecta")
else:
    print("Eres mayor de edad puedes pasar")
    
    
    
    
print("Verificacion de nota")

nota_estudiante = int(input("Introdusca su nota: "))

if nota_estudiante<5:
    print("Insuficiente")

elif nota_estudiante<6:
    print("Suficiente")

elif nota_estudiante<7:
    print("Bien")
    
elif nota_estudiante<9:
    print("Notable")
    
else:
    print("Sobresaliente")