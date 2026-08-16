# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola línea.
cadena1 = "Hola"
cadena2 = "Python"
space = " "
resultado = cadena1 + space + cadena2
print(resultado)
# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
cadena_con_salto = "Primera línea\nSegunda línea"
print(cadena_con_salto)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
cadena_formateada = f"Mi nombre es Abraham, mi apellido es Flores y tengo 30 años."
print(cadena_formateada)
# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprímelos uno por uno.
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# 6. Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
lenguaje_slice = "Programación"[3:8]
print(lenguaje_slice)
# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
lenguaje_invertido = "Python"[::-1]
print(lenguaje_invertido)
# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprímela.
cadena_mayusculas = "aprendiendo python".upper()
print(cadena_mayusculas)
# 9. Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".
cuenta_n = "Programación en Python".count("n")
print(cuenta_n)
# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.
print("12345".isnumeric())
