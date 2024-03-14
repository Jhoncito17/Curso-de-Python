from io import open

archivos_texto=open("archivo.txt","r+")

lista_texto=archivos_texto.readlines();
lista_texto[1]=" esta nueva linea fue agregada desde el exterior \n"
archivos_texto.seek(0)
archivos_texto.writelines(lista_texto)

archivos_texto.close
