# 1. Crea un set con los números del 1 al 5 e imprímelo.
set_numbers = {1, 2, 3, 4, 5}
print(set_numbers)
# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
set_numbers.add(6)
print(set_numbers)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
set_numbers.add(5)
print(set_numbers)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
set_numbers = {1, 2, 3, 4, 5}
print(3 in set_numbers)  # Output: True
# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
set_numbers.remove(4)
print(set_numbers)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
set_numbers.clear()
print(len(set_numbers))  # Output: 0
# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
fruits = {"manzana", "naranja", "plátano"}
fruits_list = list(fruits)
print(fruits_list[0])
# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = {1, 2, 3}
del my_set
try:
    print(my_set)
except NameError:
    print("my_set no está definido")  # Output: my_set no está definido
