# 1. Usa un bucle while para imprimir los números del 1 al 10.
my_condition = 0
while my_condition < 10:
    print(my_condition + 1)
    my_condition += 1
# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)
# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
my_sum = 0
i = 1
while i <= 100:
    my_sum += i
    i += 1
print(my_sum)
# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
language = "Python"
for char in language:
    print(char)
# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
num = 1
while num <= 50:
    if num % 7 == 0:
        print(num)
        break
    num += 1
# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
dictionary = {"name": "Brais", "age": 37, "country": "Galicia"}
for key in dictionary:
    print(key)
# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
num = 2
while num <= 20:
    print(num)
    num += 2
# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for i in range(10, 0, -1):
    print(i)
# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
count = 0
my_list = [30, 10, 30, 20, 30, 40]
for element in my_list:
    if element == 30:
        count += 1
print(count)
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
names = ["Alice", "Bob", "Charlie", "Brais", "David"]
for name in names:
    if name == "Brais":
        break
    print(name)
