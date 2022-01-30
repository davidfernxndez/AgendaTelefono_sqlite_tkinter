# Proyecto final Python Avanzado
#David Fernández Martínez

import os
import csv
import sqlite3
import tkinter as tk
from tkinter.filedialog import askopenfile



###############################################################################
#FUNCIONES QUE INTERVIENEN EN LA OPCIÓN DEL MENÚ "Abrir archivo"
###############################################################################

def open_file():
    """ Esta función crea un diálogo para abrir un archivo.Llama a las funciones
    lee_archivo_como_CSV y almacena_en_BD para tratar el archivo como un CSV y
    almacenarlo de forma adecuada en  una base de datos. Muestra un mensaje
    en el que indica el nombre del archivo y si el proceso se ha producido de
    forma exitosa o si hay errores.Previamente hace invisibles aquellos widgets
    que pudiesen estar abiertos cuando se seleccionó otra opción del menu.
    """

    texto1.pack_forget()
    texto2.pack_forget()
    texto3.pack_forget()
    texto_error.pack_forget()
    cuadro_texto.pack_forget()
    cuadro_texto1.pack_forget()
    boton_anadir.pack_forget()
    boton_consulta.pack_forget()
    boton_eliminar.pack_forget()


    file=askopenfile(mode='r',filetypes=[("Archivo CSV","*.*")])
    file_name=os.path.basename(file.name)

    texto1.pack()
    texto1["text"]="Nombre del archivo: {}".format(file_name)
    datos=lee_archivo_como_CSV(file)
    estado=almacena_en_BD(datos)

    texto2.pack()
    if(estado):
        texto2["text"]="Se ha producido un error"
    else:
        texto2["text"]="Se han almacenado los registros en la base de datos con éxito"


def lee_archivo_como_CSV(archivo):
    """ Esta función recibe un archivo leido con askopenfile, haciendo uso de
    csv.reader lee dicho archivo como un CSV. Se crea una lista de listas, cada
    una de las listas  contiene  una fila del CSV. Se elimina la primera fila
    porque contiene el nombre de los campos. Implementa control de errores para
    informar si el archivo no puede ser leido como un CSV. Finalmente devuelve
    la lista con el objetivo de almacenarla en la base de datos.
    """
    try:
        reader = csv.reader(archivo)
        lista=[]
        for fila in reader:
            lis=[]
            lis.append(fila[0])
            lis.append(fila[1])
            lista.append(lis)
    except:
        texto1["text"]="El archivo no puede ser leido como CSV"
    else:
        lista=lista[1:]
        return lista


def almacena_en_BD(datos):
    """ Funcion que crea una tabla 'Agenda' con los campos NOMBRE y TELEFONO e
    inserta en ella los valores de una lista que se le pasa como entrada. Devuelve una
    variable booleana que indica con un 0 que todo ha ido correctamente (control
    de errores ).
    """
    try:
        conexion = sqlite3.connect('base_de_datos.db')
        cur = conexion.cursor()

        query = "CREATE TABLE IF NOT EXISTS Agenda(NOMBRE TEXT, TELEFONO TEXT)"
        cur.execute(query)

        for i in datos:
            valores="'{}','{}'".format(i[0],i[1])
            query="INSERT INTO Agenda(NOMBRE,TELEFONO) VALUES({})".format(valores)
            cur.execute(query)

        conexion.commit()
        conexion.close()
    except:
        error=1
        return error
    else:
        error=0
        return error


################################################################################
#FUNCIONES QUE INTERVIENEN EN LA OPCIÓN DEL MENÚ "Consultar base de datos"
################################################################################

def abre_consultar():
    """ Esta función presenta en la ventana los widgets necesarios del
    proceso de consultar un nombre para ver el telefono que tiene asociado. Previamente
    hace invisibles aquellos widgets que pudiesen estar abiertos cuando se
    seleccionó otra opción del menu.
    """
    texto1.pack_forget()
    texto2.pack_forget()
    texto3.pack_forget()
    texto_error.pack_forget()
    cuadro_texto1.pack_forget()
    boton_anadir.pack_forget()
    boton_eliminar.pack_forget()
    cuadro_texto.pack_forget()

    texto1.pack(side=tk.TOP)
    texto1["text"]="Introduce el nombre para consultar su número de telefono: "
    cuadro_texto.pack(side=tk.TOP)
    boton_consulta.pack(side=tk.TOP)


