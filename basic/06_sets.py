### Sets ###

# Definición

# Un set es una estructura de datos en Python que:
# Almacena elementos únicos: No permite duplicados.
# No tiene orden: Los elementos no tienen una posición fija ni puedes acceder a ellos mediante índices.
# Es mutable: Puedes agregar o eliminar elementos después de su creación.
# Se define usando llaves {} o el constructor set().

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Misael", "Flores", 33}
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("AbrahamDev")
print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("AbrahamDev")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

# in permite buscar en el set y lanza un booleano en consola
print("Misael" in my_other_set)
print("Misa" in my_other_set)

# Eliminación

my_other_set.remove("Misael")  # Elimina o boarra el elemento con remove
print(my_other_set)

my_other_set.clear()  # clear limpia todo el set
print(len(my_other_set))  # len sale como 0 en consola

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

# El set siempre imprime de forma desordenada en consola
my_set = {"Misael", "Flores", 33}
my_list = list(my_set)  # Se convierte el set en lista []
print(my_list)
# El [0] imprimirá el primer elemento del set aleatoriamente porque el set nunca sale ordenado como tal.
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

# se utiliza para realizar la unión de dos o más conjuntos (sets).
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union(
    {"JavaScript", "C#"}))  # union Une todos los elementos del set
# difference muestra los elementos que sean diferentes en los sets.
print(my_new_set.difference(my_set))

"""
Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
"""
# Creating a set with initial items
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's Length
print(len(fruits))  # Output: 4

# Accessing Items in a Set
# Checking an Item
# To check if an item exist in a list we use in membership operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)  # True

# Adding Items to a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)  # Output: {'banana', 'orange', 'mango', 'lemon', 'lime'}

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
# Output: {'banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print(fruits)

# Removing Items from a Set
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)
# If we are interested in the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)

# Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)  # set()

# Deleting a Set
# If we want to delete the set itself we use del operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
try:
    print(fruits)
except NameError as e:
    print(e)  # Output: name 'fruits' is not defined

## Converting List to Set ##
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)  # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

# Joining Sets
# We can join two sets using the union() or update() method or | symbol .
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
# {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
print(fruits.union(vegetables))
# or using this : print(fruits | vegetables)

# Update This method inserts a set into a given set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
# {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'on
print(fruits)

# Finding Intersection Items
# Intersection returns a set of items which are in both the sets or using & symbol. See the example
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)  # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon
print(python.intersection(dragon))  # {'o', 'n'}
