### Tuplas ###
# Las tuplas son inmutables no se pueden cambiar y se definen con paréntesis


# Definición

my_tuple = tuple()  # Tupla es un conjunto de valores
my_other_tuple = ()

my_tuple = (33, 1.80, "Misael", "Flores")
print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

# Las veces que la palabra se encuentra en la tupla
print(my_tuple.count("Misael"))
print(my_tuple.index("Flores"))  # Posición en la que se encuentra la tupla
print(my_tuple.index("Misael"))  # Posición en la que se encuentra la tupla

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

# Da el rango de la posición de la tupla en este caso es "Flores"
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

# Se puede convertir la tupla en lista y podría ser mutable
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.append("AbrahamDev")
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined

"""
Tuples
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
+ operator: to join two or more tuples and to create a new tuple
"""
# Creating a Tuple
# Empty tuple: Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values
# syntax
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Slicing tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits = fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# Changing Tuples to Lists
# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)  # True
print('apple' in fruits)  # False
# fruits[0] = 'apple'  # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
# ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
print(fruits_and_vegetables)

# Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# print(fruits)  # NameError: name 'fruits' is not defined
