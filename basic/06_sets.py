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

print("Misael" in my_other_set) # in permite buscar en el set y lanza un booleano en consola
print("Misa" in my_other_set)

# Eliminación

my_other_set.remove("Misael") #Elimina o boarra el elemento con remove
print(my_other_set)

my_other_set.clear() # clear limpia todo el set
print(len(my_other_set)) # len sale como 0 en consola

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Misael", "Flores", 33} #El set siempre imprime de forma desordenada en consola
my_list = list(my_set) #Se convierte el set en lista []
print(my_list)
print(my_list[0]) #El [0] imprimirá el primer elemento del set aleatoriamente porque el set nunca sale ordenado como tal.

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set) #se utiliza para realizar la unión de dos o más conjuntos (sets). 
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # union Une todos los elementos del set 
print(my_new_set.difference(my_set)) # difference muestra los elementos que sean diferentes en los sets.
