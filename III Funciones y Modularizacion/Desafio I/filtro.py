#Rodrigo Castillo
import sys

def filtro(diccionario, umbral, opcion="mayor"):
    if opcion == "mayor":
        filtro = {k:v for k,v in diccionario.items() if v > int(umbral)}
        print("Los productos mayores al umbral son:",", ".join(filtro.keys()))
    elif opcion.lower() in ["menor"]:
        filtro = {k:v for k,v in diccionario.items() if v < int(umbral)}
        print("Los productos menores al umbral son:",", ".join(filtro.keys()))
        
    else:
        print("Lo sentimos, no es una operación válida")
    

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

if len(sys.argv)>2: 
    filtro(precios, sys.argv[1], sys.argv[2])
else:
    filtro(precios,sys.argv[1])