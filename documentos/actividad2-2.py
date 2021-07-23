# Llena este archivo con tus comentarios conforme avance la clase

# Para cada una de las siguiente funciones indica cuales
# serian los siguientes componentes:

    # estado inicial
    # tipo de datos
    # variables
    # operadores
    # estado final

#funcion suma dos valores numéricos.

def suma(num1, num2):
    res = num1  + num2
    return res

print(suma(3,5))

var = suma(8,15)

print(var)

# Un algoritmo que calcule el área de un círculo.

def area_ciruclo(radio):
    PI = 3.1415
    res =  PI * radio**2
    return res

print(area_ciruclo(1.4))

var = area_ciruclo(10)

print(var)

# Un algoritmo que transforme grados Farenheit a Celsius.
# Recuerda que Celsius = 5 / 9 ( Farenheit – 32).

def farenheit_a_celsius(far):
    cel =  5.0 / 9.0  * (far -32)
    return cel

print(farenheit_a_celsius(100))

var = farenheit_a_celsius(200)

print(var)


# Un algoritmo que calcule la superficie de un triángulo en función de
# la base y la altura.


def area_triangulo(base, altura):
    area = base*altura/2.0
    return area


print(area_triangulo(4, 5))

var = area_triangulo(10,3)

print(var)


# Desarrolla el algoritmo y posteriormente el programa completo en Python que
# solicite al usuario el valor asignado a los catetos de un triángulo rectángulo,
# y que calcule el valor resultante de la hipotenusa. Para la solución de
# este problema se sugiere que utilices el teorema de Pitágoras.
import math


def hipotenusa(cat_a, cat_b):
    temp =  cat_a**2  + cat_b**2
    hipo =  math.sqrt(temp)
    return hipo

print(hipotenusa(4, 5))

var = hipotenusa(6, 9)

print(var)





res_usuario  = float(input("cual es el area de un triangulo con base 10 y altura 6? "))

if res_usuario == area_triangulo(10, 6):
    print("muy bien")
else :
    print("la respuesta correcta es, ",  area_triangulo(10, 6))
