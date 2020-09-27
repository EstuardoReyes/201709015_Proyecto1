
dic1 = dict(nombre = 'tk_true' , valor = 'true')
dic2 = dict(nombre = 'tk_false' , valor = 'false')
lista_tk = [dic1,dic2]
lexemas = []

def AFD(cadena):
    state = 6
    auxiliar = ','
    for x in range(0,len(cadena)):
        actual = cadena[x]
        if state == 0:
            if actual == '(':
                dic = dict(token = 'tk_parentesisA' , valor = '(')
                lexemas.append(dic)
            elif actual == ')':
                dic = dict(token = 'tk_parentesisC' , valor = ')')
                lexemas.append(dic)
            elif actual == '<':
                dic = dict(token = 'tk_menor' , valor = '<')
                lexemas.append(dic)
            elif actual == '>':
                dic = dict(token = 'tk_mayor' , valor = '>')
                lexemas.append(dic)
            elif actual == '[':
                dic = dict(token = 'tk_corcheteA' , valor = '[')
                lexemas.append(dic)
            elif actual == ']':
                dic = dict(token = 'tk_corcheteC' , valor = ']')
                lexemas.append(dic)
            elif actual == '=':
                dic = dict(token = 'tk_igual' , valor = '=')
                lexemas.append(dic)
            elif actual == ';':
                dic = dict(token = 'tk_puntoComa' , valor = ';')
                lexemas.append(dic)
            elif actual == '"':
                state = 1
            elif ord(actual) >= 48 and ord(actual) <= 57:
                state = 3
                x = x-1
    ###########################################################################  
        elif state == 1:
            if actual == ' " ':
                state = 2
            else:
                auxiliar = auxiliar + actual
    ###########################################################################  
        elif state == 2:
            dic = dict(token = 'tk_cadena' , valor = auxiliar)
            lexemas.append(dic)
            auxiliar = ''
            state = 0
    ###########################################################################
        elif state == 3:   
            if ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual                                        #Estado 3
            elif actual == '.':
                state = 4
                auxiliar = auxiliar + actual
            else:
                dic = dict(token = 'tk_numero' , valor = auxiliar)
                lexemas.append(dic)
                auxiliar = ''
                state = 0
                x = x-1
    ############################################################################    
        elif state == 4:
            if ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual
                state = 5                                       #Estado 3
            else:
                auxiliar = auxiliar + '0'
                dic = dict(token = 'tk_numero' , valor = auxiliar)
                lexemas.append(dic)
                auxiliar = ''
                state = 0
                x = x-1
        elif state == 5:
            if ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual  
            else:
                dic = dict(token = 'tk_numero' , valor = auxiliar)
                lexemas.append(dic)
                auxiliar = ''
                state = 0
                x = x-1  
    ############################################################################
        elif state == 6:
            print()
            if ord(actual)==44 or ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165 or ord(actual)==32:
                print("hola")

       

