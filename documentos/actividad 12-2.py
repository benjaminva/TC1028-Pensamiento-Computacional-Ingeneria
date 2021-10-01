"""
1. Haz una lista anidada que guarde 4 listas de tamaño 2 (osea una matriz de 4 * 2) llénala con pares de buena combinaciones como: ['café','leche'] o ['rol','pizza'] o ['rick', 'morty'], etc..
"""

lista = [['café','leche'],
         ['rol','pizza'],
         ['rick', 'morty'],
         ['perro','hueso']]


"""
2. Haz la función imprime_matriz que recibe una lista anidada y la imprime en forma de matriz (renglón salto de línea)
"""
def imprime_while(matriz):
    valor = 0
    i = 0  #indice i (renglones)
    while i < len(matriz): #número de renglones
      j = 0  #indice j (columnas)
      while  j < len(matriz[0]): #número de columnas
    	  print(matriz[i][j], end = " ") #usamos los indices
    	  j = j + 1  #incremento de columna
      print()
      i = i + 1  #incremento de renglon

def imprime_for(matriz):
    for linea in matriz:
      for columna in linea:
        print(columna, end = " ")  #usamos los iteradores
      print()

imprime_while(lista)
print()
imprime_for(lista)
print()

"""
3. Haz la función suma matrices, que recibe 2 matrices de 3 * 3 y devuelve una suma de matrices
"""

def suma_mat(a,b):
    c = [[0,0,0],[0,0,0],[0,0,0]]
    valor = 0
    i = 0  #indice i (renglones)
    while i < len(a): #número de renglones
      j = 0  #indice j (columnas)

      while  j < len(a[0]): #número de columnas
    	  c[i][j] = a[i][j] + b[i][j]
    	  j = j + 1  #incremento de columna

      i = i + 1  #incremento de renglon

    return c

mat1 = [[1,2,3],
        [1,2,3],
        [1,2,3]]

mat2 = [[10,20,33],
        [10,20,33],
        [10,20,33]]


res = suma_mat(mat1, mat2)

imprime_while(res)
print()
imprime_for(res)
