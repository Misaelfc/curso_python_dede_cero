### Conditionals ###
#l
# Los condicionales son estructuras que permiten tomar decisiones dentro de un programa según ciertas condiciones. Esto se hace evaluando una expresión booleana (una que resulta en True o False) y ejecutando un bloque de código si esa condición se cumple.

# if Se usa para ejecutar un bloque de código si la condición es verdadera.

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")
    
# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 o menor que 20")
elif my_condition == 25:
    print("Es igual a 25")  
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continua")
    
# Condicional con ispección de valor

my_string = ""

if not my_string: 
    print("Mi cadena de texto es vacía") #La expresión not my_string evalúa si my_string es falsa, lo cual sucede si la cadena está vacía.
    
if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")