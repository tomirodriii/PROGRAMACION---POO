# Ejercicio 5: Clase Coche + Diccionario y Tupla
# Objetivo: Crear un diccionario de coches y almacenar sus descripciones en una tupla.

import os
os.system("cls")

marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el modelo del coche: ")
año_fabr = int(input("Ingrese el año de fabricación del coche: "))
class Coche:
    def __init__ (self, marca, modelo, año_fabr):
        self.marca = marca
        self.modelo = modelo
        self.año_fabr = año_fabr
    def descripcion (self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año de fabricación: {self.año_fabr}"

coche = Coche(marca, modelo, año_fabr)
print("Descripcion del Vehiculo: " + coche.descripcion())