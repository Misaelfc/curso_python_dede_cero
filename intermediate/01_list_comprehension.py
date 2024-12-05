### List Comprehension ###
# Son una forma compacta y elegante de crear listas a partir de secuencias o iterables. Permiten aplicar operaciones, condiciones, o transformaciones de manera concisa dentro de una misma expresión.

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Definición

my_list = [i + 1 for i in range(8)] #Transforma una lista en otra lista y suma uno al final
print(my_list) # Da salida [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i * 2 for i in range(8)] # Va de dos en dos hasta el rango 8 
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)] # Se va multiplicando por el mismo elemento
print(my_list) # Da [0, 1, 4, 9, 16, 25, 36, 49]

def sum_five(number): #La función sum_five toma un argumento (number) y devuelve ese número incrementado en 5. 
    return number + 5

my_list = [sum_five(i) for i in range(8)] #La función devuelve el resultado de i + 5, que se agrega a la lista.
print(my_list) #Da salida a [5, 6, 7, 8, 9, 10, 11, 12]
