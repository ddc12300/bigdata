
# Ejercicio 1: Introducción a Pandas

notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

**Tarea 1:** Unificar los nombres y apellidos de los alumnos en una única cadena de texto

```python
notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]
noms_complets = []

# Inicia un bucle for que recorre las listas 'alumnes' y 'cognoms' simultáneamente usando la función zip()
for a, c in zip(alumnes, cognoms):
    # Crea un f-string 'nom_complet' que combina el nombre y el apellido actuales
    nom_complet = f"{a} {c}"
    # Añade el nombre completo a la lista 'noms_complets'
    noms_complets.append(nom_complet)

# Imprime la lista 'noms_complets' con los nombres completos de los alumnos
print(noms_complets)
```


**Tarea 2:** Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida

```python
notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]
noms_complets = []

# Inicia un bucle for que recorre las listas 'alumnes', 'cognoms' y 'notes' simultáneamente usando la función zip()
for a, c, n in zip(alumnes, cognoms, notes):
    # Crea un f-string 'nom_complet' que combina el nombre y el apellido actuales
    nom_complet = f"{a} {c}"
    # Crea una tupla que contiene el nombre completo y la nota actual
    tupla = (nom_complet, n)
    # Añade la tupla a la lista 'noms_complets'
    noms_complets.append(tupla)

# Imprime la lista 'noms_complets' con los nombres completos de los alumnos y sus notas
print(noms_complets)
```


**Tarea 3:** Sumar un punto a todas la notas, sin que puedan sobrepasar el 10

```python
notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]
noms_complets = []

# Inicia un bucle for que recorre las listas 'alumnes', 'cognoms' y 'notes' simultáneamente usando la función zip()
for a, c, n in zip(alumnes, cognoms, notes):
    # Crea un f-string 'nom_complet' que combina el nombre y el apellido actuales
    nom_complet = f"{a} {c}"
    # Crea una tupla que contiene el nombre completo y la nota actual
    tupla = (nom_complet, n)
    # Añade la tupla a la lista 'noms_complets'
    noms_complets.append(tupla)

# Inicia un bucle for que recorre la lista 'noms_complets'
for persona in noms_complets:
    # Obtiene la nota de la tupla 'persona' usando su posición (índice)
    nota = persona[1]
    # Verifica si la nota es menor que 10
    if nota < 10:
        # Incrementa la nota en 1
        nota = persona[1] + 1
    # Crea una nueva tupla 'nova_persona' con el nombre completo y la nota incrementada
    nova_persona = (persona[0], nota)
    # Imprime la tupla 'nova_persona'
    print(nova_persona)
```



**Tarea 4:** Añadir un tercer elemento a la tupla siguiendo este criterio:  
  
- Si la nota final es inferior a 5, añadir el texto "suspendido".  
- Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".  
- Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".  
- Si la nota es igual o superior a 7, añadir el texto "notable".  
- Si la nota supera el 9, añadir el texto "Excelente".  
- Si la nota equivale a un 10, añadir el texto "matrícula de honor".

```python
notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]
noms_complets = []

# Inicia un bucle for que recorre las listas 'alumnes', 'cognoms' y 'notes' simultáneamente usando la función zip()
for a, c, n in zip(alumnes, cognoms, notes):
    # Crea un f-string 'nom_complet' que combina el nombre y el apellido actuales
    nom_complet = f"{a} {c}"
    # Crea una tupla que contiene el nombre completo y la nota actual
    tupla = (nom_complet, n)
    # Añade la tupla a la lista 'noms_complets'
    noms_complets.append(tupla)

# Inicia un bucle for que recorre la lista 'noms_complets'
for persona in noms_complets:
    # Obtiene la nota de la tupla 'persona' usando su posición (índice)
    nota = persona[1]
    # Verifica si la nota es menor que 10 y la incrementa en 1 si es el caso
    if nota < 10:
        nota = persona[1] + 1

    # Clasifica la nota según su valor y asigna un mensaje a la variable 'texto'
    if nota == 10:
        texto = "Matricula honor"
    elif nota >= 9 and nota < 10:
        texto = "Excelente"
    elif nota >= 7 and nota < 9:
        texto = "Notable"
    elif nota > 6 and nota < 7:
        texto = "Bien"
    elif nota >= 5 and nota <= 6:
        texto = "Aprobado"
    elif nota < 5:
        texto = "Suspendido"

    # Crea una nueva tupla 'nova_persona' con el nombre completo, la nota y el mensaje de 'texto'
    nova_persona = (persona[0], nota, texto)
    #Imprime la tupla 'nova_persona'
    print(nova_persona)
```


**Tarea 5:** Transforma la lista de tuplas en un dataset.  
**Tarea 6:** Calcula la desviación total y porcentual de cada alumno sobre la mediana del aula.  
**Tarea 7:** Exporta el Dataset resultante en formato CSV.

