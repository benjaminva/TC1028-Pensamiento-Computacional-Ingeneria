"""
ejemplo ciclos for
"""
lista = ['a','b','c','d','f']

#recorre cada elemento en la lista
for i in lista:
    print("i ", i)

#usando la funcion range para generar listas
print(range(6))
print(range(-3, 3))

#cilco con rango en acumulador
acum = 0
for i in range(5):
    print("i ", i)
    acum = acum + i*2

#busca elemento
for i in lista:
    if i == 'd':
        print("si tiene la letra d")

#suma de multiplos de 3
n = int(input())
acum = 0
for i in range(n):
    if i % 3 == 0:
        acum = acum + i
print("los multiplos de 3 entre 1 y", n, "suman", acum)
