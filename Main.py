from asdf import (lexemas, lista, listaComandos)
import asdf
#color = "\033[0;35m"
#print(color+"hola y adios")
ar = "Scrip.sqin"
asdf.AFD(ar)
lex = lexemas
com = listaComandos
for x in range(1,len(com)):
    print(1)
    comando = com[x]
    for y in range (0,len(com[x])):
        print(comando[y])
asdf.AFD("Archivo.aon")
lis = lista
print(lis)