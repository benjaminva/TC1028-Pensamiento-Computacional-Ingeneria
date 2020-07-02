"""
ejemplo manipulación de strings
"""
texto = "Mi profesor de computacion come mucho"
print("texto :", texto)

#texto como una lista
print("texto[0] texto[1] :",texto[0], texto[1])
print("tamaño texto len(texto):", len(texto))
print("subrstring texto[0 : 10]:", texto[0 : 10])
temp = texto[5 : 20]
print("subrstring temp (texto[5 : 20]):", temp, "\n")

#funciones de texto
mayusculas = texto.upper()  #mayusculas
print("todo en mayusculas :", mayusculas)
minusculas = texto.lower()  #minusculas
print("todod en minusculas :", minusculas, "\n")

#separa string en varios strings
palabras = texto.split()  #separa por espacios
print("arreglo de strings ' ':", palabras)
palabras = texto.split("e")  #separa por letra 'a'
print("arreglo de strings 'e':", palabras, "\n")

#busca contenido en una cadena
if "es" in texto:
    print("el texto contiene es\n")
else:
    print("el texto no contiene es\n")

#agrega texto
oracion = texto + ", y me gustan los video juegos"
print("oracion:\n", oracion)

#remplaza el contenido de una cadena
nueva_oracion = oracion.replace("Benjamin", "Taro")
print("oracion con remplazo:\n", nueva_oracion)
