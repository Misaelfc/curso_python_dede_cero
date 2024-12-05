### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0: # El signo % es para sacar múltiplos
            print("fizzbuz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)
            
fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    # Convertir las palabras a minúsculas para evitar problemas con mayúsculas
    if word_one.lower() == word_two.lower():
        return False # Si son exactamente iguales, no son anagramas
    # Comprobar si ambas palabras tienen las mismas letras en la misma cantidad
    return sorted(word_one.lower()) == sorted(word_two.lower()) 

print(is_anagram("Amor", "Roma")) #True

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    
    prev = 0
    next = 1
    
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        
fibonacci()    

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo():
    for number in range(1, 101):
        if number >= 2:
            es_divisible = False
            
            for index in range(2, number):
                if number % index == 0:
                    es_divisible = True
                    break
            
            if not es_divisible:
                print(number)
                
es_primo()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverso(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text
print(reverso("Hola mundo"))
        
# Otro ejemplo

def invertir_cadena(cadena):
    # Crear una nueva cadena invertida manualmente
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

# Ejemplo de uso
texto = "Hola mundo"
resultado = invertir_cadena(texto)
print(resultado)  # Output: "odnum aloH"
