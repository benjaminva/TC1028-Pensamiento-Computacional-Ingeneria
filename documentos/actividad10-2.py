# agrega comentarios en PEP 8 para cada función y
# haz tus comentarios pertinentes

"""
Crea la función menor, que encuentra el valor más pequeño en la lista
recorriendo todos lo elementos.
"""

def menor(lista):
    min = lista[0]

    for i in lista:
        if i < min:
            min = i

    return min


print(menor([1,2,3,4,577,-199,89]))













"""
Crea la función longitud (len) que recorre toda la lista y
 final devuelve el número de elementos en la lista
"""
def longitud(lista):
    cont = 0

    for i in lista:
        cont = cont + 1

    return cont

print(longitud([1,2,3,4,577,-199,89]))










"""
Crea una función para calcular la varianza. La varianza (s), se define como:
Usa tu función creada en el autoestudo para calcular el promedio.

"""
def prom(lista):
    cont = 0
    for i in lista:
        cont = cont + i
    return cont / longitud(lista)


import math

def varianza(lista):

    promedio = prom(lista)
    acum = 0
    for i in lista:
        acum = acum + (i - promedio)
    acum = acum/longitud(lista)

    return math.sqrt(acum)

print(varianza([1,2,3,4,577,-199,89]))











"""
Crea la función moda que devuelve el elemento que más se repite en la lista
y el número de veces que se repite. (puedes usar diccionarios o listas auxiliares).
Desplegar un histograma de frecuencias de los números.
"""

def moda(lista):

    diccionario = {}

    for i in lista:
        diccionario[i] = 0

    for i in lista:
        diccionario[i] = diccionario[i] + 1

    max_valor = lista[0]
    max_repeticiones = diccionario[max_valor]

    for llave in diccionario:
        if diccionario[llave] > max_repeticiones:
            max_repeticiones = diccionario[llave]
            max_valor = llave

    return max_valor, diccionario


moda, histograma = moda([11,12,11,14,577,12,14,11])

print("moda: ", moda)
print("historgrama: ",histograma)
