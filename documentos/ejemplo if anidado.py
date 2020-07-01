"""
ejemplo if anidados
"""
dinero, opcion1, corona_virus = 80, "cine",  False

print("\ncon algebra bool") #con algebra booleana

if dinero > 100 and opcion1 == "cine" and corona_virus == False :
    print("ve al cine")
elif (dinero < 100 or opcion1 == "plaza") and corona_virus == False :
    print("ve a la plaza")
elif (dinero < 100 and opcion1 == "cine") or corona_virus == True :
    print("ve a casa")
elif dinero > 100 and opcion1 == "plaza" and corona_virus == False :
    print("ve a la plaza")

print("\ncon if anidados")  #if anidados

if dinero > 100:
    if opcion1 == "cine":
        if corona_virus:
            print("ve a casa")
        else:
            print("ve al cine")
    else:
        if corona_virus:
            print("ve a casa")
        else:
            print("ve a la plaza")
else :
    if corona_virus:
        print("ve a casa")
    else:
        print("ve a la plaza")

print("\naproximación mixta") #mixto
if corona_virus :
    print("ve a la casa")
else:
    if dinero > 100 and opcion1 == "cine":
        print("ve al cine")
    else:
        print("ve a la plaza")
