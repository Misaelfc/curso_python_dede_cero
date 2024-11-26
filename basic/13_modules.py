### Modules ###

# Un módulo es un archivo que contiene código Python (funciones, clases o variables) que puedes reutilizar en otros programas. Esto permite organizar el código en partes más manejables y reutilizables.

from math import pi as PI_VALUE # Importar pi como un alias de PI_VALUE
import math
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")

sumValue(5, 3, 1)
printValue("Hola python")

print(math.pi)
print(math.pow(2, 8)) # Pow es la potencia


print(PI_VALUE)