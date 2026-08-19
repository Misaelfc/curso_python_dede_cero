### Dictionaries ###

# Definición proporciona una forma eficiente de organizar y acceder a la información mediante una clave única asociada a cada valor y es en pares de valores.

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Misael",
                 "Apellido": "Flores", "Edad": 33, 1: "Python"}

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

# Imprime el valor y le da salida en consola en este caso 1.8
print(my_dict[1])
# Imprime el valor y le da salida en consola en este caso 1.Misael
print(my_dict["Nombre"])

# Imprime un booleano porque busca siempre las keys que los values en este caso da False
print("Flores" in my_dict)
print("Apellido" in my_dict)  # Booleano da True

# Inserción

# Inserta nuevos keys y values, key: calle y value: Calle Melón en el dict.
my_dict["Calle"] = "Calle Melón"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Abraham"  # Actualiza el nombre del diccionario
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]  # Elimina el key de calle
print(my_dict)

# Otras operaciones

print(my_dict.items())  # Obtiene pares clave-valor como tuplas.
# Las keys obtiene las claves del diccionario. son Nombre, Apellido, Edad, Lenguajes, y 1
print(my_dict.keys())
print(my_dict.values())  # Obtiene los valores del diccionario.

my_list = ["Nombre", 1, "Piso"]

# El método dict.fromkeys() se utiliza para crear un diccionario con claves provenientes de un iterable (como una lista) y asignarles un valor por defecto, que es None si no se especifica otro.
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

# Dará salida solo a los keys y por defecto da None como valor del diccionario my_dict
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

# Si quieres que todas las claves tengan un valor específico, puedes pasarlo como segundo argumento a fromkeys():
my_new_dict = dict.fromkeys(my_dict, "AbrahamDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))  # Se crea una tupla inmutable de los keys
print(set(my_new_dict))  # Se crea el set del diccionario nuevo

# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
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

# Dictionary Length
# It checks the number of 'key: value' pairs in the dictionary.
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
print(len(person))  # 7

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.
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
print(person['first_name'])  # Abraham
print(person['last_name'])  # Flores
print(person['age'])        # 35
print(person['country'])    # México
print(person['is_marred'])  # True
# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'])
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
# print(person['city'])       # Error

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.

print(person.get('first_name'))  # Abraham
print(person.get('country'))    # México
# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('skills'))
print(person.get('city'))   # None

# Adding Items to a Dictionary
# We can add new key and value pairs to a dictionary
person['job_title'] = 'Data Analyst'
person['skills'].append('SQL')
print(person)

# Modifying Items in a Dictionary
# We can modify items in a dictionary
person['first_name'] = 'Misael'
person['age'] = 33
print(person)

# Removing Items from a Dictionary
# We can remove items from a dictionary using the pop() method. The pop() method removes the item with the specified key name.
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
# del person['is_married']

# Deleting a Dictionary
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct

# Getting Dictionary Keys as a List
# We can get all the keys as a list using the keys() method.
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
# dict_keys(['first_name', 'last_name', 'age', 'country', 'is_marred', 'skills', 'address'])
print(person.keys())
print(list(person.keys()))

# Getting Dictionary Values as a List
# We can get all the values as a list using the values() method.
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
# dict_values(['Abraham', 'Flores', 35, 'México', True, ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], {'street': 'Space street', 'zipcode': '02210'}])
print(person.values())
