### Functions ###

# Deficiión: es un bloque de código reutilizable que realiza una tarea específica. Las funciones ayudan a organizar y estructurar el código, facilitando la lectura, el mantenimiento y la reutilización.

def my_function():
    print("Esto es una función")


# Siempre en las funciones para que salga en consola después de imprimir tienes que llamar la función junto con su paréntesis.
my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")  # En str solo se juntan los números no los suma.
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Flores", name="Misael")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Misael", "Flores")
print_name_with_default("Misael", "Flores", "AbrahamDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

# Funciones
# Definir funciones
# Una función es un bloque de código reutilizable o una sentencia de programación que realiza una tarea específica. Para definir o declarar una función, Python provee la palabra clave def. La sintaxis para definir funciones es la siguiente. El código dentro de la función solo se ejecuta cuando la llamamos o la invocamos.

# Declarar y llamar a una función
# Cuando creamos una función, decimos que la declaramos. Cuando la usamos, decimos que la llamamos o invocamos. Las funciones pueden tener parámetros o no.
# Función sin parámetros


def generate_full_name():
    first_name = 'Abraham'
    last_name = 'Flores'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()  # Llamar a una función


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()

# Funciones que retornan valores - Parte 1
# Una función también puede devolver un valor; si una función no tiene return, devuelve None. Reescribamos las funciones anteriores usando return. A partir de ahora, cuando llamemos a la función y la imprimamos, obtendremos un valor.


def generate_full_name():
    first_name = 'Abraham'
    last_name = 'Flores'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())

# Funciones con parámetros
# En una función podemos pasar diferentes tipos de datos (números, cadenas, booleanos, listas, tuplas, diccionarios o sets) como parámetros.
# Parámetro único: si una función necesita un parámetro, la llamamos con un argumento.


def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings('Abraham'))  # Abraham, welcome to Python for Everyone!


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050

# Dos parámetros: una función puede no tener parámetros o tener uno o varios. Si necesita dos parámetros, la llamamos con dos argumentos.


def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print('Full Name: ', generate_full_name('Abraham', 'Flores'))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum


print('Sum of two numbers: ', sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(2021, 1819))


def weight_of_object(mass, gravity):
    # El valor necesita convertirse a cadena primero
    weight = str(mass * gravity) + ' N'
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# Pasar argumentos por clave y valor


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)


print(print_fullname(firstname='Abraham', lastname='Flores'))


def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)


print(add_two_numbers(num2=3, num1=2))  # el orden no importa

# Devolver números:


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(2019, 1819))

# Devolver booleanos: Ejemplo:


def is_even(n):
    if n % 2 == 0:
        print('even')
        return True    # la instrucción return detiene la ejecución adicional en la función
    return False


print(is_even(10))  # True
print(is_even(7))  # False


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))

# Número arbitrario de argumentos


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # equivalente a total = total + num
    return total


print(sum_all_nums(2, 3, 5))  # 10

# Función como parámetro de otra función
# Puedes pasar una función como argumento


def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))  # 27
