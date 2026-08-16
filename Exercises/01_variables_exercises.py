# 1. Declara y asigna valores a las siguientes variables:
# 	name: una cadena que contenga tu nombre.
# 	age: un número entero que represente tu edad.
# 	height: un número flotante que represente tu altura.
# 	Imprime cada variable en una línea separada.

name = "Misael"
age = 33
height = 1.80
print(f"Mi nombre es: {name}")
print(f"Mi edad es: {age}")
print(f"Mi altura es: {height}")

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
age_str = str(age)
print("Tengo " + age_str + " años.")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = True
print(f"¿Soy estudiante? {is_student}")
# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
full_name = "Abraham Misael Flores Castrejón"
print(f"Mi nombre completo tiene {len(full_name)} caracteres.")
# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, surname, city = "Misael", "Flores", "México"
print(f"Mi nombre es: {name} {surname} y soy de {city}.")
# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.
# color = input("¿Cuál es tu color favorito? ")
# print(color)

# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "manzana"
print(f"Mi fruta favorita es: {fruit}")
fruit = "banana"
print(f"Mi fruta favorita es: {fruit}")
# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 17.99
price_int = int(price)
print(f"El precio como número entero es: {price_int}")
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address_len = len("Calle Falsa 123, Ciudad de México")
print(f"La longitud de la dirección es: {address_len} caracteres.")
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = 9981807936
print(f"El número de teléfono es: {phone}")
phone = 9981807937
print(f"El nuevo número de teléfono es: {phone}")
print(f"El tipo de la variable phone es: {type(phone)}")
