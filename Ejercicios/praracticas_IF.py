print("Programa evaluacion de alumnos")

nota_alumnos = input("introduce la nota de un alumno: ")

def evaluacion(nota):
    valoracion = "aprobado"
    if nota<5:
        valoracion = "Reprobado"
    return  valoracion


print(evaluacion(int(nota_alumnos)))


