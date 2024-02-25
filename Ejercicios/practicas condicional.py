edad = -7

if 0<edad<100:
    print("Edad correcta")
    
else:
    print("Edad incorrecta")
    
    
    
salario_presidente = int(input("Ingrese el salario del presidente: "))
print("El salario del presidente es: " + str(salario_presidente))


salario_director = int(input("Ingrese el salario del director: "))
print("El salario del director es: " + str(salario_director))


salario_jefe_area = int(input("Ingrese el salario del jefe de area: "))
print("El salario del jefe de area es: " + str(salario_jefe_area))


salario_administrativo = int(input("Ingrese el salario del administrativo: "))
print("El salario del administrativo es: " + str(salario_administrativo))


if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todos bien con los salarios de la empresa")
    
else:
    print("Algo esta mal con los salarios de la empresa")
    






print("programa de becas para el 2024")

distancia_escuela = int(input("Introduce la distancia a la escuela: "))
print(distancia_escuela)


numero_hermanos = int(input("Ingresa tu numero de hermanos: "))
print(numero_hermanos)


salario_anual = int(input("Ingrese el salario anual bruto: "))
print(salario_anual)

if distancia_escuela>40 and numero_hermanos>2 or salario_anual<=20000:
    print("Tienes derecho a una beca")
    
else:
    print("NO tienes derecho a beca")







print("Materias optativas año 2024")
print("Asinaturas optativas: empanada 2 - sancocho coperativo  -  salchipapa teorica")
opcion = input("Escoge una materia optativa: ")

asignatura = opcion.lower()

if asignatura in ("empanada 2","sancocho coperativo","salchipapa teorica"):
    print("Materia optativa escogida " + asignatura)
    
else:
    print("Materia optativa incorrecta")
    


