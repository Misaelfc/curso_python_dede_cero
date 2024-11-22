### Loops ###

#Definición: los loops o bucles son estructuras de control que permiten repetir un bloque de código varias veces. Son fundamentales para automatizar tareas repetitivas o para procesar datos en colecciones (como listas, tuplas o diccionarios). Python soporta dos tipos principales de bucles: for y while.

# While El bucle while repite un bloque de código mientras una condición sea verdadera (True).

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 #+= es número de veces del conteo
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")
    
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1 #En cada iteración, my_condition se incrementa en 1 (+= 1).
    if my_condition == 15:
        print("Se detiene la ejecución")
        break # break: rompe el bucle inmediatamente, dejando de ejecutarse.
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: #La variable element toma, uno a uno, los valores de los elementos de la lista.
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
    if element == "Edad": #Cuando la clave es "Edad", el continue salta la línea print("Se ejecuta"), por lo que no se imprime en esa iteración.
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado") #Al final del bucle, como no hay un break, se ejecuta el bloque else.
