"""
ejemplo listas
"""

#llista de puros numeros
lista = [11,12,13,14,15]
print("lista: ",lista)

#agregar elementos
lista.append(50)
print("lista: ", lista)

#tamaño de una lista  con len()
print("tamaño lista", len(lista))

#consultar  elementos
print("elemento 0", lista[0])
print("elemento 2", lista[2])
print("elemento 5", lista[5])

print("elemento -1", lista[-1]) #va en reversa
print("elemento -2", lista[-2])

#lista de strings
lista_palabras = ["hola", "me", "llamo", "Barret"]
print("lista palabras: ",lista_palabras)

#lista mixta
lista_mixta = ["tengo", 40, "años"]
print("lista mixta: ",lista_mixta)
