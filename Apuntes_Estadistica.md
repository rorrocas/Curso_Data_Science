# Unidad Fundamentos Data Science
## Libreria Pandas (Panel Data)
- Hace uso de archivos **csv** (comma separated value).
- **read_csv("archivo")** # Es una funcion que se utiliza para abrir un **csv** como **DataFrame**.
- **.head()** # Muestra las primeras filas de un dataframe.
- **.shape()** # Retorna la cantidad de filas y columnas de un DataFrame.
- **.columns()** # Retorna un index de las columnas en un DataFrame (Como un diccionario).
- **.iloc[]** # Accede a un valor de un indice o fila (Entrega la fila completa y se puede manipular como diccionario).
- **.values** # Muestra los valores de una columna llamada.
- **value_counts()** # Muestra cantidades de valores por variable.

_Se puede trabajar con un conjunto definido dentro del DF haciendo uso de ["columna"] podemos especificar la columna deseada o el numero de filas [2], [:10] o [2:10].
Cuando es solicitada una columna se crea un serie, un lista unidimensional con valores de esa columna._ 

## Operacionalización
1. Dominio especifico: **Definir** el concepto a evaluar o analizar.
2. Operacionalizacion estadistica: Como vamos a **clasificar** tal concepto bajo que parametros se puede subclasificar.
3. Operacionalizacion computacional: Como vamos a guardar o **representar** estos datos con que tipo de variables o margenes.

## Estadistica Univariada
_Promedio:_
- Con numpy: np.mean(lista)
- Con Python nativo: sum(lista)/len(lista)
- Con pandas: df["columna"].mean()

_Moda: Valor que mas se repite en una muestra._
- Con Scipy: import scipy.stats as stats -> stats.mode(lista)

_Mediana:_
- Con numpy: np.median(lista)
- Con pandas: df["columna"].median()

_Percentiles:_
- Con numpy: np.percentile(lista,porcentaje)

_Rango:_
- Con numpy: np.ptp(lista)
- Con Python N: altura.max() - altura.min()

_Varianza:_
- Con numpy: np.var(lista)
- Con pandas: df["columna"].var()

_Desviacion Estandar:_
- Con numpy: np.std(lista)
- Con pandas: df["columna"].std()

## Momentos Estadisticos
_Cuatro medidas para el analisis descriptivo de los datos_
- Medidas de tendencia central: Busca resumir cual numero describe o representa mejor la variable.
- Medidas de dispercion: Que tan disperso estan los datos respecto a la media.
- Medidas de sesgo: Que tan desviada esta la distribucion de una variable respecto a su punto de origen. 
- Medidas de curtosis: La altura de un distribucion respcto al centro.

## Control de flujo con pandas
- for i in df["columna"] # Retorna el valor de la columna mas no el indice.
- for i in df["columna"].index() # Retorna el indice mas no el valor de la columna.
- for i,j in df["columna"].iteritems() # Retorna nombre de columna y **todos** los valores de esa columna como una **serie** .
- for i in df["columna"].iterrows # Recorre dataframe por filas y retorna indice con valores de fila en cada iteracion.

## Subsetting
- df[bool][indice]
_Ejemplo:_
```
df[df["sexo"] == "M"]["nombres"]
R:
2 Jose
4 Abraham
5 Julio
```

