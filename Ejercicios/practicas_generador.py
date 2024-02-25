def generadorpares(limite):
    num=1
    
    
    while num<limite:
        yield num*2
        num=num+1

retornavalores=generadorpares(10)
    
print(next(retornavalores))
print("Aqui podria ur mas codigo...")

print(next(retornavalores))
print("Aqui podria ur mas codigo...")


