"""
ejemplo fucniones (solo sintaxis, para modelado hay que seguir los ejemplos)
"""

#declaración de una función

def divide(num1, num2):
    return num1/num2

def duplica(num1, num2, num3):
    return num1*2, num2*2, num3*3

#mandar a llamar la función divide
div = divide(10, 5)  #guarda en variable
print("div ", div)

print("divide_a ", divide(30,100)) # directamente imprime

print("divide_b ", divide(10,div)) # recibe como parametro una variable

#mandar a llamar la función duplica
val_1, val_2, val_3 =  duplica(1,2,3)  #guarda en 3 variables
print("valores_a ", val_1, val_2, val_3)

print("valores_b ", duplica(1.5, 2.4, 4.2))

print("valores_c ", duplica(val_1, val_2, val_3))

prueba = float(input())
prueba2 = float(input())

print("divide con inputs", prueba, prueba2, " = ", divide(prueba, prueba2))

prueba3 = float(input())
print("duplica con inputs ", prueba, prueba2, prueba3, " se convierten en",
        duplica(prueba, prueba2, prueba3))
