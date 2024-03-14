import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una nueva persona nueva con el nombre de : ", self.nombre)
        
    def __str__(self):
        return"{} {} {}".format(self.nombre, self.genero,self.edad)
    
class ListaPersonas:
    
    personas=[]
    
    def __init__(self):
        
        listadepersonas=open("ficheroExterno", "ab+")
        listadepersonas.seek(0)
        
        try:
            self.personas=pickle.load(listadepersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
            
        except:
            print("El fichero esta vacio")
            
        finally:
            listadepersonas.close()
            del(listadepersonas)

    def agregarpersonas(self,p):
        self.personas.append(p)
        self.guardarpersonasenficheroexterno()
        
    def mostrarpersonas(self):
        for p in self.personas:
            print(p)
            
    def guardarpersonasenficheroexterno(self):
        ListadePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,ListadePersonas)
        ListadePersonas.close()
        del(ListadePersonas)
        
    def mostrarficheroexterno(self):
        print("La informacion del infierno externo es la siguiente: ")
        for p in self.personas:
            print(p)
            
Milista=ListaPersonas()
persona=Persona("jose","masculino",29)
Milista.agregarpersonas(persona)
Milista.mostrarficheroexterno