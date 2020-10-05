# SimpleQL CLI
                                            1. Introduccion
SimpleQL CLI es una interfaz de línea de comandos que permite utilizar SimpleQL para
realizar diferentes operaciones de análisis y consultas sobre un conjuto de datos que se
encuentra alojado en memoria. Esta versión de SimpleQL también implementa su propia notación de objetos
para los archivos de texto que contienen la información inicial, esta se conoce como AON
(Alternative Object Notation)

                                           2. Primeros Pasos
Lo primero que se debe de realizar antes de ejecutar el programa es descargar python para el respectivo sistema operativo https://www.python.org/downloads/mac-osx/ para mac
y https://www.python.org/downloads/windows/ para sistemas operativos windows, luego de instalar para corroborar el funcionamiento ejecutar en cmd la palabra python luego de eso con presionar click izquierdo al archivo automaticamente se abrira una terminal para ejecutar el programa

                                             3. Modo de funcionamiento
 Para facilitar la comprobacion de todas las funciones disponibles en el programa el modo de funcionamiento es a partir de la lectura de un archivo de extension .siql que contienen series de
instrucciones y comandos SimpleQL, esto con el objetivo de que el usuario no tenga
que escribir uno por uno los comandos que se desee ejecutar
 
                                3.1 Cargar
Con este comando basta con seguir el siguiente comando: cargar archivo.json y para agregar varios archivos json basta con colocar una coma(,) justo despues de cada archivo.json
exceptuando el ultimo archivo

                               3.2 Seleccionar
Con este comando lo unico de debe hacer es empezar el comando con la palabras seleccionar escoger los atributos que desea mostrar en pantalla siempre y cuando existan y luego
agregar la palabra DONDE el atributo que desea buscar y seguido de un igual la palabra que desea buscar , si es un nombre debe de ir encerrado en comillas
SELECCIONAR nombre DONDE nombre = "tato"
                               
                               3.3 Maximo
Con este comando permite saber cual es el valor maximo ya sea que se elija de promedio o de edad                               
                               
                             
                               3.4 Minimo
Con este comando permite saber cual es el valor minimo ya sea que se elija de promedio o de edad

                               3.5 suma
Con este comando permite saber cual es el total de la suma de todos los atributos escogidos  

                               3.6 Cuenta
Permite saber la cantidad de registros existentes en memoria