def consulta_BD():
    """Esta funcion obtiene el nombre introducido en el cuadro de texto y busca
    el telefono asociado a este.Si el nombre no existe lo indica. Si realizamos
    una consulta y aun no hemos cargado ningún archivo mostrará un mensaje que
    indica este hecho
    """
    conexion=sqlite3.connect('base_de_datos.db')
    cur=conexion.cursor()
    try:
        word=cuadro_texto.get()
        cur.execute("SELECT * FROM Agenda WHERE NOMBRE='{}'".format(word))
        resultado=cur.fetchone()
    except:
        texto1.pack_forget()
        cuadro_texto.pack_forget()
        boton_consulta.pack_forget()

        texto_error.pack()
        texto_error["text"]="Para realizar una consulta debe crear la tabla\npara ello seleccione la opción 'Abrir archivo'"
        conexion.commit()
        conexion.close()
    else:
        texto2.pack()
        texto2["text"]="RESULTADO: "
        texto3.pack()
        if(resultado==None):
            texto3["text"]="No se ha encontrado ese nombre en la base de datos"
        else:
            texto3["text"]="{}".format(resultado)

        conexion.commit()
        conexion.close()

###############################################################################
#FUNCIONES QUE INTERVIENEN EN LA OPCIÓN DEL MENÚ "Añadir registro a la base de
# datos"
###############################################################################

def abre_anadir():
    """ Esta función muestra sobre la ventana los widgets necesarios para añadir
    un nuevo registro a la base de datos. Previamente hace invisibles aquellos
    widgets que pudiesen estar abiertos cuando se seleccionó otra opción del menu.
    """
    boton_consulta.pack_forget()
    boton_eliminar.pack_forget()
    texto1.pack_forget()
    texto2.pack_forget()
    texto3.pack_forget()
    cuadro_texto.pack_forget()
    texto_error.pack_forget()

    texto1.pack(side=tk.TOP)
    texto1["text"]="NOMBRE: "
    cuadro_texto.pack(side=tk.TOP)
    texto2.pack(side=tk.TOP)
    texto2["text"]="TELEFONO: "
    cuadro_texto1.pack(side=tk.TOP)
    boton_anadir.pack(side=tk.TOP)

def numero_correcto(n):
    """ Para que un número de teléfono sea correcto la cadena de caracteres que
    se introduce en el cuadro de texto debe estar formada por 9 números. La
    función comprueba mediante isdigit si la cadena contiene unicamente numeros
    y mediante len si el tamaño es 9.
    """
    if(n.isdigit() and len(n)==9):
        es_valido=1
        return es_valido
    else:
        es_valido=0
        return es_valido

def anadir_registro():
    """ Esta función lee lo que se introduce en los cuadros de texto correspondientes
    al nombre y al teléfono que se quieren añadir. Mediante la función numero_correcto
    verifica que el teléfono a añadir es correcto, si lo es se conecta a la base de
    datos, añade el nuevo registro y muestra un mensaje informando que la operación es
    correcta. Si por el contrario el número de telefóno es incorrecto mostrará un
    mensaje informando de este hecho. Además si aún no se ha abierto un archivo CSV
    mostrará un mensaje informando sobre esto.
    """
    texto3.pack_forget()
    nombre_in=cuadro_texto.get()
    telefono_in=cuadro_texto1.get()

    if(numero_correcto(telefono_in)):
        conexion=sqlite3.connect('base_de_datos.db')
        cur=conexion.cursor()

        try:
            cur.execute("INSERT INTO Agenda(NOMBRE,TELEFONO) VALUES('{}','{}')".format(nombre_in,telefono_in))
        except:
            cuadro_texto.pack_forget()
            boton_consulta.pack_forget()
            texto1.pack_forget()
            texto2.pack_forget()
            cuadro_texto1.pack_forget()
            boton_anadir.pack_forget()


            texto_error.pack()
            texto_error["text"]="Para añadir un nuevo registro debe crear la tabla\npara ello seleccione la opción 'Abrir archivo'"
            conexion.commit()
            conexion.close()
        else:
            texto3.pack()
            texto3["text"]="RESULTADO: \nOperación realizada con éxito"
            conexion.commit()
            conexion.close()
    else:
        texto3.pack()
        texto3["text"]="El número de teléfono introducido, no es correcto"

