### Loops ###

# Definición: los loops o bucles son estructuras de control que permiten repetir un bloque de código varias veces. Son fundamentales para automatizar tareas repetitivas o para procesar datos en colecciones (como listas, tuplas o diccionarios). Python soporta dos tipos principales de bucles: for y while.

# While El bucle while repite un bloque de código mientras una condición sea verdadera (True).

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2  # += es número de veces del conteo
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    # En cada iteración, my_condition se incrementa en 1 (+= 1).
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break  # break: rompe el bucle inmediatamente, dejando de ejecutarse.
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

# La variable element toma, uno a uno, los valores de los elementos de la lista.
for element in my_list:
    print(element)

my_tuple = (33, 1.80, "Misael", "Flores", "Misael")

for element in my_tuple:
    print(element)

my_set = {"Misael", "Flores", 33}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Misael", "Apellido": "Flores", "Edad": 33, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    # Cuando la clave es "Edad", el continue salta la línea print("Se ejecuta"), por lo que no se imprime en esa iteración.
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    # Al final del bucle, como no hay un break, se ejecuta el bloque else.
    print("El bluce for para diccionario ha finalizado")

# Loops
"""
Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

while loop
for loop
"""
count = 0
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4

# if we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue - Part 1
# Break: We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

# For Loop
# A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# Using For loop on string
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

# Using For loop on tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    'first_name': 'Abraham',
    'last_name': 'Flores',
    'age': 35,
    'country': 'México',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out

# Using For Loop in set
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    # for short hand conditions need both if and else statements
    print('Next number should be ', number +
          1) if number != 5 else print("loop's end")
print('outside the loop')

# The Range Function
# The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2 arguments indicate start and end of the sequence, step set to default 1
st = set(range(1, 11))
print(st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)  # {0, 2, 4, 6, 8, 10}

# for backward from start to end
lst = list(range(11, 0, -2))
print(lst)  # [11,9,7,5,3,1]

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# For Else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# Pass
# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass
