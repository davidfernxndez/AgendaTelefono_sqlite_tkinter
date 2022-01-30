# AgendaTelefono_sqlite_tkinter
Implementación de una agenda de teléfono que actua sobre un archivo CSV, almacenando y cargando los datos de una base de datos a través de sqlite3. Se implementa una interfaz grafica (GUI) haciendo uso de la libreria tkinter. 
# 1. FUNCIONAMIENTO 
Se ha creado una interfaz de usuario (“Agenda”) compuesto por un menú (“OPCIONES”), este 
menú contiene 4 opciones:
- Abrir archivo. Si clicamos en esta opción se abrirá un dialogo para abrir el archivo CSV. 
Si el archivo seleccionado puede ser leído como un CSV con la estructura que se trabaja 
en este proyecto se almacenará adecuadamente en una base de datos. Si el proceso se 
realiza con éxito se muestra un mensaje informando del nombre del archivo y de que 
los registros se han almacenado sin problemas.

- Consultar base de datos. Esta opción nos abre un cuadro de texto en el que podemos 
introducir un nombre y un botón para consultar el número de teléfono que tiene 
asociado dicho nombre. En caso de que el nombre no exista en la base de datos nos dirá 
que no ha sido encontrado, en otro caso nos mostrará como resultado la pareja de 
NOMBRE-TELEFÓNO solicitada. En caso de que realicemos una consulta en la base de 
datos sin haber seleccionado en primer lugar la opción “Abrir archivo”, la tabla en la que 
se almacenan los datos todavía no estará creada por lo que se muestra un mensaje que 
nos informa de este hecho y nos invita a abrir un archivo.

- Añadir registro a la base de datos. Esta opción muestra en la interfaz dos cuadros de 
texto, uno para introducir el nombre y otro para introducir el teléfono que queremos 
añadir, y un botón “AÑADIR” que pulsaremos para realizar la acción. Para que el 
teléfono introducido sea correcto debe contener 9 números. Si el teléfono introducido 
es correcto nos mostrará un mensaje informando de que la operación se ha realizado 
con éxito, en caso contrario nos dirá que el teléfono no es correcto. En caso de que 
intentemos añadir un registro en la base de datos sin haber seleccionado en primer lugar 
la opción “Abrir archivo”, la tabla en la que se almacenan los datos todavía no estará 
creada por lo que se muestra un mensaje que nos informa de este hecho y nos invita a 
abrir un archivo.

- Eliminar registro de la base de datos. Esta opción muestra en la interfaz un cuadro de 
texto y un botón. En el cuadro de texto se introduce el nombre del registro que se quiere 
eliminar y el botón “ELIMINAR” se pulsa para que se realice el proceso. La pulsación del 
botón ofrece un mensaje que informa si la operación se ha realizado con éxito o si el 
nombre que se quiere eliminar no existe en la tabla. En caso de que intentemos eliminar 
un registro en la base de datos sin haber seleccionado en primer lugar la opción “Abrir 
archivo”, la tabla en la que se almacenan los datos todavía no estará creada por lo que 
se muestra un mensaje que nos informa de este hecho y nos invita a abrir un archivo.

# 2. ESTRUCTURA DEL CÓDIGO

Cada una de las opciones que componen el menú se han implementado mediante funciones que 
actuando de forma conjuntan proporcionan el servicio deseado para cada opción del menú que 
seleccione el usuario. 
Con el objetivo de estructurar las funciones que son utilizadas en cada una de las opciones se ha 
utilizado la siguiente sintaxis en el código:
######################################################################

#FUNCIONES QUE INTERVIENEN EN LA OPCIÓN DEL MENÚ "<Nombre de la opción>"

######################################################################

Todo lo que hay tras esos comentarios y hasta los siguientes comentarios de este tipo 
corresponderá con las funciones utilizadas para la implementación de la opción del menú que 
se indica en el comentario.

Tras todas las funciones, al final del código se define la ventana, el menú y todos los widgets 
(Labels, cuadros de texto y botones) que serán utilizados por las funciones previamente 
definidas.

Un aspecto que cabe mencionar es el uso del método pack_forget(). Se ha pretendido que cada 
opción del menú presente únicamente los widgets necesarios para llevar a cabo su funcionalidad 
específica. Por ello se ha utilizado pack_forget() para hacer invisibles aquellos widgets utilizados 
en una opción y que no queremos que aparezcan en otras.

Las funciones empleadas se han documentado mediante docstrings. Si se abre un nuevo archivo 
tras haber abierto uno y sobre la misma base de datos, se añadirán los nuevos pares nombre-teléfono a la tabla Agenda junto a los que ya se habían almacenado procedentes del CSV previo
