#Agrega el estilo correcto y los comentarios decuados al siguiete código




#Una función que determina, dados 2 valores, cuál es el mayor.

def mayor(num1, num2):
    if num1 > num2:
        return num1
    return num2

print(mayor(19,2))





"""
 Una función que calcula la corriente de un circuito conociendo el voltaje y
 la resistencia, suponga que el valor de la resistencia no puede ser negativo.
 corriente = voltaje / resistencia
"""

def corriente(voltaje, resistencia):
    if resistencia >= 0:
        return "Resitencia no puede ser negativo o 0"
    return voltaje / resistencia

print(corriente(19,2))

print(corriente(19,-2))








"""
Dadas tres cantidades enteras positivas, se quiere determinar las siguientes situaciones:

¿Es un triángulo? Si los valores de dichas cantidades pueden corresponder a las longitudes de los lados de un triángulo.
¿Es escaleno? En el caso de que las medidas puedan corresponder a las longitudes de los lados de un triángulo, si dicho triángulo es escaleno.
¿Es equilátero? En el caso de que las medidas puedan corresponder a las longitudes de los lados de un triángulo, si dicho triángulo es equilátero.
¿Es isósceles? En el caso de que las medidas puedan corresponder a las longitudes de los lados de un triángulo, si dicho triángulo es isósceles.
"""
def determina_triangulo(lado_a, lado_b, lado_c):

    if ((lado_a + lado_b) < lado_c) or ((lado_a + lado_c) < lado_b) or ((lado_b + lado_c) < lado_a):
        return "no es un triangulo"
    else:
        if lado_a == lado_b and lado_b == lado_c :
            return "equilatero"
        elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
            return "escaleno"
        else:
            return "isoceles"



print(determina_triangulo(2,2,5))

print(determina_triangulo(5,5,5))

print(determina_triangulo(4,5,6))

print(determina_triangulo(4,4,5))







"""
 Determinar si un año es bisiesto. Un año es bisiesto si es múltiplo
 de 4 (por ejemplo, 1984). Sin embargo, los años múltiplos de 100 sólo son
 bisiestos cuando a la vez son múltiplos de 400
 (por ejemplo, 1800 no es bisiesto, mientras que 2000 si lo es).
"""

def es_bisiesto(year):  #yo muy listo
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False


print("1800 es bisiento? ", es_bisiesto(1800))
print("2000 es bisiento?", es_bisiesto(2000))
