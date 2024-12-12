### Regular Expressions ###
# son una poderosa herramienta utilizada para buscar, coincidir y manipular cadenas de texto basándose en patrones definidos.

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])
    
print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

# pattern = r"[lL]ección":
# Este es el patrón que describe lo que se quiere buscar en my_string.
pattern = r"[lL]ección"
# La función re.findall de la biblioteca re encuentra todas las coincidencias del patrón en la cadena my_string.
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
# re.findall: Devuelve todas las coincidencias como una lista.
print(re.findall(pattern, my_string))
# re.search: Devuelve la primera coincidencia como un objeto Match (o None si no encuentra ninguna).
print(re.search(pattern, my_string))

# \d es un metacarácter en las expresiones regulares que equivale a cualquier dígito decimal (0-9).
pattern = r"\d"
print(re.findall(pattern, my_string))

# r"\D": Busca cualquier carácter que no sea un dígito (letras, espacios, signos de puntuación, etc.).
pattern = r"\D"
print(re.findall(pattern, my_string))

# [l].*: Busca una “l” seguida de cualquier cantidad de caracteres hasta el final de la línea.
pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "aflorescastrejon@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))
