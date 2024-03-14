import math

def raizCuadrada(listaNumeros):



   """
   La funcion devuelve una lista con la raiz cuadrada de los elementos numericos
   pasados por parametros en otra lista


   >>> lista=[]
   >>> for i in [4,9,16]:
   ... raizCuadrada(lista)
   [2.0, 3.0, 4.0]

   >>> lista=[]
   >>> fpr i in [4,9,16,50,78,90,125]:
   ... raizCuadrada(lista)
   Traceback (most recent call last):
     ...
   ValueError: math domain error

   """

   return [math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9,16,25,36]))

import doctest
doctest.testmod()