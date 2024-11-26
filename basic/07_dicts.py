### Dictionaries ###

# Definición proporciona una forma eficiente de organizar y acceder a la información mediante una clave única asociada a cada valor y es en pares de valores.

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Misael", "Apellido": "Flores", "Edad": 33, 1: "Python"}

my_dict = {
    "Nombre": "Misael",
    "Apellido": "Flores",
    "Edad": 33,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.80
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1]) #Imprime el valor y le da salida en consola en este caso 1.8
print(my_dict["Nombre"]) #Imprime el valor y le da salida en consola en este caso 1.Misael

print("Flores" in my_dict) #Imprime un booleano porque busca siempre las keys que los values en este caso da False
print("Apellido" in my_dict) #Booleano da True

# Inserción

my_dict["Calle"] = "Calle Melón" #Inserta nuevos keys y values, key: calle y value: Calle Melón en el dict.
print(my_dict)

# Actualización

my_dict["Nombre"] = "Abraham" #Actualiza el nombre del diccionario
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"] #Elimina el key de calle
print(my_dict)

# Otras operaciones

print(my_dict.items()) #Obtiene pares clave-valor como tuplas.
print(my_dict.keys()) #Las keys obtiene las claves del diccionario. son Nombre, Apellido, Edad, Lenguajes, y 1
print(my_dict.values()) #Obtiene los valores del diccionario.

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) #El método dict.fromkeys() se utiliza para crear un diccionario con claves provenientes de un iterable (como una lista) y asignarles un valor por defecto, que es None si no se especifica otro.
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict) #Dará salida solo a los keys y por defecto da None como valor del diccionario my_dict
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, "AbrahamDev") #Si quieres que todas las claves tengan un valor específico, puedes pasarlo como segundo argumento a fromkeys():
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict)) #Se crea una tupla inmutable de los keys
print(set(my_new_dict)) #Se crea el set del diccionario nuevo

