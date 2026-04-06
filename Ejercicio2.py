# Ejercicio 2: Clase Rectángulo + Diccionario y Condicional
# Objetivo: Crear un diccionario de rectángulos y calcular el área de los que tienen una base mayor a 5.

import os
os.system("cls")

input_base = float(input("Ingrese la base del rectángulo: "))
input_altura = float(input("Ingrese la altura del rectángulo: "))

class Rectangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    def area (self):
        return self.base * self.altura

rectangulo = Rectangulo(input_base, input_altura)
print(f"El área del rectángulo es: {rectangulo.area()}")