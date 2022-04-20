#Rodrigo
lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]

def factorial(valor):
    total=1
    if valor == 0:
        return 1
    for i in range(1,valor+1):
        total *= i
    return total        
def productoria(lista):
    total=1
    for i in lista:
        total*=i
    return total
def calcular(lista_factorial,lista_productos):
    for i in lista_factorial:
        print(f"\nEl factorial de {i} es: {factorial(i)}")
    for i in lista_productos:
        print(f"\nLa productoria de {i} es {productoria(i)}")

def validacion(lista_str):
    global lista_numeros
    lista_validada = []
    for i in lista_str:
        if i in lista_numeros:
            lista_validada.append(i)
    if len(lista_validada)>0:
        print("\nLa lista es valida.")
        return True
    else:
        print("\nIngrese valores validos.")
        return False
def menu():
    global lista_numeros
    condicion = True
    lista_productos = []
    lista_factorial = []
    while condicion:
        opcion = input("\nEliga una opcion:\n1)Ingresar productoria.\n2)Ingresar factorial.\n3)Realizar calculo.\n4)Salir del programa.\n")
        if opcion == "1":
            valido = True
            while valido:
                lista = input("Ingrese Lista: ")
                if validacion(lista):
                    valido = False
            lista_productos.append([int(i) for i in lista.split(",") if type(int(i)) == int])
            print(lista_productos)
        elif opcion == "2":
            valido = True
            while valido:
                numero_factorial = input("Ingrese numero: ")
                if validacion(numero_factorial):
                    valido = False
            lista_factorial.append(int(numero_factorial))
            print(lista_factorial)
                
        elif opcion == "3":
            if len(lista_productos)>0 or len(lista_factorial)>0:
                calcular(lista_factorial,lista_productos)
                lista_factorial = []
                lista_productos = []
            else:
                print("\nPrimero ingrese valores para calcular.")
        elif opcion == "4":
            condicion = False
        else:
            print("\3\3\3\nIngrese opcion valida.\n1)Ingresar productoria.\n2)Ingresar factorial.\n3)Realizar calculo.\n4)Salir del programa.")
    print("\nAdios.")        

menu()