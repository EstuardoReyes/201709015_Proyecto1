from asdf import (lexemas, lista, listaComandos)
import asdf
import webbrowser
listaCategorias = []
color = "\033[0;37m"
listaSeleccionada = []
def Script(archivo):
    asdf.AFD(archivo)
    color="\033[0;37m"
    com = listaComandos
    listaSeleccionada = []
    lexemaFinal = []
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
                                print(color+"Set "+nombrelista+" ya existente")
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
                                            la = lexemas
                                            for c in range(0,len(la)):
                                                lexemaFinal.append(la[c])

                                            for b in range(0,len(li)):
                                                listaFinal.append(li[b])
                                                
                                        listaClave.clear
                                        listaClave = {nombrelista:listaFinal}
                                        #del listaCategorias[v][nombrelista]
                                        listaClave[nombrelista]=listaFinal     ###problema aqui
                                        listaCategorias[v] = listaClave     
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
                y = y + 1
                if(listaSeleccionada == []):
                    print("Error no existe ninguna lista seleccionada")
                else:
                    numWhere = 0
                    imprimir = []
                    out = False
                    w = 1
                    while out == False:
                        if(comando[w]=='WHERE'):
                            numWhere = w
                            out = True
                        else:
                            imprimir.append(comando[w])
                            w = w + 1
                        if(w == len(comando)):
                            out = True
                            print("Comando WHERE no encontrado")
                    if(out == True):
                        out = False
                        encontrado = False
                        q = numWhere + 1
                        while out == False:
                            if(comando[q]=='REGEX'):
                                out = True
                                encontrado = True
                            if(q == len(comando)-1):
                                out = True
                            else:
                                q = q + 1
                        if encontrado == True:
                            #En el comando existe el pedido regex a partir de aqui debo seguir desarrollando la busqueda
                            nombreClave = comando[numWhere+1]
                            inicio = numWhere + 3
                            yaImprimida = []
                            i = 1
                            nuevaLista = listaSeleccionada
                            for r in range(inicio,len(comando)):
                                for e in range(0,len(nuevaLista)):
                                    if nombreClave in nuevaLista[e]:
                                        if comando[r][0] == '^':
                                            comparativa  = comando[r][1]
                                            if nuevaLista[e].get(nombreClave)[0] == comparativa:
                                                yaImprimida.append(e)
                                                print("Registro "+str(i))
                                                new = list(nuevaLista[e])           
                                                i = i + 1
                                                if(comando[1] == '*'):
                                                    for u in range(0,len(new)):
                                                        print(color+new[u]+": "+nuevaLista[e].get(new[u]))
                                                else:
                                                    for u in range(0,len(imprimir)):
                                                        print(color+imprimir[u]+": "+nuevaLista[e].get(imprimir[u]))
                                        else:
                                            if(comando[r][len(comando[r])-1]=='+'):
                                                palabra = nuevaLista[e].get(nombreClave)
                                                w = 0
                                                v = 0
                                                salir = False
                                                while salir == False:
                                                    if(palabra[w] == comando[r][v]):
                                                        v = v + 1
                                                        t = w + 1
                                                        salida = False
                                                        while salida == False:
                                                            if(comando[int(r)][int(v)] == '+' or comando[int(r)][int(v)] == '.'):
                                                                yaImprimida.append(e)
                                                                print(color+"Registro "+str(i))
                                                                new = list(nuevaLista[e])  
                                                                salir = True         
                                                                i = i + 1
                                                                if(comando[1] == '*'):
                                                                    for u in range(0,len(new)):
                                                                        print(color+new[u]+": "+nuevaLista[e].get(new[u]))
                                                                else:
                                                                        for u in range(0,len(imprimir)):
                                                                            print(color+imprimir[u]+": "+nuevaLista[e].get(imprimir[u]))
                                    
                                                            if(palabra[t] == comando[r][v]):
                                                                v = v + 1
                                                                t = t + 1
                                                            else:
                                                                salida = True
                                                    if(w == len(palabra)-1):
                                                        salir = True
                                                    else:
                                                        w = w + 1    
                                            if(comando[r][len(comando[r])-1]=='*'):
                                                palabra = nuevaLista[e].get(nombreClave)
                                                w = 0
                                                v = 0
                                                salir = False
                                                while salir == False:
                                                    if(palabra[w] == comando[r][v]):
                                                        v = v + 1
                                                        t = w + 1
                                                        salida = False
                                                        while salida == False:
                                                            if(comando[int(r)][int(v)] == '*' or comando[int(r)][int(v)] == '.'):
                                                                yaImprimida.append(e)
                                                                print(color+"Registro "+str(i))
                                                                new = list(nuevaLista[e])  
                                                                salir = True         
                                                                i = i + 1
                                                                if(comando[1] == '*'):
                                                                    for u in range(0,len(new)):
                                                                        print(color+new[u]+": "+nuevaLista[e].get(new[u]))
                                                                else:
                                                                        for u in range(0,len(imprimir)):
                                                                            print(color+imprimir[u]+": "+nuevaLista[e].get(imprimir[u]))
                                    
                                                            if(palabra[t] == comando[r][v]):
                                                                v = v + 1
                                                                t = t + 1
                                                            else:
                                                                salida = True
                                                    if(w == len(palabra)-1):
                                                        salir = True
                                                    else:
                                                        w = w + 1    
                                            if(comando[r][len(comando[r])-1]=='?'):
                                                palabra = nuevaLista[e].get(nombreClave)
                                                w = 0
                                                v = 0
                                                salir = False
                                                while salir == False:
                                                    if(palabra[w] == comando[r][v]):
                                                        v = v + 1
                                                        t = w + 1
                                                        salida = False
                                                        while salida == False:
                                                            if(comando[int(r)][int(v)] == '?' or comando[int(r)][int(v)] == '.'):
                                                                yaImprimida.append(e)
                                                                print(color+"Registro "+str(i))
                                                                new = list(nuevaLista[e])  
                                                                salir = True         
                                                                i = i + 1
                                                                if(comando[1] == '*'):
                                                                    for u in range(0,len(new)):
                                                                        print(color+new[u]+": "+nuevaLista[e].get(new[u]))
                                                                else:
                                                                        for u in range(0,len(imprimir)):
                                                                            print(color+imprimir[u]+": "+nuevaLista[e].get(imprimir[u]))
                                    
                                                            if(palabra[t] == comando[r][v]):
                                                                v = v + 1
                                                                t = t + 1
                                                            else:
                                                                salida = True
                                                    if(w == len(palabra)-1):
                                                        salir = True
                                                    else:
                                                        w = w + 1              
                                        
                                if yaImprimida != []:
                                    for u  in range(0,len(yaImprimida)):
                                        nuevaLista.pop(yaImprimida[u]-u)  
                                yaImprimida = []                              
                        else:
                            y = numWhere + 1
                            clave = comando[y]
                            accion = comando[y+1]
                            valor = comando[y+2]
                            y = y + 3
                            if y < len(comando):
                                expresion = comando[y]
                                clave1 = comando[y+1]
                                accion1 = comando[y+2]
                                valor1 = comando[y+3]
                                e = 1
                                for t in range(0,len(listaSeleccionada)):
                                    if(clave in listaSeleccionada[t] and clave1 in listaSeleccionada[t]):
                                        if(expresion == 'AND'):
                                            # < 
                                            if(accion == '<' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) and (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '<' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) and (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '<' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) and (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) and (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '<' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) and (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) and (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # <= 
                                            if(accion == '<=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) and (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '<=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) and (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '<=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) and (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) and (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '<=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) and (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) and (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # >
                                            if(accion == '>' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) and (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '>' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) and (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '>' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) and (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) and (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '>' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) and (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) and (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            #  >= 
                                            if(accion == '>=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) and (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '>=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) and (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '>=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) and (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) and (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '>=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) and (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) and (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # =   
                                            if(accion == '=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) and (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) and (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) and (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) and (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) and (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) and (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) and (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) and (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) and (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) and (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                               print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) and (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # !=
                                            if(accion == '!=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) and (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) and int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) and (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '!=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) and (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) and int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) and (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '!=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) and (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) and int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) and (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '!=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) and (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) and int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) and (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '!=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) and int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) and (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '!=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) and (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) and int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                               print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) and (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                        if(expresion == 'OR'):
                                            # < 
                                            if(accion == '<' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) or (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '<' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) or (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '<' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) or (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) or (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '<' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) or (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # <= 
                                            if(accion == '<=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '<=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '<=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '<=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) or (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # >
                                            if(accion == '>' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) or (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or (listaSeleccionada[t].get(clave1)) < (valor1) ):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '>' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) or (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '>' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) or (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) or (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '>' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) or (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            #  >= 
                                            if(accion == '>=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) or (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '>=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) or (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '>=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) or (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) or (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '>=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print("Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) or (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # =   
                                            if(accion == '=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) or (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) or (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) or (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) or (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '=' and accion1 == '>'):
                                                
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                  
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) or (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) or (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) or (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) or (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave1) == (valor1)) or int(listaSeleccionada[t].get(clave)) == int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) or (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                               print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) or (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # !=
                                            if(accion == '!=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) or (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) or int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) or (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '!=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) or (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) or int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if (digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) or (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '!=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) or (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) or int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) or (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '!=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) or (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) or int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) or (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print("Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '!=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) or int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) or (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '!=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) or int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                               print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) or (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                        if(expresion == 'XOR'):
                                            # < 
                                            if(accion == '<' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) != (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '<' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) != (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '<' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) != (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) < int(valor) != (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '<' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor) != (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) < (valor)) != (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # <= 
                                            if(accion == '<=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) != (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '<=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) != (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '<=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor) != (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) <= int(valor)!= (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '<=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '<=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor) or (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) <= (valor)) != (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # >
                                            if(accion == '>' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) != (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '>' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) != (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '>' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) != (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) > int(valor) != (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '>' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor) != (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) > (valor)) != (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            #  >= 
                                            if(accion == '>=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) != (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '>=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) != (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '>=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) != (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) >= int(valor) != (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false') or (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '>=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '>=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor) != (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito == 'true' or digito == 'false'):
                                                        print(color+"Opcion 1 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) >= (valor)) != (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # =   
                                            if(accion == '=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) != (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) != (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) != (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) != (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) != (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) != (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) == int(valor) != (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) == (valor)) != (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) != (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor) != (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) == (valor)) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                               print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) == (valor)) != (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            # !=
                                            if(accion == '!=' and accion1 == '<'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) != (listaSeleccionada[t].get(clave1) < (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) != int(listaSeleccionada[t].get(clave1)) < int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) != (listaSeleccionada[t].get(clave1)) < (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                            if(accion == '!=' and accion1 == '<='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) != (listaSeleccionada[t].get(clave1) <= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) != int(listaSeleccionada[t].get(clave1)) <= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if (digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) != (listaSeleccionada[t].get(clave1)) <= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))   
                                            if(accion == '!=' and accion1 == '>'):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) != (listaSeleccionada[t].get(clave1) > (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) != int(listaSeleccionada[t].get(clave1)) > int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) != (listaSeleccionada[t].get(clave1)) > (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '!=' and accion1 == '>='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print(color+"Opcion 2 no admitida")
                                                    else:
                                                        if(int(listaSeleccionada[t].get(clave)) != int(valor) != (listaSeleccionada[t].get(clave1) >= (valor1))):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) != int(listaSeleccionada[t].get(clave1)) >= int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(digito1 == 'true' or digito1 == 'false'):
                                                        print("Opcion 2 no admitida")
                                                    else:
                                                        if((listaSeleccionada[t].get(clave) != (valor)) != (listaSeleccionada[t].get(clave1)) >= (valor1)):
                                                            new = list(listaSeleccionada[t])
                                                            print(color+"Registro "+str(e))
                                                            e = e + 1
                                                            if(comando[1] == '*'):
                                                                for u in range(0,len(new)):
                                                                    print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                            else:
                                                                for u in range(0,len(imprimir)):
                                                                    print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))    
                                            if(accion == '!=' and accion1 == '='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != (listaSeleccionada[t].get(clave1) == (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) != int(listaSeleccionada[t].get(clave1)) == int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) != (listaSeleccionada[t].get(clave1)) == (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                            if(accion == '!=' and accion1 == '!='):
                                                digito = valor
                                                digito1 = valor1  
                                                  # numero y numero
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' and ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # numero y letra
                                                if((ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-') and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 9122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor) != (listaSeleccionada[t].get(clave1) != (valor1))):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y numero
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 48 and ord(digito1[0]) <= 57 or digito1[0] == '-')): # es un numero
                                                    if((listaSeleccionada[t].get(clave) != (valor)) != int(listaSeleccionada[t].get(clave1)) != int(valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                               print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                # letra y letra
                                                if((ord(digito[0]) >= 65 and ord(digito[0]) <= 90 or ord(digito[0]) >= 97 and ord(digito[0]) <= 122 or digito[0] == 'Ñ' or digito[0] == 'ñ' ) and (ord(digito1[0]) >= 65 and ord(digito1[0]) <= 90 or ord(digito1[0]) >= 97 and ord(digito1[0]) <= 122 or digito1[0] == 'Ñ' or digito1[0] == 'ñ' )): # es un numero
                                                     if((listaSeleccionada[t].get(clave) != (valor)) != (listaSeleccionada[t].get(clave1)) != (valor1)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))  
                                        
                            else:
                                e = 1
                                for t in range(0,len(listaSeleccionada)):
                                    if(clave in listaSeleccionada[t]):
                                        if(accion == '<'):
                                            if(comando[1] == '*'):
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) < (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                            else:
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) < int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(imprimir)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) < (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                        if(accion == '<='):
                                            if(comando[1] == '*'):
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) <= (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                            else:
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) <= int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(imprimir)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) <= (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                        if(accion == '>'):
                                            if(comando[1] == '*'):
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) > (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                            else:
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) > int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(imprimir)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) > (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                        if(accion == '>='):
                                            if(comando[1] == '*'):
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) >= (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                            else:
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) >= int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(imprimir)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) >= (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                        if(accion == '='):
                                            if(comando[1] == '*'):
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    if(listaSeleccionada[t].get(clave) == (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) == (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                            else:
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) == int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(imprimir)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    if((listaSeleccionada[t].get(clave)) == (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) == (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                        if(accion == '!='):
                                            if(comando[1] == '*'):
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) != (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                            else:
                                                digito = valor
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ): # es un numero
                                                    if(int(listaSeleccionada[t].get(clave)) != int(valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(imprimir)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                                                elif(valor == 'True' or valor == 'False'): #valor bool
                                                    print(color+"Comando no admitido")
                                                else: # es letra
                                                     if((listaSeleccionada[t].get(clave)) != (valor)):
                                                        new = list(listaSeleccionada[t])
                                                        print(color+"Registro "+str(e))
                                                        e = e + 1
                                                        for u in range(0,len(new)):
                                                            print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))
                salir = True
            elif(comando[y] == 'LIST'):
                y = y + 1
                if(comando[y]== 'ATTRIBUTES'):
                    for a  in range(0,len(listaSeleccionada)):
                        t = a + 1
                        print(color+'Registro: '+str(t))
                        l = listaSeleccionada[a]
                        claves = l.keys()
                        for clave in l.keys():
                            print(color+clave)
                else:
                    print(color+"Comando LIST no valido")
                salir = True
######################## LIST TERMINADO ####################################################3
            elif(comando[y] == 'PRINT'):
                y = y + 1
                if(comando[y]=='IN'):
                    y = y + 1
                    if(comando[y]=='RED'):
                        color = "\033[0;31m"
                    elif(comando[y]=='GREEN'):
                        color = "\033[0;32m"
                    elif(comando[y]=='YELLOW'):
                        color = "\033[0;33m"
                    elif(comando[y]=='BLUE'):
                        color = "\033[0;34m"
                    elif(comando[y]=='PINK'):
                        color = "\033[0;35m"
                    elif(comando[y]=='ORANGE'):
                        color = "\033[38:5:202m"
                    else:
                        print("Color no valido")
                else: 
                    print("Comando PRINT no valido")
                salir = True
############################COLOR TERMINADO#################################################
            elif(comando[y] == 'MAX'):
                y = y + 1
                nombrelista = comando[y]
                v=0
                if(len(listaSeleccionada) == 0):
                    print(color+"No existe lista seleccionada")
                    salir=True
                else:
                    for v in range(0,len(listaCategorias)):
                        listaClave = listaSeleccionada[v]
                        if(nombrelista in listaClave):
                            encotrado = True
                            for numPasada in range(len(listaSeleccionada)-1,0,-1):
                                for i in range(numPasada):
                                    digito = listaSeleccionada[i].get(comando[y])
                                    if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                        # true es un numero
                                        num1 = listaSeleccionada[i].get(comando[y])
                                        num2 = listaSeleccionada[i+1].get(comando[y])
                                        if(int(num1) > int(num2)):
                                            temp = listaSeleccionada[i]
                                            listaSeleccionada[i] = listaSeleccionada[i+1]
                                            listaSeleccionada[i+1] = temp
                                    else:
                                        letra1 = (listaSeleccionada[i].get(comando[y]))
                                        letra2 = (listaSeleccionada[i+1].get(comando[y]))
                                        if(letra1 > letra2):
                                            temp = listaSeleccionada[i]
                                            listaSeleccionada[i] = listaSeleccionada[i+1]
                                            listaSeleccionada[i+1] = temp
                            print(color+"El valor mayor de "+str(comando[y])+" es: "+str(listaSeleccionada[len(listaSeleccionada)-1].get(comando[y])))
                    if(encotrado == False):
                        print(color+"Nombre de lista no existe")
                salir = True
            elif(comando[y] == 'MIN'):
                y = y + 1
                nombrelista = comando[y]
                v=0
                if(len(listaSeleccionada) == 0):
                    print(color+"No existe lista seleccionada")
                    salir=True
                else:
                    for v in range(0,len(listaCategorias)):
                        listaClave = listaSeleccionada[v]
                        if(nombrelista in listaClave):
                            encotrado = True
                            for numPasada in range(len(listaSeleccionada)-1,0,-1):
                                for i in range(numPasada):
                                    digito = listaSeleccionada[i].get(comando[y])
                                    if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                        # true es un numero
                                        num1 = listaSeleccionada[i].get(comando[y])
                                        num2 = listaSeleccionada[i+1].get(comando[y])
                                        print(num1+" "+num2)
                                        if(int(num1) > int(num2)):
                                            temp = listaSeleccionada[i]
                                            listaSeleccionada[i] = listaSeleccionada[i+1]
                                            listaSeleccionada[i+1] = temp
                                    else:
                                        letra1 = (listaSeleccionada[i].get(comando[y]))
                                        letra2 = (listaSeleccionada[i+1].get(comando[y]))
                                        if(letra1 > letra2):
                                            temp = listaSeleccionada[i]
                                            listaSeleccionada[i] = listaSeleccionada[i+1]
                                            listaSeleccionada[i+1] = temp
                            print(color+"El valor mINIMO de "+str(comando[y])+" es: "+str(listaSeleccionada[0].get(comando[y])))
                    if(encotrado == False):
                        print(color+"Nombre de lista no existe")
                salir = True
################################# MAX Y MIN TERMINADO #########################################################################
            elif(comando[y] == 'SUM'):
                y = y + 1
                if(listaSeleccionada == []):
                    print(color+"No existe lista seleccionada")
                else:
                    if(comando[y]=='*'):
                        l = list(listaSeleccionada[0])  
                        for a in range(0,len(l)):
                            digito = listaSeleccionada[0].get(l[a])
                            if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                suma = 0
                                for b in range(0,len(listaSeleccionada)):
                                    suma = suma + int(listaSeleccionada[b].get(l[a]))
                                print("La suma de "+str(l[a]+" es: "+str(suma)))
                    else:
                        for a in range(1,len(comando)):
                            if(comando[a] in listaSeleccionada[0]):
                                digito = listaSeleccionada[0].get(comando[a])
                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                    suma = 0
                                    for b in range(0,len(listaSeleccionada)):
                                        suma = suma + int(listaSeleccionada[b].get(comando[a]))
                                    print("La suma de "+str(comando[a]+" es: "+str(suma)))
                salir = True
###################################SUM TERMINADO####################################################
            elif(comando[y] == 'COUNT'):
                y = y + 1
                if(listaSeleccionada == []):
                    print(color+"No existe lista seleccionada")
                else:
                    if(comando[y]=='*'):
                        l = list(listaSeleccionada[0])  
                        for a in range(0,len(l)):
                            print("La suma de  registros en "+str(l[a]+" es: "+str(len(listaSeleccionada))))
                    else: # BUSCA ATRIBUTO POR ATRRIBUTO
                        for a in range(1,len(comando)):
                            sum = 0
                            for b in range(0,len(listaSeleccionada)):
                                if comando[a] in listaSeleccionada[b]:
                                    sum = sum + 1
                            print("La suma de registros en "+str(comando[a]+" es: "+str(sum)))
                salir = True
###############################################COUNT TERMINADO #############################################
            elif(comando[y] == 'REPORT'):
                y = y + 1
                if (listaSeleccionada == []):
                    print("No existe lista seleccionada previamente")
                else:
                    if comando[y] == 'TO':
                        y = y + 1 
                        nombreArchivo = comando[y]+".html"
                        y = y + 1
                        f = open(nombreArchivo,'wb')
                        mensaje = """<html>
                        <head><title>Reporte</title></head>
                        <body bgcolor=#4A4A4A>
                        <h2 align="center" style="color:#F8F8FF">Reporte de elementos</h2>
                        <div style="text-align:center;" >
	                    <table border="1" style="margin: 0 auto;">
	                    <tr>
		                <td style="color:#F8F8FF">Comando: """+comando[y]+ """</td>
	                    </tr>"""
                        mensajefinal ="""</table>
                        </div>
                        </body>
                        </html>"""   
                        if(comando[y] == 'SELECT'):
                            print(1)
                        if(comando[y] == 'LIST'):
                            print(1)
                            y = y + 1
                            if(comando[y]== 'ATTRIBUTES'):
                                print(2)
                                for a  in range(0,len(listaSeleccionada)):
                                    t = a + 1
                                    l = listaSeleccionada[a]
                                    claves = l.keys()
                                    for clave in l.keys():
                                        mensaje = mensaje + """<tr style="color:#F8F8FF"> <td  style="color:#F8F8FF"> Registro: """+str([a+1])+""" es: """+clave+"""</td></tr>"""
                            else:
                                print(color+"Comando LIST no valido")
                        if(comando[y] == 'MAX'):
                            y = y + 1
                            nombrelista = comando[y]
                            v=0
                            if(len(listaSeleccionada) == 0):
                                print(color+"No existe lista seleccionada")
                                salir=True
                            else:
                                for v in range(0,len(listaCategorias)):
                                    listaClave = listaSeleccionada[v]
                                    if(nombrelista in listaClave):
                                        encotrado = True
                                        for numPasada in range(len(listaSeleccionada)-1,0,-1):
                                            for i in range(numPasada):
                                                digito = listaSeleccionada[i].get(comando[y])
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                            # true es un numero
                                                    num1 = listaSeleccionada[i].get(comando[y])
                                                    num2 = listaSeleccionada[i+1].get(comando[y])
                                                    if(int(num1) > int(num2)):
                                                        temp = listaSeleccionada[i]
                                                        listaSeleccionada[i] = listaSeleccionada[i+1]
                                                        listaSeleccionada[i+1] = temp
                                                    else:
                                                        letra1 = (listaSeleccionada[i].get(comando[y]))
                                                        letra2 = (listaSeleccionada[i+1].get(comando[y]))
                                                        if(letra1 > letra2):
                                                            temp = listaSeleccionada[i]
                                                            listaSeleccionada[i] = listaSeleccionada[i+1]
                                                            listaSeleccionada[i+1] = temp
                                        mensaje = mensaje + """<tr> <td style="color:#F8F8FF">  El valor maximo de  """+str(comando[a])+""" es: """+str(listaSeleccionada[len(listaSeleccionada)-1].get(comando[y]))+"""</td></tr>"""
                                if(encotrado == False):
                                    print(color+"Nombre de lista no existe")
                        if(comando[y] == 'MIN'):
                            y = y + 1
                            nombrelista = comando[y]
                            v=0
                            if(len(listaSeleccionada) == 0):
                                print(color+"No existe lista seleccionada")
                                salir=True
                            else:
                                for v in range(0,len(listaCategorias)):
                                    listaClave = listaSeleccionada[v]
                                    if(nombrelista in listaClave):
                                        encotrado = True
                                        for numPasada in range(len(listaSeleccionada)-1,0,-1):
                                            for i in range(numPasada):
                                                digito = listaSeleccionada[i].get(comando[y])
                                                if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                            # true es un numero
                                                    num1 = listaSeleccionada[i].get(comando[y])
                                                    num2 = listaSeleccionada[i+1].get(comando[y])
                                                    if(int(num1) > int(num2)):
                                                        temp = listaSeleccionada[i]
                                                        listaSeleccionada[i] = listaSeleccionada[i+1]
                                                        listaSeleccionada[i+1] = temp
                                                    else:
                                                        letra1 = (listaSeleccionada[i].get(comando[y]))
                                                        letra2 = (listaSeleccionada[i+1].get(comando[y]))
                                                        if(letra1 > letra2):
                                                            temp = listaSeleccionada[i]
                                                            listaSeleccionada[i] = listaSeleccionada[i+1]
                                                            listaSeleccionada[i+1] = temp
                                        mensaje = mensaje + """<tr> <td style="color:#F8F8FF">  El valor minimo de  """+str(comando[a])+""" es: """+str(listaSeleccionada[0].get(comando[y]))+"""</td></tr>"""
                                if(encotrado == False):
                                    print(color+"Nombre de lista no existe")
                        if(comando[y] == 'SUM'):
                            y = y + 1
                            if(listaSeleccionada == []):
                                print(color+"No existe lista seleccionada")
                            else:
                                if(comando[y]=='*'):
                                    l = list(listaSeleccionada[0])  
                                    for a in range(0,len(l)):
                                        digito = listaSeleccionada[0].get(l[a])
                                        if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                            suma = 0
                                            for b in range(0,len(listaSeleccionada)):
                                                suma = suma + int(listaSeleccionada[b].get(l[a]))
                                            mensaje = mensaje + """<tr> <td style="color:#F8F8FF">  La suma de  """+str(l[a])+""" es: """+str(suma)+"""</td></tr>"""
                                else:
                                    for a in range(4,len(comando)):
                                        if(comando[a] in listaSeleccionada[0]):
                                            digito = listaSeleccionada[0].get(comando[a])
                                            if(ord(digito[0]) >= 48 and ord(digito[0]) <= 57 or digito[0] == '-' ):
                                                suma = 0
                                                for b in range(0,len(listaSeleccionada)):
                                                    suma = suma + int(listaSeleccionada[b].get(comando[a]))
                                                mensaje = mensaje + """<tr> <td style="color:#F8F8FF">  La suma de  """+str(comando[a])+""" es: """+str(suma)+"""</td></tr>"""
                        if(comando[y] == 'COUNT'):
                            y = y + 1
                            if(listaSeleccionada == []):
                                print(color+"No existe lista seleccionada")
                            else:
                                if(comando[y]=='*'):
                                    l = list(listaSeleccionada[0])  
                                    for a in range(0,len(l)):
                                        mensaje = mensaje + """<tr> <td style="color:#F8F8FF">  La suma de  registros en """+l[a]+""" es: """+len(listaSeleccionada)+"""</td></tr>"""
                                else: # BUSCA ATRIBUTO POR ATRRIBUTO
                                    for a in range(4,len(comando)):
                                        sum = 0
                                        for b in range(0,len(listaSeleccionada)):
                                            if comando[a] in listaSeleccionada[b]:
                                                sum = sum + 1
                                            else:
                                                print("Erro tipo de archivo no admitido")
                                        mensaje = mensaje + """<tr> <td style="color:#F8F8FF">  La suma de  registros en """+str(comando[a])+""" es: """+str(sum)+"</td></tr>"""
                        mensaje = mensaje + mensajefinal
                        f.write(bytes(mensaje,"ascii"))
                        f.close()
                        webbrowser.open_new_tab(nombreArchivo)
                        
                    if comando[y] == 'TOKENS':
                        f = open('reporte.html','wb')
                        mensaje = """<html>
                        <head><title>Reporte</title></head>
                        <body>
                        <h2 align="center">Reporte de elementos</h2>
                        <div style="text-align:center;">
	                    <table border="1" style="margin: 0 auto;">
	                    <tr>
		                <td>Token</td>
                        <td>Valor</td>
                        <td>Descripcion</td>
	                    </tr>"""
                        mensajefinal ="""</table>
                        </div>
                        </body>
                        </html>"""   
                        
                        for x in range(0,len(lexemaFinal)):
                            if( lexemaFinal[x].get('token') == 'tk_parentesisA'):
                                descripcion = 'Indica apertura de un nuevo conjunto de datos'
                            if( lexemaFinal[x].get('token') == 'tk_parentesisC'):
                                descripcion = 'Indica cierre de un nuevo conjunto de datos'
                            if( lexemaFinal[x].get('token') == 'tk_menor'):
                                descripcion = 'Indica apertura de un nuevo diccionario'
                            if( lexemaFinal[x].get('token') == 'tk_mayor'):
                                descripcion = 'Indica cierre de un nuevo diccionario'
                            if( lexemaFinal[x].get('token') == 'tk_corcheteA'):
                                descripcion = 'Indica apertura del nombre de dato'
                            if( lexemaFinal[x].get('token') == 'tk_corcheteB'):
                                descripcion = 'Indica cierre del nombre de dato'
                            if( lexemaFinal[x].get('token') == 'tk_reservada'):
                                descripcion = 'Indica el nombre que llevara el dato'
                            if( lexemaFinal[x].get('token') == 'tk_igual'):
                                descripcion = 'Indica asignacion de valor'
                            if( lexemaFinal[x].get('token') == 'tk_numero'):
                                descripcion = 'Indica valor numerico asignado'
                            if( lexemaFinal[x].get('token') == 'tk_coma'):
                                descripcion = 'Indica separacion entre diferentes diccionarios o tipo de datos'
                            if( lexemaFinal[x].get('token') == 'tk_true'):
                                descripcion = 'Indica asignacion de valor True booleano'
                            if( lexemaFinal[x].get('token') == 'tk_false'):
                                descripcion = 'Indica asignacion de valor False booleano'
                            if( lexemaFinal[x].get('token') == 'tk_cadena'):
                                descripcion = 'Indica valor de cadena de datos'
                      
                            mensaje = mensaje + """<tr> <td style="color:#F8F8FF"> """+lexemaFinal[x].get('token')+"""</td> <td style="color:#F8F8FF"> """+lexemaFinal[x].get('valor')+"""</td> <td style="color:#F8F8FF"> """+descripcion+"""</td></tr>"""
                        mensaje = mensaje + mensajefinal
                        f.write(bytes(mensaje,"ascii"))
                        f.close()
                        webbrowser.open_new_tab('reporte.html')
                    else:
                        print("Error comando no admitido")
                salir = True
            else:
                q=0
                aux =''
                for q in range(0,len(comando)):
                    aux = aux+comando[q]+" "
                print(color+"Comando "+aux+"No reconocido")
                salir = True      
