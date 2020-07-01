"""
ejemplo escritura y lectura de archivos
"""

#abrir archivo en modo lectura
f = open("readme.txt", "r")

#leer todo el archivo en una sola cadena.
print(f.read())

#cerrar archivo
f.close()

#abrir archivo en modo lectura
f = open("readme.txt", "r")
# lee una sola línea
linea = f.readline()

#leer cada linea por separado
for linea in f:
    print(linea) #imprime una línea a la vaz

f.close()
