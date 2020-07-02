"""
ejemplo escritura y lectura de archivos
"""

#abrir archivo en modo lectura
f = open("readme.txt", "r")

#leer todo el archivo en una sola cadena.
print(f.read())

#cerrar archivo
f.close()
nombre = input("dame el nombre de un archivo")
#abrir archivo en modo lectura
f = open(nombre, "r")
# lee una sola línea
linea = f.readline()

#leer cada linea por separado
for linea in f:
    print(linea) #imprime una línea a la vaz

f.close()

#escribe en archivo
f = open("zzzzzaaaaaa nuevo archivo.txt", "w")
f.write("Mi nombre es Seiya!!!")
f.close()
