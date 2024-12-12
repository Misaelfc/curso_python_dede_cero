### Python Package Manager ###
# Herramienta que facilita la instalación, actualización, desinstalación y gestión de bibliotecas o dependencias necesarias para desarrollar proyectos en Python.

# PIP https://pypi.org

# Para instalar los paquetes crear primero una carpeta de entorno virtual
# 1. sudo -H pip3 install virtualenv
# 2. password: (Pones la contraseña)
# 3. python3 -m virtualenv my_virtualenv es el nombre de la carpeta del entorno virtual, pero tu le puedes poner el que tu quieras.
# 4. cd my_virtualenv Esto es para entrar a la carpeta del entorno virtual
# 5. source bin/activate
# 6. python3 --version Checa que version de python tienes
# 7. pip3 install numpy pandas Instalas los paquetes que quieras poner en python


# pip install pip
# pip --version

# pip install numpy
import pandas # pip3 install pandas
from mypackage import arithmetics
import requests # pip3 install requests
import numpy # pip3 install numpy
print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array * 2)

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

print(arithmetics.sum_two_values(1, 4))
