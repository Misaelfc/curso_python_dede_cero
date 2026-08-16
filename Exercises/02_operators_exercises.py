# 1. Realiza las siguientes operaciones aritméticas:
Suma = 15 + 25
Resta = 50 - 22
Multiplicación = 8 * 7
División = 100 / 20

print("Suma: ", Suma)
print("Resta: ", Resta)
print("Multiplicación: ", Multiplicación)
print("División: ", División)

# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.
remainder = 37 % 5
print("Resto de la división de 37 entre 5: ", remainder)

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase " es mi número favorito". Imprime el resultado.
numero = 7
frase = str(numero) + " es mi número favorito"
print(frase)

# 4. Repite la palabra "Python" 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
palabra = "Python " * 10
print(palabra)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
resultado = a > b
print("¿Es a mayor que b?: ", resultado)
# 6. Compara dos cadenas de texto ("apple" y "banana") usando los operadores > y < y explica cuál tiene mayor orden alfabético.
x = "apple"
y = "banana"
resultado_mayor = x > y
print("¿apple es mayor que banana?: ", resultado_mayor)
# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.
comparacion_logica = 10 > 5 and 10 < 20
print("¿10 es mayor que 5 y menor que 20?: ", comparacion_logica)
# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.
comparacion_logica_or = 7 < 3 or 7 > 5
print("¿7 es menor que 3 o mayor que 5?: ", comparacion_logica_or)

# 9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?
operador_not = not (15 > 20)
print("¿15 no es mayor que 20?: ", operador_not)
# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
resultado_expresion = (5 * 3) + 2
comparacion_combinada = resultado_expresion > 10 and resultado_expresion < 20
print("¿El resultado de la expresión es mayor que 10 y menor que 20?: ",
      comparacion_combinada)
