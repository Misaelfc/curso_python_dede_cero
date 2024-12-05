### Lambdas ###
# Es una función anónima, es decir, una función que no tiene un nombre explícito y se define en una sola línea. Las lambdas son útiles cuando necesitas una función pequeña y temporal, típicamente como argumento para otra función.

def sum_two_values(
    first_value, second_value): return first_value + second_value

print(sum_two_values(2, 4))

def multiply_values(
    first_value, second_value): return first_value * second_value - 3

print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))

#Ejemplo con funciones superior

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usar lambda con map para duplicar cada número
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Salida: [2, 4, 6, 8, 10]   