```python
import pandas as pd

notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]
noms_complets = []

tupla = []
llista_definitiva = []

# Inicia un bucle for que recorre las listas 'alumnes', 'cognoms' y 'notes' simultáneamente usando la función zip()
for a, c, n in zip(alumnes, cognoms, notes):
    # Crea un f-string 'nom_complet' que combina el nombre y el apellido actuales
    nom_complet = f"{a} {c}"
    # Crea una tupla que contiene el nombre completo y la nota actual
    tupla = (nom_complet, n)
    # Añade la tupla a la lista 'noms_complets'
    noms_complets.append(tupla)

# Inicia un bucle for que recorre la lista 'noms_complets'
for persona in noms_complets:
    # Obtiene la nota de la tupla 'persona' usando su posición (índice)
    nota = persona[1]
    # Verifica si la nota es menor que 10 y la incrementa en 1 si es el caso
    if nota < 10:
        nota = persona[1] + 1

    # Clasifica la nota según su valor y asigna un mensaje a la variable 'texto'
    if nota == 10:
        texto = "Matricula honor"
    elif nota >= 9 and nota < 10:
        texto = "Excelente"
    elif nota >= 7 and nota < 9:
        texto = "Notable"
    elif nota > 6 and nota < 7:
        texto = "Bien"
    elif nota >= 5 and nota <= 6:
        texto = "Aprobado"
    elif nota < 5:
        texto = "Suspendido"

    # Crea una nueva tupla 'nova_persona' con el nombre completo, la nota y el mensaje de 'texto'
    nova_persona = (persona[0], nota, texto)
    # Añade la tupla 'nova_persona' a la lista 'llista_definitiva'
    llista_definitiva.append(nova_persona)

# Crea un DataFrame 'df' a partir de la lista 'llista_definitiva' y asigna nombres de columna
df = pd.DataFrame(llista_definitiva, columns=["nom", "nota", "qualificacio"])
# Guarda el DataFrame 'df' en un archivo CSV llamado "Dataset.csv" sin incluir los índices
df.to_csv("Dataset.csv", index=False)
# Imprime el contenido del DataFrame 'df'
print(df)
```


---

Añadir Ejercicio 2



---

# Ejercicio 3: Datos desde JSON

En este [archivo .json](https://raw.githubusercontent.com/AdriaPadilla/bigdata-uab/main/ejercicios/medidas.json) tienes los datos de temperatura y presión atmosférica de un sensor, que durante unos meses ha estado capturando algunos datos en un lugar de trabajo.

1.  ¿Cuantas muestras ha capturado el sensor?
2. Transformar los datos a un formato .csv para poder manipularlos con Excel/Tableau y hacer las gráficas evolutivas.
3. Saber cuál ha sido la temperatura máxima, en qué fecha ocurrió
4.  Saber cuál ha sido la temperatura mínima, en qué fecha ocurrió
5.  ¿Hay errores en los datos?

Opción 1 con Pandas:

``` Python
import pandas as pd 

# Carga el archivo JSON en un DataFrame de pandas
file = "./medidas.json"  
df = pd.read_json(file)  
  
# ¿Cuantas muestras ha capturado el sensor?  
# Cuenta la cantidad de muestras capturadas por el sensor
print(df.shape[0])  
  
  
# Transformar los datos a un formato .csv para poder manipularlos con Excel/8ableau y hacer las gráficas evolutivas  
df.to_csv("Dataset.csv")  
  
# Saber cuál ha sido la temperatura máxima, en qué fecha ocurrió  
  
  
  
# Saber cuál ha sido la temperatura mínima, en qué fecha ocurrió  
# ¿Hay errores en los datos?
```


Opción 2 libreria json:

```python
import json

# Abre el archivo 'medidas.json' en modo lectura y lo guarda en la variable 'f'
f = open('medidas.json')
# Carga el contenido del archivo 'medidas.json' en la variable 'data' como un objeto JSON
data = json.load(f)

# Imprime la cantidad de elementos en el objeto JSON 'data'
print(len(data))
```



```python
import json
import pandas as pd

# Abre el archivo 'medidas.json' en modo lectura y carga su contenido en la variable 'data'
f = open('medidas.json')
data = json.load(f)
llista_dades = []

# Imprime la cantidad de elementos en el objeto JSON 'data'
print(len(data))

# Recorre cada elemento en 'data' y extrae sus atributos "temperatura", "presion" y "fecha" en una tupla
for d in data:
    temp = d["temperatura"]
    pres = d["presion"]
    date = d["fecha"]
    tuple = (temp, pres, date)
    # Añade la tupla a la lista 'llista_dades'
    llista_dades.append(tuple)

# Convierte la lista 'llista_dades' en un DataFrame de pandas
df = pd.DataFrame(llista_dades)

# Imprime el DataFrame 'df'
print(df)

# Guarda el DataFrame 'df' en un archivo CSV llamado "temperaturas.csv" sin incluir los índices y usando coma como decimal
df.to_csv("temperaturas.csv", index=False, decimal=",")

```

---

```

import json  
  
import pandas as pd  
  
f = open('medidas.json')  
data = json.load(f)  
llista_dades = []  
  
  
print(len(data))  
  
for d in data:  
    temp = d["temperatura"]  
    pres = d["presion"]  
    date = d["fecha"]  
    tuple = (temp,pres,date)  
    llista_dades.append(tuple)  
  
  
df = pd.DataFrame(llista_dades)  
  
print(df)  
  
df.to_csv("temperaturas.csv", index=False, decimal=",")  
  
sample = df.sample(frac=0.1)  
sample_2 = sample.sample(frac=0.1)  
sample_2.to_csv("sample.csv")

```


----


```python
import json
import pandas as pd

# Abre el archivo 'medidas.json' en modo lectura y carga su contenido en la variable 'data'
f = open('medidas.json')
data = json.load(f)
llista_dades = []

# Recorre cada elemento en 'data' y extrae sus atributos "temperatura", "presion" y "fecha" en una tupla
for d in data:
    temp = d["temperatura"]
    pres = d["presion"]
    date = d["fecha"]
    tuple = (temp, pres, date)
    # Añade la tupla a la lista 'llista_dades'
    llista_dades.append(tuple)

# Convierte la lista 'llista_dades' en un DataFrame de pandas y asigna nombres de columna
df = pd.DataFrame(llista_dades, columns=["temp", "press", "data"])

# Imprime el DataFrame 'df'
print(df)

# Encuentra el índice de la temperatura máxima en la columna 'temp'
max = df["temp"].idxmax()

# Imprime la fila correspondiente al índice de la temperatura máxima
print(df.iloc[max])

```

