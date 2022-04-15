#RODRIGO IGNACIO CASTILLO VILLEGAS
import sys

with open(f"{sys.argv[1]}", "r") as file:
    texto=file.read()
lista_palabras = texto.split(" ")
lista_caracteres = list(texto)
set_caracteres = set(lista_caracteres)
set_palabras = set(lista_palabras)

#Otra opcion es usar la funcion zip() para convertir las listas en diccionarios utilizando un duplicado de la lista como segundo parametro
print("El número de caracteres distintos es: ",len(set_caracteres))
print("El número de palabras distintas es: ",len(set_palabras))