#Comenta el código para que cumpla con pep 8 y úsalo para tus notas


"""
Calcular el factorial de un número N, donde N es pedido al usuario.
El factorial de un número N = 1 * 2 * 3 * ... * N.
"""

def fact(n):
    i = 1
    acum = 1

    while i <= n :
        acum = acum * i
        i = i + 1

    return acum

print(fact(3))


print(fact(5))



"""
Usando sólo sumas y/o restas, obtener el módulo y cociente de una división.
"""
def division(divisor, dividendo): # dividendo/divisor

    cociente = 0

    while dividendo > divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    modulo = divisor - dividendo

    return dividendo, modulo

print(division (4, 15))


"""
Dado un número, obtener su inverso numérico. Por ejemplo, si el número es 1234,
el resultado debe ser 4321.
"""


def obten_inverso (num):

    inverso = 0

    while num > 0:
        digito = num % 10
        num = int(num / 10)
        inverso = inverso * 10 + digito

    return inverso

print("inverso de 1245 es: ", obten_inverso(1245))








"""
En la actividad "Codificando mis primeros programas II" se dio la fórmula para
 calcular el N-ésimo número de Fibonacci. La fórmula es útil para encontrar un
 número en una secuencia, pero una forma más efectiva de producir series de
 números en la secuencia es usar la relación de recurrencia FN = FN-1 + FN-2,
 con los dos primeros números de la secuencia F1 y F2 definidos como 1.
 Usando esta relación de recurrencia, se pueden calcular los primeros 7
 números de Fibonacci como sigue:
F1 = 1
F2 = 1
F3 = F1 + F2 = 1 + 1 = 2
F4 = F2 + F3 = 1 + 2 = 3
F5 = F3 + F4 = 2 + 3 = 5
F6 = F4 + F5 = 3 + 5 = 8
F7 = F5 + F6 = 5 + 8 = 13


Dado un valor N, N >= 2, mostrar los primeros N números en la secuencia
de Fibonacci.
"""


def fibo (n):

    if n < 1 :
        return
    print (1, ' ', end = '')

    if n < 2 :
        return
    print (1, ' ', end = '')

    f1 = 1
    f2 = 1
    i = 2

    while (i < n):
        temp = f1 + f2
        print(temp, ' ', end = '')
        f1 = f2
        f2 = temp
        i = i + 1


fibo(8)
