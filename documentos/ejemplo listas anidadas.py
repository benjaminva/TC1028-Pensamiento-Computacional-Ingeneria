"""
ejemplo listas anidadas
"""

perros = ["dogo", "matsy", "cacho"] #lista normal
gatos = ["taro", "misifus"]
pericos = ["loro","sam"]


veterinaria = [perros, gatos, pericos] #lista anidada
print("\nveterinaria", veterinaria)

#modifico sub_lista y el cambio de hace también en la lista_anidada
perros.append("rufo")
print("\nperros", perros)
print("veterinaria : \n", veterinaria)

#modifico sub_lista y el cambio de hace también en la lista_anidada
veterinaria.append("PET CO")
print("\nperros", perros)
print("veterinaria : \n", veterinaria)

#sobre escribiend elementos
perros[2] = ""
print("\nperros :", perros)
print("veterinaria : \n", veterinaria)
print("perros[1] : ", perros[1])
print("veterinaria[0][1] :", veterinaria[0][1])

#cada grupo es diferente
print("\ngrupos\n")
for grupo in veterinaria:
    print(grupo)
