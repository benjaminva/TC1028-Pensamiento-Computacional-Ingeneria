"""
ejempos matrcies
"""
matriz = [[0,1],[2,3],[4,5]]
valor = 0
for linea in matriz:
  for columna in linea:
    valor = valor + columna  #usamos los iteradores
print("for 1:",valor)

"""
usando contadores for
"""
matriz = [[0,1],[2,3],[4,5]]
valor = 0
i = 0  #indice i (renglones)
for linea in matriz:
  j = 0  #indice j (columnas)
  for columna in linea:
    valor =  valor + matriz[i][j] #usamos los indices
    print("i,j, valor:", i, j, matriz[i][j])
    j = j + 1  #incremento de columna
  i = i + 1  #incremento de renglon
print("for 2:", valor)

"""
usando contadores while
"""
matriz = [[0,1],[2,3],[4,5]]
valor = 0
i = 0  #indice i (renglones)
while i < len(matriz): #número de renglones
  j = 0  #indice j (columnas)
  while  j < len(matriz[0]): #número de columnas
	  valor =  valor + matriz[i][j] #usamos los indices
	  j = j + 1  #incremento de columna
  i = i + 1  #incremento de renglon
print("while :",valor)
