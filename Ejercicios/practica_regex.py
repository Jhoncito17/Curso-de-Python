import re

codigo1="sdwsd3efwcqwxw71zzzzwssw"
codigo2="s71dwsd3efwcqwxw"
codigo3="dcecsxsx"

if re.search("71",codigo2):
    print("Hemos encontrado el numero")
        
else: 
    print("No lo hemos encontrado")




nombre1="Lara castillo"
nombre2="jose lopez"
nombre3="Jara reyes"

if re.match(".ara",nombre1,re.IGNORECASE):
    print("Hemos encontrado el nombre")
        
else: 
    print("No lo hemos encontrado")




















#ListaNombres = ["Ma.1",
#               "Se1",
#                "Ma2",
#                "Ba1",
#                "Ma:3",
#                "Va1",
#                "Va2",
#                "Ma4",
#                "MaA",
#                "Ma.5",
#                "MaB",
#                "Ma:c"]
#
#for palabra in ListaNombres:
#    if re.findall("Ma[.:]", palabra):
#        print(palabra)























#cadena="Vamos aprender expresiones regulares en python, python es un lenguaje de sintaxis sencilla"
#textobuscar="aprender"
#textoEncontrado=re.search(textobuscar,cadena)
#TEXTOBUSCAR="python"


#print(len(re.findall(TEXTOBUSCAR,cadena)))
#print(textoEncontrado.start())
#print(textoEncontrado.end())
#print(textoEncontrado.span())


#if re.search(textobuscar,cadena) is not None:
#    print("he encontrado el texto")
    
#else:
#    ("No he encontrado el texto")




#print(re.search("aprender",cadena))