################################################################################
#FUNCIONES QUE INTERVIENEN EN LA OPCIÓN DEL MENÚ "Eliminar registro a la base de
# datos"
################################################################################

def abre_eliminar():
    """Esta función muestra sobre la ventana los widgets necesarios para eliminar
    un registro de la base de datos. Previamente hace invisibles aquellos
    widgets que pudiesen estar abiertos cuando se seleccionó otra opción del menu.
    """
    texto1.pack_forget()
    texto2.pack_forget()
    texto3.pack_forget()
    texto_error.pack_forget()
    cuadro_texto.pack()
    cuadro_texto1.pack_forget()
    boton_consulta.pack_forget()
    boton_anadir.pack_forget()
    cuadro_texto.pack_forget()

    texto1.pack(side=tk.TOP)
    texto1["text"]="Introduce el nombre de la agenda que quiere eliminar: "
    cuadro_texto.pack(side=tk.TOP)
    boton_eliminar.pack(side=tk.TOP)

def eliminar_registro():
        """ Esta función lee  del cuadro de texto el nombre que se quiere eliminar.
        En primer lugar comprueba que el nombre existe en la tabla. Si existe lo
        elimina. Muestra un mensaje informando si la operación ha sido existosa
        o si el nombre no existe. Además si la tabla aún no se ha creado notifica
        con un mensaje.
        """
        conexion=sqlite3.connect('base_de_datos.db')
        cur=conexion.cursor()

        try:
            palabra=cuadro_texto.get()
            cur.execute("SELECT * FROM Agenda WHERE NOMBRE='{}'".format(palabra))
            res=cur.fetchone()

            if(res!=None):
                cur.execute("DELETE FROM Agenda WHERE NOMBRE='{}'".format(palabra))
                eliminado=1
            else:
                eliminado=0
        except:
            cuadro_texto.pack_forget()
            boton_consulta.pack_forget()
            texto1.pack_forget()
            texto2.pack_forget()
            cuadro_texto1.pack_forget()
            boton_anadir.pack_forget()
            boton_eliminar.pack_forget()


            texto_error.pack()
            texto_error["text"]="Para eliminar un registro debe crear la tabla\npara ello seleccione la opción 'Abrir archivo'"
            conexion.commit()
            conexion.close()
        else:
            if(eliminado):
                texto2.pack()
                texto2["text"]="RESULTADO: \nSe ha eliminado el registro con éxito"
                conexion.commit()
                conexion.close()
            else:
                texto2.pack()
                texto2["text"]="RESULTADO: \nEl nombre introducido no existe en la base de datos"
                conexion.commit()
                conexion.close()

################################################################################
# Implementación de la ventana, menu y los widgets que utilizaremos
################################################################################

window=tk.Tk()
window.title("Agenda")
window.geometry("500x200")

#Creamos el menu
menu=tk.Menu(window)
group1=tk.Menu(menu,tearoff=0)
group1.add_command(label='Abrir archivo',command=open_file)
group1.add_command(label='Consultar base de datos',command=abre_consultar)
group1.add_command(label='Añadir registro a la base de datos',command=abre_anadir)
group1.add_command(label='Eliminar registro de la base de datos',command=abre_eliminar)
menu.add_cascade(label="OPCIONES",menu=group1)
window.config(menu=menu)

#Definimos los Labels que utilizaremos en las diferentes opciones del menu
texto1=tk.Label(window,text="")
texto2=tk.Label(window,text="")
texto3=tk.Label(window,text="")
texto_error=tk.Label(window,text="")

#Definimos los cuadros de texto que necesitaremos
cuadro_texto=tk.Entry(window)
cuadro_texto1=tk.Entry(window)

#Definimos los botones que necesitaremos
boton_consulta=tk.Button(window,text='CONSULTA',bg='red',fg='white',command=consulta_BD)
boton_anadir=tk.Button(window,text='AÑADIR',bg='blue',fg='white',command=anadir_registro)
boton_eliminar=tk.Button(window,text='ELIMINAR',bg='green',fg='white',command=eliminar_registro)


window.mainloop()
