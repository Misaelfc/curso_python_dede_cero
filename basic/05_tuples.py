### Tuplas ###
# Las tuplas son inmutables no se pueden cambiar y se definen con paréntesis


# Definición

my_tuple = tuple() #Tupla es un conjunto de valores
my_other_tuple = ()

my_tuple = (33, 1.80, "Misael", "Flores")
print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Misael")) #Las veces que la palabra se encuentra en la tupla
print(my_tuple.index("Flores")) #Posición en la que se encuentra la tupla
print(my_tuple.index("Misael")) #Posición en la que se encuentra la tupla

# my_tuple[1] = 1.80 'tuple' object does not support item assignment 

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6]) # Da el rango de la posición de la tupla en este caso es "Flores"

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple) # Se puede convertir la tupla en lista y podría ser mutable
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
