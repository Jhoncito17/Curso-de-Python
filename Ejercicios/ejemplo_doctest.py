def compruebaEmail(EmailUsuario):
    
    """
    La funcion compruebaEmail evalua un mail recibido en busca de la @
    si tiene una @ es correcto si tiene mas de una @ es incorrecto y si
    la arroba @ esta al final es incorrecto
    
    >>> compruebaEmail('Jhon@python.com')
    True
    
    >>> compruebaEmail('Jhonpython.com@')
    False
    
    >>> compruebaEmail('Jhonpython.com')
    False
    
    >>> compruebaEmail('Jhon@python@.com')
    False
    
    """
    
    
    
    arroba=EmailUsuario.count('@')
    
    if (arroba!=1 or EmailUsuario.rfind('@')==(len(EmailUsuario)-1) or EmailUsuario.find('@')==0):
        return False
        
    else:
         return True
        
        
import doctest
doctest.testmod()


    