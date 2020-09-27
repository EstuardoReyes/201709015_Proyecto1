def lista(arch):
    archivo = open(arch)
    cadena = archivo.read()
    ultimo = len(cadena)
    print(cadena[0])
    print(cadena[ultimo-1])
    if(ord(cadena[0])==40 and ord(cadena[ultimo-1])==41): #Comprueba que el arreglo tenga inicio y fin
        lista = []
        return "q"
    else:
        print("Error 001 en el archivo ingresado")
#for w in range(0,2):
# if(1<2):
 #    print("c")
