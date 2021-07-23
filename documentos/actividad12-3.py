# Agrega comentarios segun PEP 8 y crea tu propia funcion imprime mat
# para poder visualisar las matrices correctamente



"""
Crea una función promedio matriz que recibe una matriz de enteros.
La función regresa el promedio de todos los elementos de la matriz.
"""

def promedio_matriz(mat):
    acum = 0
    for line in mat:
        for num in line:
            acum = acum + num
    total = len(mat) * len(mat[0])

    return acum/total


mat = [[10, 29, 30],[11, 12, 13]]

print(promedio_matriz( mat ))









"""
Crea una función multiplica columna que recibe una matriz y dos
números (valor y columna). La función multiplica toda la columna de
 la matriz por el valor de num.
Por ejemplo, si la matriz tiene los siguientes valores:

2 5 6 4
3 4 5 1
7 8 5 6
9 7 1 5

Al llamar multiplica_columna(matrix, 1, 4) los nuevos valores en la matriz deberán ser:

2 20 6 4
3 16 5 1
7 32 5 6
9 28 1 5
"""

def multiplica_columna(mat, columna, valor):

    linea = 0
    while linea < len(mat):
        mat[linea][columna] = mat[linea][columna] * valor
        linea = linea + 1

    return mat

mat = [ [2, 5, 6, 4],
        [3, 4, 5, 1],
        [7, 8, 5, 6],
        [9, 7, 1, 5]]


print(multiplica_columna(mat, 1, 4))










"""
Desarrolla la función posicion_pares que recibe una matriz de enteros.
La función despliega en pantalla el número del renglón y el número de la
columna donde se encuentran los elementos pares.
Utiliza dos ciclos anidados y condicionales.

Por ejemplo, si la matriz tiene los siguientes valores:

2 5 7 4
3 6 5 1
7 3 5 8
4 9 1 6

El procedimiento desplegará en pantalla:

El valor 2 esta en la posición 0,0
El valor 4 esta en la posición 0,3
El valor 6 esta en la posición 1,1
El valor 8 esta en la posición 2,3
El valor 4 esta en la posición 3,0
El valor 6 esta en la posición 3,3
"""

def muestra_pares(mat):
    i = 0
    j = 0
    while i < len(mat):
        while j < len(mat[0]):
            valor = mat[i][j]
            if valor % 2 == 0:
                print("El valor ", valor, " esta en la posición ", i, ",", j)
            j = j + 1
        i = i + 1

muestra_pares(mat)
