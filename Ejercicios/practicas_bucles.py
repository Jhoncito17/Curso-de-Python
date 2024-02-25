for letra in "python":
    
    if letra=="h":
        continue

print("La letra es: " + letra)
    
    
nombre = "Armando mendoza"
contador = 0

for i in nombre:
    if i == " ":
        continue
    contador+=1
    
print(contador)



email=input("Introduce tu email: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)