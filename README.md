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
 
                                               4. Lectura de archivo
La lectura de archivo se hace mediante la lectura de archivo tipo AON que es un tipo de archivo propio del programa que maneja y consta la siguiente estructura ( ) Los paréntesis definen un arreglo, todo lo que se encuentra adentro es un elemento del mismo, < > Estos símbolos definen un objeto, los
atributos de un objeto están separados por
comas. [] Se utilizan para definir identificadores, o en
otras palabra el nombre de un atributo 


                                              5. Comando CREATE
Tiene la función de crear sets de memoria donde se alojarán ciertos conjuntos de
datos cargados por el usuario un ejemplo es: CREATE SET carros
                               
                                              6. Comando LOAD
Este comando carga al conjunto especificado por set_id la información contenida en
la los archivos de la lista de archivos definida después de la keyword FILES.
Ejemplos:
LOAD INTO elementos FILES periodica.aon, periodica2.aon
LOAD INTO carros FILES carros.aon

Algunas consideraciones para tomar en cuenta son que los archivos para cargarse a
un mismo set siempre tendrán la misma estructura, es decir, en ningún momento
se tendrá que cargar al set carros un archivo con información de elementos y otro
archivo con información de carros, garantizando así que todos los registros de un
set tengan siempre la misma estructura
                               
                             
                                             7. Comando USE
Este comando define el set de datos a utilizar para las siguientes operaciones, si se
intenta realizar operaciones sin haber definido un set de datos la aplicación debe
mostrar un error. Ejemplo:
USE SET carros
USET SET elementos

                                           8. Comando SELECT
Permite seleccionar uno o más registros o atributos de los mismos con base en
condiciones simples que pueden aplicarse a los atributos de los mismos.
En lugar de listar los atributos también es posible utilizar el operador *, esto
automáticamente seleccionará todos los campos del registro.
Ya que la estructura de los sets no está predefinida, sino que viene definida en los
archivos los atributos seleccionables serán cualquiera que pertenezca al set sobre el
cual se está actualmente trabajando.
Algunos Ejemplos para el set carros:
SELECT modelo, tipo, marca, año WHERE color = “rojo”
SELECCIONAR *
SELECCIONAR * WHERE marca = “Mazda” AND año < 1996
Otras funcionalidades con las que cuenta el comando SELECT es la ampliación de las
condiciones, a continuación se definen las ampliaciones:

● Es posible utilizar diferentes operaciones de comparación, las mismas que
serían utilizadas en un lenguaje regular de programación: < (menor que), >
(mayor que), <= (menor igual), >= (mayor igual), = (igual) y != (no igual). Estas
operaciones solo pueden ser realizadas entre datos del mismo tipo: cadenas
con cadenas, números con números y booleanos con booleanos (en el caso
de los booleanos True es siempre mayor que False). En caso de comparar
cadenas se hará de forma lexicográfica.
● Es posible combinar condiciones utilizado los operadores AND (conjunción),
OR (disyunción) y XOR (disyunción exclusiva).
● El comando SELECT permitirá el uso de expresiones regulares, las reglas de
las mismas se definen más adelante.
Algunos adicionales para el set de elementos:
SELECT nombre, padre, siglas WHERE tipo = “metal” OR tipo = “carbono”
SELECCIONAR * WHERE siglas = “HG” 

                                            9. Comando LIST
Este comando permite listar los atributos que componen a cada registro del set.


                                            10. Comando PRINT
Este comando permite al usuario elegir el color en el que serán presentados los
resultados en la línea de comandos. Los valores a elegir serán BLUE, RED, GREEN,
YELLOW, ORANGE y PINK. Ejemplo:
PRINT IN BLUE

                                            11. Comando SUM
Permite obtener la suma de todos los valores de un atributo especificado en el
comando. Este comando solamente se utilizará sobre valores de tipo numérico, no
se realizarán sumas sobre valores de tipo cadena o booleanos. En caso de
seleccionarse varios atributos deberá reportar cada atributo con su respectiva
suma, en caso de que el atributo tenga valor null se ignorará. El comando SUM
acepta el uso del operador *.
Ejemplos:
SUM edad, promedio, faltas
SUM asistencias

                                            12. Comando MAX | MIN
Permiten encontrar el valor máximo o el valor mínimo que se encuentre en el
atributo de uno de los registros del conjunto en memoria. En caso de seleccionar el
valor máximo de un valor de tipo String la comparación será realizada de forma
lexicográfica. Ejemplos usando el set carro:
MAX año
MIN modelo


                                            13. Comando COUNT
Permite contar el número de registros que se han cargado a memoria. En caso de
que alguno de los atributos tenga valor null se ignorará. El comando COUNT
permite el uso del operador *.
Ejemplos:
COUNT *
COUNT edad, promedio, faltas

                                           14. Comando REPORT
Este comando permite crear un reporte en html a partir de cualquier otro comando
de análisis o selección. Permite 
definir el nombre del archivo sobre el que se crea el reporte.
Ejemplos:
REPORT TO reporte1 COUNT *
REPORT TO reporte2 SUM *

                                           15. Comando REPORT TOKENS
Este comando crea un reporte en html que muestra una lista de todos los
lexemas encontrados por el AFD, mostrando también a cual token pertenece
el lexema y una breve descripción del mismo.
                             


