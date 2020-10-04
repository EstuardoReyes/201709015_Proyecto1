                                                        new = list(listaSeleccionada[t])
                                                        print("Registro "+str(e))
                                                        e = e + 1
                                                        if(comando[1] == '*'):
                                                            for u in range(0,len(new)):
                                                                print(color+new[u]+": "+listaSeleccionada[t].get(new[u]))
                                                        else:
                                                            for u in range(0,len(imprimir)):
                                                                print(color+imprimir[u]+": "+listaSeleccionada[t].get(imprimir[u]))