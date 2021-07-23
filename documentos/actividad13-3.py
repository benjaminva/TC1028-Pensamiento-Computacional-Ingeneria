"""
Un programa que pida al usuario el nombre de un archivo.
El programa deberá mostrar el contenido del archivo en pantalla.
"""

def despliega_archivo (nombre):

    f = open(nombre, "r")
    lineas = f.readlines()
    f.close()

    for linea in lineas:
        print(linea)

despliega_archivo("actividad13-3.py")

"""
Un función que copie todos los contenidos de un archivo a otro.
"""

def copia_archivo (origen, destino):

    f_origen = open(origen, "r")
    lineas = f_origen.readlines()
    f_origen.close()

    f_destino = open(destino, "a")

    for linea in lineas:
        f_destino.write(linea)
    f_destino.close()

copia_archivo("actividad13-3.py", "basura.txt")

"""
Una función que busque en el archivo todos los nombres de los jugadores.
"""

# buscar columna que corresponda en un csv, separa con split
# econtrar su posición y obtenerla de cada linea para luego
# agregarla a una lista o diccionario, despues devolver la lista

"""
Una función normalización que normalice todos los números de un archivo,
y sustituya cada modificación en su respectivo lugar. Para normalizar
puedes usar la formula valor/valorMax.
"""

# buscar la columna que corresponda con csv separa con split
# econtrar su posición y obtener los numeros, converstirlos a tipo float
# hacer la operacion despues usar replace para insertarlos de vuelta o
# concatenar todos los elementos de la listas en cada línea sobre escribir el
# archivo completo
