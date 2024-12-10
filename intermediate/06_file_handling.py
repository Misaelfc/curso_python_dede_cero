### File Handling ###
# Se refiere al conjunto de operaciones que puedes realizar con archivos, como abrirlos, leerlos, escribir en ellos y cerrarlos. Python facilita estas tareas a través de funciones y métodos específicos.

import os
import json
import csv
import xml

# .txt file
txt_file = open("./intermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Misael\nMi apellido es Flores\n33 años\nY mi lenguaje preferido es Python") 
# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta JavaScript")
print(txt_file.readline())

txt_file.close()

with open("intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")

# .json file

json_file = open("intermediate/my_file.json", "w+")

json_test = {
    "name": "Misael",
    "surname": "Flores",
    "age": 33,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent=2) #indent son los espacios que se crean en el fichero

json_file.close()

with open("intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
        
json_dict = json.load(open("intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

csv_file = open("intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Misael", "Flores", 33, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xlsx file

