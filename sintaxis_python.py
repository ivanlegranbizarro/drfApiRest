# Sintaxis básica de Python

# Variables

nombre = 'Iván'

# Constantes

PI = 3.14


edad = 17

# Control de flujo

if edad >= 18:
    print('Puedes entrar')
else:
    print('No puedes entrar')

# Funciones


def discoteca(edad):
    if edad >= 18:
        print('Puedes entrar')
    else:
        print('No puedes entrar')

# Ciclos


for i in range(10):
    print(i)

# Listas

lista = [1, 2, 3, 4, 5]

# Diccionarios

diccionario = {'nombre': 'Iván', 'edad': 37}

# Tuplas

tupla = (1, 2, 3, 4, 5)


# Clases


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def discoteca(self):
        if self.edad >= 18:
            print('Puedes ir a una discoteca')
        else:
            print('No puedes ir a una discoteca')


ivan = Persona('Iván', 37)

ivan.discoteca()


# Herencia de clases en Python

class Estudiante(Persona):
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)
        self.universidad = universidad

    def estudiar(self):
        print('Estoy estudiando')

    def discoteca(self):
        print('No puedo ir a una discoteca porque tengo exámenes')

# Tipar variables en Python


nombre: str = 'Iván'
edad: int = 37
estatura: float = 1.75
