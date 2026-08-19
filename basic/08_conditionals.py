### Conditionals ###
# l
# Los condicionales son estructuras que permiten tomar decisiones dentro de un programa según ciertas condiciones. Esto se hace evaluando una expresión booleana (una que resulta en True o False) y ejecutando un bloque de código si esa condición se cumple.

# if Se usa para ejecutar un bloque de código si la condición es verdadera.

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 o menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continua")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    # La expresión not my_string evalúa si my_string es falsa, lo cual sucede si la cadena está vacía.
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")

# Conditionals
"""
By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true
Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
"""
# If Condition
# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

# If Else
# If condition is true the first block will be executed, if not the else condition will run.
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If Elif Else
# In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Short Hand
a = 3
# first condition met, 'A is positive' will be printed
print('A is positive') if a > 0 else print('A is negative')

# Nested Conditions
# Conditions can be nested
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
