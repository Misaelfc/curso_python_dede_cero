### Classes ###

# Definición: Es una estructura que permite crear objetos que agrupan datos (atributos) y comportamientos (métodos). Es el pilar de la programación orientada a objetos (POO). Una clase actúa como una plantilla para crear instancias (objetos) con características y comportamientos definidos.

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas

class Person:
    def __init__(self, name, surname, alias="Sin alias"): #	__init__: Método especial para inicializar los atributos del objeto.
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada 
        
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} está caminando")
        
my_person = Person("Misael", "Flores")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Misael", "Flores", "AbrahamDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 777
print(my_other_person.full_name)