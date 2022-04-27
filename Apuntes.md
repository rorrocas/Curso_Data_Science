# Unidad I
## Metodos para string
- **string.count("caracter")** # Cuenta la cantidad de "caracter" en string.
- **string.upper()**: # Transforma a Mayusculas.
- **string.lower()**  # Transforma a Minuscula.
- **string.title()** #Transforma a Mayusculas la primera letra al comienzo y despues de un espacio.
- **(", "join(["a","b","c"]))** # Une elemtos de una lista a un string.

## Funciones importantes
- __getpass.getpass()__ # Funciona como un input pero con caracteres ocultos.
- <b>sys.argv[#]</b> # Pasa argumentos al ejecutar el script (El elemento[0] es el nombre del script).
- <b>.__dir__()</b> # En un objeto muestra las funciones de tal objeto.
- **dir(objeto)** # Cumple la misma funcion que __dir__ pero con otra sintaxis.

## Metodos para listas
```
lista[**indice**] = **valor**
```
_Los elementos se buscan por el **indice**._
- **append()** # Inserta elemento en la ultima posicion.
- **insert(i,x)** # Inserta elemento x en posicion i.
- **pop()** # Retorna ultimo elemento.
- **remove(x)** # Remueve elemento "x".
- **reverse()** # Revierte elementos de la lista.
- **sort()** # Ordena elementos de la lista menor a mayor y de forma alfabetica.
- **sorted(lista)** || **sorted(lista, reverse = True)** # Misma funcion que sort pero retorna la lista e invertida con reverse True.	
- **index(x)** # retorna indice del elemento "x".
- **sum(lista)** # Suma elementos dentro de una lista.
- **max(lista)** # Retorna mayor elemento de una lista.
- **min(lsita)** # Retorna menor elemento de una lista.

## Metodos para diccionario
```
diccionario[**Llave**] = **valor**
```
_Los elementos se buscan por la **clave**._

_Las **claves** son unicas y se **reemplazaran** si se usa una ya existente._

- **del** diccionario[**"llave"**] # Elimina elemento de la llave correspondiente.
- diccionario.**pop("llave")** # Elimina y retorna valor a partir de la llave.
- diccionario_a.update(diccionario_b) # Une ambos diccionarios *si existen elementos con llaves en comun el diccionario_b sobreescribe al diccionario_a.*
- **.keys()** # Retorna lista con llaves.
- **.values()** # Retorna lista con valores.
- **.items()** # Entrega lista con pares (**key**,**value**).
- **.get()** # Permite entregar mensaje en caso de no encontrar llave.
```
diccionario.get('llave', 'No se encuentra el elemento solicitado')
'No se encuentra el elemento solicitado'
```
## Tuplas
_Funcionan como listas inmutables, sirven esencialmente para el **unpacking**._
```
tupla = (elemento1, elemento2)
var1, var2 = tupla
```
## Sets
_Funcionan como listas que no permiten elementos repetidos._
```
set = {elemento1, elemento2, elemento3} -> Con elemento1 != elemento2 != elemento3 
```
## Convertir estructuras
_Diccionario a lista (key y value)._
```
list({"k1": 1, "k2": 2}.items()) # [('k1', 1), ('k2', 2)]
```
_Lista a Diccionario__
```
dict([('k1', 1), ('k2', 2)]) # {"k1": 1, "k2": 2}
```

# Unidad II
## Ciclo for
- **for i,j in enumerate(string)** #permite traer poscicion y elemento de un string.
- **for i, j in diccionario.items()** #Realiza recorrido for por clave y valor del diccionario.

# Unidad III	
# Unidad IV Conexion y Consumo de APIs
