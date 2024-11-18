### Listas ###

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
print(my_list.count(30)) #Count cuenta las veces que el número esta en el parentesis 
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Misael"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("Misael Flores") #El método .append() se usa para añadir un elemento al final de una lista.
print(my_other_list)

my_other_list.insert(1, "Rojo") #El método .insert(posición, elemento) en Python agrega un elemento a una lista en una posición específica.
print(my_other_list)

my_other_list[1] = "Azul" #"Azul" reemplaza el elemento en la posición 1 de la lista con el valor "Azul".
print(my_other_list)

my_other_list.remove("Azul") #Remueve el elemento "Azul de la lista"
print(my_other_list)

my_list.remove(30) #Elimina o remueve un número en este caso el 30 de la lista
print(my_list)

print(my_list.pop()) #Elimina y devuelve el último elemento de una lista    
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element) # Muestra: 62
print(my_list) # Muestra 35, 24, 52, 30 de la lista

del my_list[2] #Elimina la posición de 2 contando como 0 el primer elemento, en este caso eliminará el número 52 de la lista
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

print(my_new_list.reverse())
print(my_new_list)

my_new_list.sort() #Ordena los números de la lista en este caso de menor a mayor
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))