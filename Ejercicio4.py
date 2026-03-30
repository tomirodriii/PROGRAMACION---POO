# Ejercicio 4: Clase Libro + Lista y Condicional
# Objetivo: Crear una lista de libros y mostrar solo los publicados después del año 2000.

import os
os.system("cls")

class Libro:
    def __init__ (self):
        self.nombre = input("Nombre del libro: ")
        self.autor = input("Su autor es: ")
        self.añopub = int(input("Su año de publicacion es: "))
        
libro1 = Libro()
libro2 = Libro()
libro3 = Libro()
libro4 = Libro()

libros = [libro1, libro2, libro3, libro4]

for i in libros: 
    if i.año>2000:
        print(f"Nombre del Libro: {libros.nombre} | Autor del libro: {libros.autor} | Año de Publicacion: {libros.añopub}")
    else:
        print("No se ha encontrado libros con publicacion despues del 2000")