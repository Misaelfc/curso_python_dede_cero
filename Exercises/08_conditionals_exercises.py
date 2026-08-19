# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
x = 7
if x > 0:
    print("El número es positivo")
elif x < 0:
    print("El número es negativo")
else:
    print("El número es cero")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
# usuario_edad = int(input("Ingrese su edad: "))
# if usuario_edad >= 18:
#   print("Eres mayor de edad")
# else:
#    print("Eres menor de edad")
# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
x = ""
if not x:
    print("La cadena de texto está vacía")
# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
a = 7
b = 9
if a > b:
    print("El primer número es mayor")
elif a < b:
    print("El segundo número es mayor")
else:
    print("Los números son iguales")
# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
a = 15
if a % 3 == 0 and a % 5 == 0:
    print("El número es divisible por 3 y por 5")
# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
user_number = 9
if user_number % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
vote_age = 17
if vote_age >= 18:
    print("Puede votar")
elif vote_age == 16 or vote_age == 17:
    print("Puede votar con permiso especial")
else:
    print("No puede votar")
# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
user_password = "1234"
if user_password == "1234":
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
num = 15
if num >= 10 and num <= 20:
    print("El número está entre 10 y 20")
# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
semaforo_color = "rojo"
if semaforo_color == "rojo":
    print("Detenerse")
elif semaforo_color == "amarillo":
    print("Estar alerta")
elif semaforo_color == "verde":
    print("Avanzar")
