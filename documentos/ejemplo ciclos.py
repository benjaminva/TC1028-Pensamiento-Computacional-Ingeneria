"""
ejemplo ciclos
"""

#ciclo basico
i = 10  #contador
while i > 0:   #condicion
    print("i vale :", i)
    i = i - 1 # incremento
print("")

#ciclo limite
i = 0  #contador
lim = 6  #limite
while i < lim:   #condicion
    print("i vale :", i)
    i = i + 1 # incremento
print("")

#ciclo acumulador
i = 0  #contador
lim = 4  #limite
acum  = 0 # acumulador
while i < lim:   #condicion
    acum = acum + i * 2
    i = i + 1 # incremento
print("acumulador ",acum, "\n")


#ciclo evento o bander
i = 0  #contador
bandera = True  #bandera
while bandera:  #condicion/evento
    i = i + 1 # incremento
    print("i vale :", i)
    if i%5 == 0 :
        bandera = False
        print("cambio de bandera")
