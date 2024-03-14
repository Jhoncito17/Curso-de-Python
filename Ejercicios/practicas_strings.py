Edad=input("Introduce tu edad: ")

while (Edad.isdigit()==False):
    print("Incorrecto vuelve a introducir tu edad")
    Edad=input("Introduce tu edad: ")
    
if (int(Edad)<18):
    print("no puedes pasar")
else:
    print("puedes pasar")