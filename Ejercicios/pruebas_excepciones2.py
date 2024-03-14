def divide():
    try:
        op=float(input("Introduce el primer valor: "))
        op1=float(input("Introduce el segundo valor: "))
    
        print("el resultado es: " + str(op/op1))
        
    except ValueError:
       print("valor incorrecto")
       
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        print("fin de eduacion")
    
divide()