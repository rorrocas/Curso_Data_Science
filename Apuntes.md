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
lista[indice] = valor
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
diccionario[Llave] = valor
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
- **is** # Es una **keyword** y funciona como un "==".
## Ciclo for
- **for posicion, elemento in enumerate(string)** # Permite traer poscicion y elemento de un string.
- **for clave, valor in diccionario.items()** # Realiza recorrido for por clave y valor del diccionario.
- **zip()** # Permite unir listas para iterarlas a la vez.
```
for elemento_1, elemento_2, elemente_3 in zip(lista_1, lista_2, lista_3)
```
- **random.shuffle(lista)** # Retorna una lista mezclada derivada de una lista original.
## List comprehesions
_Para armar una lista basada en valores dados por una condicional y un else _
```
[expresión1 if condición1 else expresión2 for variable in iterable]
```
_Para armar una lista basada solo en una condicion sin else_
```
[expresión for variable in iterable if condición ]
```
## Dictionary Comprehensions
_Utilizando dos listas podemos armar un diccionario de la sgte. forma:_
```
{key:value for key,value in zip(claves, valores)}
```
# Unidad III
_DRY: Don't Repeat Your Self_
- **global** # Se utiliza para llamar variables globales a entornos locales
## Tipos de parametros
_Obligatorio_
```
def funcion(parametro_obligatorio)
```
_Opcional o Por Defecto__
```
def funcion(parametro_obligatorio,parametro_opcional = valor_por_defecto)
```
_***args** y ****kwarsg**__
- ***arg** permite pasar multiples argumentos transformandoloes en una lista.
- ****kwarsg** permite pasar multiples argumentos pasandolos a diccionario y por eso estos deben ser asignados.
```
def funcion(**kwarsg):
  return kwarsg
funcion(key_1 = value_1, key_2 = value_2) # Imprime {"key_1": value_1, "key_2": value_2}
```
## Documentacion
_Importante documentar codigo en cada funcion_
```
def funcion(parametro):
""" La funcion toma el parametro y retorna esta operacion... """
```
_Sintaxis para comentar codigo_
### Google
```
"""
[summary]
Args:
var1 ([type]): [description]
var2 ([type]): [description]
Returns:
[type]: [description]
"""
```
### Sphinx
```
"""
[summary]
:param var1: [description]
:type var1: [type]
:param var2: [description]
:type var2: [type]
:return: [description]
:rtype: [ty
"""
```
### Docblockr
```
"""
[summary]
Arguments:
var1 {[type]} -- [description]
var2 {[type]} -- [description]
Returns:
[type] -- [description]
"""
```
### Numpy
```
"""
[summary]
Parameters
----------
var1 : [type]
[description]
var2 : [type]
[description]
Returns
-------
[type]
[description return]
"""
```
# Unidad IV Conexion y Consumo de APIs
_**requests** es la libreria utilizada para realizar consultas en APIs.
- **requests.request** # Es utilizada para realizar consultas.
```
response = requests.request("GET", url, headers=headers, data=payload)
```
_Para visualizar la consulta se utiliza **response.text** que retorna un string en formato JSON_
## Codigos
- 1xx: Información.
- 2xx: Solicitudes exitosas.
- 3xx: Redireccionamiento.
- 4xx: Error del cliente (no hizo la request correctamente).
- 5xx: Error del servidor (no puede dar una respuesta).
_Algunos ejemplos:_
```
● 200: Ok.
● 401: Unauthorized.
● 403: Forbidden.
● 404: Not Found.
● 500: Server error.
```
# Lectura del contenido
_La libreria **json** se utiliza para transformar de JSON a listas, diccionarios o viceversa_
- Con **json.loads(response.text)** obtenemos una lista o diccionario a partir de un JSON
_Ejemplo de transformar requests en una funcion:_
```
import requests
import json
def request_get(url):
  return json.loads(requests.get(url).text)
```
