# comenta en PEP 8 y haz tus notas.

"""
Desarrolla la función formato_web, que recibe una cadena de texto y la
convierte en texto de una pagina web para lo anterior necesitas varias funciones:

La función inserta_html que recibe una cadena de texto e insert al
principio de la cadena "<html><body>" y al final "</body ></html>" de tal forma
que si se manda a llamar insert_html("Hola mundo"), lo que devolvería la función
 sería "<html><body> Hola Mundo </body ></html>"

Corre la función formato_web y copia la salida de la consola a un archivo de texto.
Salva el archivo con la extensión .html y arrastra el archivo a tu navegadro web.
Voila! ya haz hecho tu primer código generador de páginas web."""

def inserta_html(texto):
    return "<html><body>" + texto + "</body ></html>"


def inserta_saltos(texto):

    return texto.replace("\n", "<Br>" )

texto = """ Nadie rebaje a lágrima o reproche
esta declaración de la maestría
de Dios, que con magnífica ironía
me dio a la vez los libros y la noche.

De esta ciudad de libros hizo dueños
a unos ojos sin luz, que sólo pueden
leer en las bibliotecas de los sueños
los insensatos párrafos que ceden

las albas a su afán. En vano el día
les prodiga sus libros infinitos,
arduos como los arduos manuscritos
que perecieron en Alejandría.
"""

def mi_pag(texto):
    lineas = texto.split("\n")
    titulo = " <h1> " + lineas[0] + " </h1> "
    texto = titulo + texto

    texto = inserta_saltos(texto)
    texto = inserta_html(texto)
    print(texto)

mi_pag(texto)









"""
La función es_palindromo que recibe una cadena y devuelve True si la cadenas es
palíndromo o False en caso contratio. Por ejemplo, "Anita lava la tina" es un
palíndromo. Ignora los signos de puntuación, espacios en blanco,
las mayúsculas y minúsculas.
"""
def es_palindromo(linea):
    linea = linea.replace(" ", "")
    linea = linea.replace(".", "")
    linea = linea.replace(",", "")
    linea = linea.replace("!", "")
    linea = linea.replace("?", "")
    linea = linea.lower()

    fin = len(linea)-1
    i = 0
    while i != fin :
        if linea[i] != linea[fin] :
            return False
        i = i + 1
        fin = fin - 1
    return True

#print(es_palindromo("Anita lava la tina"))

#print(es_palindromo("Anita lava la tinwweda"))
