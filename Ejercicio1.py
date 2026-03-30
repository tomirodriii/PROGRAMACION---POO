#  Ejercicio 1: Clase Persona + Lista y Ciclo
#  Objetivo: Crear una lista de personas y mostrar su información usando un ciclo.

import os
os.system("cls")


class Socio:
    def __init__(self, nombre, apellido, legajo, telefono, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.telefono = telefono
        self.sexo = sexo
        pass

Socios = []
nombre = input("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
sexo = input ("Ingrese su sexo (M/F): ")
legajo = int(input("Ingrese su legajo: "))
telefono = int(input("Ingrese su telefono: "))

socios_nuevos = Socio(nombre, apellido, legajo, telefono, sexo)
Socios.append(socios_nuevos)
for Socio in Socios:
    print(f"El nuevo socio agregado es:")
    print(f"Nombre: {nombre}")
    print()
    print(f"Apellido: {apellido}")
    print()
    print(f"Sexo: {sexo}")
    print()
    print(f"N° Legajo: {legajo}")
    print()
    print(f"Telefono: {telefono}")
     
    

            