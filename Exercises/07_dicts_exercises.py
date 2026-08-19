# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
person_dict = {
    "name": "Abraham",
    "age": 35,
    "country": "México"
}
print(person_dict)
# 2. Accede al valor de la clave name en el diccionario.
print(person_dict["name"])
# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
person_dict["job"] = "Programador"
print(person_dict)
# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
person_dict["age"] = 38
print(person_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
person_dict.pop("country")
print(person_dict)
# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
squares_dict = {i: i**2 for i in range(1, 6)}
print(squares_dict)
# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
person_check_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in person_check_dict)
# 8. Imprime solo las claves del diccionario.
print(person_check_dict.keys())
# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
person_check_dict_keys_list = list(person_check_dict.keys())
print(person_check_dict_keys_list)
# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
new_dict = dict.fromkeys(["name", "age", "job"], "Desconocido")
print(new_dict)
