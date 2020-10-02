from asdf import (lexemas, lista, listaComandos)
import asdf
listaCategorias = []
color = "\033[0;37m"
listaSeleccionada = []
def Script(archivo):
    asdf.AFD(archivo)
    com = listaComandos
    for x in range(1,len(com)):
        comando = com[x]
        salir = False
        y = 0
        while salir == False:
            if(comando[y] == 'CREATE'):  #COMANDO CREATE
                y = y +1
                if(comando[y] == 'SET'):
                    y = y + 1
                    nombrelista = comando[y]
                    v=0
                    encotrado = False
                    if(len(listaCategorias) == 0):
                        diccionario = {comando[y]}
                        listaCategorias.append(diccionario)
                        print(color+'lista '+comando[y]+' creada')
                        salir=True
                    else:
                        while(encotrado == False and v<len(listaCategorias)): 
                            listaClave = listaCategorias[v]
                            if(nombrelista in listaClave):
                                print("Set "+nombrelista+" ya existente")
                                encotrado = True
                            v=v+1
                        if encotrado == False:
                            diccionario = {comando[y]}
                            listaCategorias.append(diccionario)
                            print(color+'lista '+comando[y]+' creada')
                else:
                    print(color+"comando CREATE no es valido")
                salir = True
#########################CREATE TERMINADO#####################################
            elif(comando[y] == 'LOAD'):
                y = y + 1
                if(comando[y] == 'INTO'):
                    y = y + 1
                    nombrelista = comando[y]
                    v=0
                    if(len(listaCategorias) == 0):
                        print(color+"No existe lista seleccionada")
                        salir=True
                    else:
                        for v in range(0,len(listaCategorias)):
                            listaClave= listaCategorias[v]
                            if(nombrelista in listaClave):
                                encotrado = True
                                y = y+1
                                if(comando[y] == 'FILES'):
                                    y = y + 1
                                    if(len(comando)==3):
                                        print(color+"No hay archivo seleccionado para agregar")
                                    else:
                                        listaFinal = []
                                        for a in range(4,len(comando)):
                                            asdf.AFD(comando[a]) #implementar try chatcj
                                            li = lista
                                            for b in range(0,len(li)):
                                                listaFinal.append(li[b])
                                        listaClave.clear
                                        listaClave = {nombrelista:listaFinal}
                                        #del listaCategorias[v][nombrelista]
                                        listaClave[nombrelista]=listaFinal     ###problema aqui
                                        listaCategorias[v] = listaClave
                                        print(listaCategorias[v])   
                                        print(len(listaCategorias))      
                                else:
                                    print(color+"Comando LOAD INTO no valido")
                        if(encotrado == False):
                            print(color+"Nombre de lista no existe")
                else:
                    print(color+"Comando LOAD no es valido")
                salir = True
#########################LOAD TERMINADO ####################################          
            elif(comando[y] == 'USE'):
                y = y + 1
                if(comando[y] == 'SET'):
                    y = y + 1
                    nombrelista = comando[y]
                    v=0
                    if(len(listaCategorias) == 0):
                        print(color+"No existe lista seleccionada")
                        salir=True
                    else:
                        for v in range(0,len(listaCategorias)):
                            listaClave= listaCategorias[v]
                            if(nombrelista in listaClave):
                                encotrado = True
                                listaSeleccionada = listaClave[nombrelista]
                                print(color+"Lista "+nombrelista+" Seleccionada")
                        if(encotrado == False):
                            print(color+"Nombre de lista no existe")
                else:
                    print("Comando USE no valido")            
                salir = True
###########################USE TERMINADO#############################################
            elif(comando[y] == 'SELECT'):
                pri
                salir = True
            elif(comando[y] == 'LIST'):
                print(5)
                salir = True
            elif(comando[y] == 'PRINT'):
                print(6)
                salir = True
            elif(comando[y] == 'MAX'):
                print(7)
                salir = True
            elif(comando[y] == 'MIN'):
                print(8)
                salir = True
            elif(comando[y] == 'SUM'):
                print(9)
                salir = True
            elif(comando[y] == 'COUNT'):
                print(10)
                salir = True
            elif(comando[y] == 'REPORT'):
                print(11)
                salir = True
            else:
                q=0
                aux =''
                for q in range(0,len(comando)):
                    aux = aux+comando[q]+" "
                print(color+"Comando "+aux+"No reconocido")
                salir = True      
