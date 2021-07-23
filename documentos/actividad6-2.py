# Una función que eleve un número al cuadrado y lo imprima en pantalla.


def imprime_cuadrado(num):
    print(num**2)



imprime_cuadrado(10)


imprime_cuadrado(100)





# Una función que eleve un número al cuadrado y lo devuelva a una variable.

def devuelve_cuadrado(num):
    return num**2

print(devuelve_cuadrado(9))

var = devuelve_cuadrado(9)

print(var)



# Una función que imprima un texto en la pantalla pidiendo 3 numeros
# y devuelva el mayor de ellos.

def compara_numeros():
    num1 = int(input("valor 1? "))
    num2 = int(input("valor 2? "))
    num3 = int(input("valor 3? "))
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    if num3 >= num1 and num3 >= num2:
        return num3

print(compara_numeros())


# La función millas_kilometros que convierta la cantidad dada en millas a kilómetros.

def millas_kilometros(millas):

    kilometros = millas * 1.61
    return kilometros


print(millas_kilometros(100))

# La función libras_kilogramos que convierta la cantidad dada en libras a kilos.

def libras_kilogramos(libras):

    kilogramos = libras * 0.45
    return kilogramos

print(libras_kilogramos(1000))




# La funcion going_to_mexico que reciba millas y libras y hace uso de los funciones anteriores para devolver kilometros y kilos

def going_to_mexico(millas, libras):

    kilometros = millas_kilometros(millas)
    kilogramos = libras_kilogramos(libras)

    return kilometros, kilogramos


print(going_to_mexico(100, 1000))


var1, var2 = going_to_mexico(100, 1000)

print(var1)
print(var2)
