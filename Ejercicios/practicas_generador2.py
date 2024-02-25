def devuelveciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento
        
retornaciudades=devuelveciudades("Cali","Bogota","Medellin")

print(next(retornaciudades))
print(next(retornaciudades))
            