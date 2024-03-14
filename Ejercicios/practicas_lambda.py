#def area_triaungulo(area,base):
#    return (area*base)/2

area_triangulo= lambda area,base: (area*base)/2

triangulo1=area_triangulo(12,3)
triangulo2=area_triangulo(3,6)

#print(triangulo1,triangulo2)





al_cubo= lambda numero:pow(numero,3)
al_cubo= lambda numero:numero**3

#print(al_cubo(2))




destacarValor= lambda Comision:"¡TIENES {} Dolares!".format(Comision)

comision_pedro=23341

print(destacarValor(comision_pedro))

