# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprí­mela.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)
# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
tuple2 = (100, 200, 300, 400, 500)
print(tuple2[1])
# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
tuple3 = (1, 2, 3)
try:
    tuple3[0] = 10
except TypeError as e:
    print(f"Error: {e}")
# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
tuple4 = (1, 2, 3, 3, 4, 5, 3)
print(tuple4.count(3))
# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
tuple_languages = ("Java", "Python", "JavaScript", "Python")
print(tuple_languages.index("Python"))
# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tuple5 = (1, 2, 3)
tuple6 = (4, 5, 6)
tuple7 = tuple5 + tuple6
print(tuple7)
# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
print(my_tuple[2:4])
# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
tuple_colors = ("rojo", "verde", "azul")
list_colors = list(tuple_colors)
list_colors[1] = "amarillo"
tuple_colors = tuple(list_colors)
print(tuple_colors)
# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(f"Error: {e}")
# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tuple_single = (100,)
print(tuple_single)
