### Listas ###
# Las listas son mutables y se pueden cambiar y se definen con corchetes

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [33, 1.80, "Misael", "Flores"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
# Count cuenta las veces que el número esta en el parentesis
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Misael"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
# print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

# El método .append() se usa para añadir un elemento al final de una lista.
my_other_list.append("Misael Flores")
print(my_other_list)

# El método .insert(posición, elemento) en Python agrega un elemento a una lista en una posición específica.
my_other_list.insert(1, "Rojo")
print(my_other_list)

# "Azul" reemplaza el elemento en la posición 1 de la lista con el valor "Azul".
my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")  # Remueve el elemento "Azul de la lista"
print(my_other_list)

# Elimina o remueve un número en este caso el 30 de la lista
my_list.remove(30)
print(my_list)

print(my_list.pop())  # Elimina y devuelve el último elemento de una lista
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)  # Muestra: 62
print(my_list)  # Muestra 35, 24, 52, 30 de la lista

# Elimina la posición de 2 contando como 0 el primer elemento, en este caso eliminará el número 52 de la lista
del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

print(my_new_list.reverse())
print(my_new_list)

my_new_list.sort()  # Ordena los números de la lista en este caso de menor a mayor
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))

"""
How to Create a List
In Python we can create lists in two ways:
"""
# Using list built-in function
# syntax
lst = list()
empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0

# Using square brackets, []
# syntax
lst = []  # this is an empty list, no item in the list
print(len(lst))  # 0

# Lists with initial values. We use len() to find the length of a list.
# list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter',
                   'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# Lists can have items of different data types
# list containing different data types
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]

first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden',
             'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Removing Items Using Pop
# The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# Clearing List Items
# The clear() method empties the list:

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# Joining Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# Plus Operator (+)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
# ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(fruits_and_vegetables)

"""
    Sorting List Items
To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

sort(): this method modifies the original list
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
# sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
print(fruits)
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]
