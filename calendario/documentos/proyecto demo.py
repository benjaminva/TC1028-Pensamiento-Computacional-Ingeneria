#proyecto "carreras peligrosas"
#Autor: Benjamin Valdes Aguirre
#Matricula: A00882900

#comentarios generales del programa

#Primero van todas las funciones que generaron.

#programas con listas ===========================================================
def crea_lista_anidada(exterior, interior):

    """ crea una lista anidada de 2 niveles """
    
    lista_exterior = []
    
    i = 0
    while(i < exterior):
        lista_interior = []
        
        j = 0
        while(j < interior):
            lista_interior.append(int(input()))
            j = j + 1
        
        lista_exterior.append(lista_interior)
        i = i + 1
       
    return lista_exterior
#=================================================================================== 

#correccion programas con listas y con listas anidadas y matrices.==================    
def suma_diagonal(matriz):
 
    """suma la diagonal de una matriz"""
 
    if len(matriz) != len(matriz[0]):
        return False 
        
    sum = 0
    i = 0
    for line in matriz:
        
        j = 0
        for number in line:
            if i == j:
                sum = sum + number
            j = j + 1
        
        i = i + 1
    return sum
    
#===================================================================================   
    
#correcion Programas que involucran cálculos y con estructuras de repetición.=======
def potencia(x,n):

    """ culcula la potencia de un número usando ciclos"""

    i = 0
    pot = 1.0
    if(n > 0):
        while(i < n):
            pot = pot * x
            i = i + 1
    else:
        while(0 > n):
            pot = pot * 1.0/x
            n = n + 1    
    return pot
#===================================================================================

#correcion Programas con funciones y pruebas  ======================================
def dolares_a_pesos(dolares):
    """ convierte dolares a pesos"""
    
    return dolares * 21.5
    
#caso de prueba: 
#dolares_a_pesos(20) -> 420
#dolares_a_pesos(1)  -> 21.5 
#dolares_a_pesos(-10) -> -215

#===================================================================================

    
def costo_hotel(noches):
    """ devuelve el costo total en dolares """
    
    return noches * 170.0

#correcion Programas con funciones y pruebas  ======================================    
def costo_avion(pasajeros):
    """  devuelve el costo total de los aviones en dolares"""
    
    return pasajeros * 315

#caso de prueba: 
#costo_avion(10)  -> 3150
#costo_avion(1)   -> 315
#costo_avion(-5)  -> -1575
#====================================================================================
def costo_viaje(noches, pasajeros):
    """ devuelve el costo aproximado en pesos del hotel y el avion """
    
    hotel = dolares_a_pesos(costo_hotel(noches))
    avion = dolares_a_pesos(costo_avion(pasajeros))
    
    return hotel + avion 
   
#correcion programas que involucran estructuras de decisión	=========================
def valida(num):
    """ valida que el número sea mayor que cero """

    if(num > 0.0):
        return True
    else:
        return False
#====================================================================================
        

def corriente(voltaje, resistencia):
    """ calcula la corriente electrica según la ley Ohm """
    
    if(valida(resistencia)):
        return voltaje/resistencia
    else:
        return -1
        
        


def get_nombre(linea):

    """extrae el nombre de un judar de la línea"""

    palabras = linea.split('\t')
    nick = palabras[0]
    nombre = palabras[1]
    
    return nombre

def get_sueldo(linea):

    """extrae el sueldo y lo regresa como float"""

    index = linea.find("$")
    numero = linea[index+1:]
    valor = numero.replace(',','')

    return float(valor)
    

def escribe_tabla(origen, destino):
    """escribe el nombre y el sueldo de un jugador 
    en otro archivo"""

    f = open(origen)
    lineas = f.readlines()
    f.close()

    f = open(destino, "w")
    
    for linea in lineas:
        f.write("nombre %s sueldo %s \n" %(get_nombre(linea),get_sueldo(linea)))
    
    f.close()


#parte principal del código donde debe de estar la lógica principal del programa. 

origen = input()
destino = input()
escribe_tabla(origen,destino)