
dic1 = dict(nombre = 'tk_true' , valor = 'true')
dic2 = dict(nombre = 'tk_false' , valor = 'false')
lista_tk = [dic1,dic2]
lexemas = [""]
listaComandos =[""]
lista = [""]
def AFD(cade):
    comando = [""]
    comando[:]=[]
    print("Leyendo archivo "+cade)
    archivo = open(cade)
    cadena = archivo.read()
    state = 0
    abierto = False
    auxiliar = ''
    claveAuxiliar=''
    valorAuxiliar=''
    x=0
    diccionario = dict()
    while x < len(cadena):
        actual = cadena[x]
        if state == 0:
            if actual == '(':
                dic = dict(token = 'tk_parentesisA' , valor = '(')
                lexemas.append(dic)
                lista[:]=[]
                abierto = True
                x=x+1
                
            elif actual == ')':
                dic = dict(token = 'tk_parentesisC' , valor = ')')
                lexemas.append(dic)
                x=x+1
            elif actual == '<': #crea un dicionario
                dic = dict(token = 'tk_menor' , valor = '<')
                lexemas.append(dic)
                diccionario = dict()
                cont=0
                cunt=0
                x=x+1
            elif actual == '>': #se guarda el diccionario
                dic = dict(token = 'tk_mayor' , valor = '>')
                lexemas.append(dic)
                valorAuxiliar = lexemas[len(lexemas)-2]['valor']
                diccionario[claveAuxiliar]=valorAuxiliar
                lista.append(diccionario)
                x=x+1
            elif actual == '[':
                dic = dict(token = 'tk_corcheteA' , valor = '[')
                lexemas.append(dic)
                x=x+1
            elif actual == ']':
                dic = dict(token = 'tk_corcheteC' , valor = ']')
                claveAuxiliar = lexemas[len(lexemas)-1]['valor']
                lexemas.append(dic)
                x=x+1
            elif actual == '=':
                dic = dict(token = 'tk_igual' , valor = '=')
                lexemas.append(dic)
                x=x+1
            elif actual == ';':
                dic = dict(token = 'tk_puntoycoma' , valor = ';')
                lexemas.append(dic)
                listaComandos.append(comando)
                comando=[]
                x=x+1
            elif actual == ',':
                if lexemas[len(lexemas)-1]['valor'] != '>' and abierto ==True:
                   valorAuxiliar = lexemas[len(lexemas)-1]['valor']
                   diccionario[claveAuxiliar]=valorAuxiliar
                dic = dict(token = 'tk_coma' , valor = ',')
                lexemas.append(dic)
                x=x+1
            elif actual == '"':
                state = 1
                x=x+1
            elif ord(actual) >= 48 and ord(actual) <= 57 or actual=='-':
                state = 3
            elif ord(actual)==95 or ord(actual)==44 or ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165:
                state = 6
                auxiliar = auxiliar + actual
                x=x+1
            elif ord(actual) == 32:
                x=x+1
            else:
                x=x+1
    ###########################################################################  
        elif state == 1:
            if actual == '"':
                state = 2
            else:
                auxiliar = auxiliar + actual
                x=x+1
    ###########################################################################  
        elif state == 2:
            dic = dict(token = 'tk_cadena' , valor = auxiliar)
            lexemas.append(dic)
            auxiliar = ''
            state = 0
            x=x+1
    ###########################################################################
        elif state == 3:   
            if ord(actual) >= 48 and ord(actual) <= 57 or actual=='-':
                auxiliar = auxiliar + actual  
                x=x+1                                      #Estado 3
            elif actual == '.':
                state = 4
                auxiliar = auxiliar + actual
                x=x+1
            else:
                dic = dict(token = 'tk_numero' , valor = auxiliar)
                lexemas.append(dic)
                auxiliar = ''
                state = 0
    ############################################################################    
        elif state == 4:
            if ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual
                x=x+1
                state = 5                                       #Estado 3
            else:
                auxiliar = auxiliar + '0'
                dic = dict(token = 'tk_numero' , valor = auxiliar)
                lexemas.append(dic)
                auxiliar = ''
                state = 0
    ##############################################################################
        elif state == 5:
            if ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual  
                x=x+1
            else:
                dic = dict(token = 'tk_numero' , valor = auxiliar)
                lexemas.append(dic)
                auxiliar = ''
                state = 0
    ############################################################################
        elif state == 6:        #Imprime solo pal
            if ord(actual)==46 or ord(actual)==95 or ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165  or ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual
                x=x+1
            else:
                flag = False
                for q in range(0,len(lista_tk)):
                    if(auxiliar == lista_tk[q]['valor']):
                        lexemas.append(lista_tk[q])
                        flag = True
                        state = 0
                        auxiliar=''
                if flag==False:
                    dic = dict(token = 'tk_reservada' , valor = auxiliar)
                    comando.append(auxiliar)
                    lexemas.append(dic)
                    auxiliar = ''
                    state = 0 
  
       

