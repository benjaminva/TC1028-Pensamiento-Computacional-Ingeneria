"""
ejemplo condicional if
"""
#defino variables a comparar
edad_goku = 21
edad_roshi = 75
edad_gohan = 9
planeta_picoro = "namecusei"
planeta_kami_sama = "namecusei"
planeta_goku = "vegueta"
print("")
#comparando numeros
if edad_goku > 18 :
    print("goku es mayor de edad")

if  edad_gohan > 18 :
    print("gohan es mayor de edad")

if  edad_roshi> 18 :
    print("roshi es mayor de edad")
print("")

#comparando strings
if planeta_goku == planeta_kami_sama:
    print ("goku y camisama son paisanos")

if planeta_picoro == planeta_kami_sama:
    print ("picoso y kami sama son paisanos")
print("")

#comparaciones compuestas (algebra booleana)
planeta = "vegueta"

if planeta != "namecusei" or planeta != "vegueta":
    print("planeta tierra")
elif planeta == "namecusei":
    print("planeta namecusei")
else:
    print("veguueta")
