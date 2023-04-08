
# Ejercicio 1: Introducción a Pandas

notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

**Tarea 1:** Unificar los nombres y apellidos de los alumnos en una única cadena de texto

```python

notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms_complets = []  
for a, c in zip (alumnes,cognoms):  
    nom_complet = f"{a} {c}"  
    noms_complets.append(nom_complet)  
  
print(noms_complets)

```

**Tarea 2:** Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida

```python

notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms_complets = []  
  
tupla = []  
  
for a, c, n in zip (alumnes,cognoms, notes):  
    nom_complet = f"{a} {c}"  
    tupla = (nom_complet, n)  
    noms_complets.append(tupla)  
  
print(noms_complets)

```

**Tarea 3:** Sumar un punto a todas la notas, sin que puedan sobrepasar el 10

```python


notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms_complets = []  
  
tupla = []  
  
for a, c, n in zip (alumnes,cognoms, notes):  
    nom_complet = f"{a} {c}"  
    tupla = (nom_complet, n)  
    noms_complets.append(tupla)  
  
for persona in noms_complets:  
    nota = persona[1]  
    if nota < 10:  
        nota = persona[1]+1  
    nova_persona = (persona[0], nota, )  
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
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms_complets = []  
  
tupla = []  
  
for a, c, n in zip (alumnes,cognoms, notes):  
    nom_complet = f"{a} {c}"  
    tupla = (nom_complet, n)  
    noms_complets.append(tupla)  
  
for persona in noms_complets:  
    nota = persona[1]  
    if nota < 10:  
        nota = persona[1] + 1  
  
    if nota == 10:  
        texto = "Matricula honor"  
    elif nota >= 9 and nota < 10:  
        texto = "Excelente"  
    elif nota >= 7 and nota < 9:  
        texto = "Notable"  
    elif nota > 6 and nota < 7:  
        texto = "Bien"  
    elif nota >= 5 and nota<=6:  
        texto = "Aprobado"  
    elif nota < 5:  
        texto = "Suspendido"  
  
  
    nova_persona = (persona[0], nota, texto)  
    print(nova_persona)

```


**Tarea 5:** Transforma la lista de tuplas en un dataset.  
**Tarea 6:** Calcula la desviación total y porcentual de cada alumno sobre la mediana del aula.  
**Tarea 7:** Exporta el Dataset resultante en formato CSV.

```Python

import pandas as pd  
  
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
noms_complets = []  
  
tupla = []  
llista_definitiva = []  
  
for a, c, n in zip (alumnes,cognoms, notes):  
    nom_complet = f"{a} {c}"  
    tupla = (nom_complet, n)  
    noms_complets.append(tupla)  
  
for persona in noms_complets:  
    nota = persona[1]  
    if nota < 10:  
        nota = persona[1] + 1  
  
    if nota == 10:  
        texto = "Matricula honor"  
    elif nota >= 9 and nota < 10:  
        texto = "Excelente"  
    elif nota >= 7 and nota < 9:  
        texto = "Notable"  
    elif nota > 6 and nota < 7:  
        texto = "Bien"  
    elif nota >= 5 and nota<=6:  
        texto = "Aprobado"  
    elif nota < 5:  
        texto = "Suspendido"  
  
  
    nova_persona = (persona[0], nota, texto)  
    llista_definitiva.append(nova_persona);  
  
df = pd.DataFrame(llista_definitiva, columns=["nom","nota","qualificacio"])  
df.to_csv("Dataset.csv", index=False)  
print(df)

```

---

```

import pandas as pd  
  
file = "./medidas.json"  
  
df = pd.read_json(file)  
  
# ¿Cuantas muestras ha capturado el sensor?  
print(df.shape[0])  
  
  
# Transformar los datos a un formato .csv para poder manipularlos con Excel/8ableau y hacer las gráficas evolutivas  
  
df.to_csv("Dataset.csv")  
  
# Saber cuál ha sido la temperatura máxima, en qué fecha ocurrió  
  
  
  
# Saber cuál ha sido la temperatura mínima, en qué fecha ocurrió  
# ¿Hay errores en los datos?
```


1.  ¿Cuantas muestras ha capturado el sensor?

```python

import json  
  
f = open('medidas.json')  
data = json.load(f)  
  
print(len(data))

```

1.  Transformar los datos a un formato .csv para poder manipularlos con Excel/8ableau y hacer las gráficas evolutivas.
2.  Saber cuál ha sido la temperatura máxima, en qué fecha ocurrió
3.  Saber cuál ha sido la temperatura mínima, en qué fecha ocurrió
4.  ¿Hay errores en los datos?

```python

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
  
f = open('medidas.json')  
data = json.load(f)  
llista_dades = []  
  
  
for d in data:  
    temp = d["temperatura"]  
    pres = d["presion"]  
    date = d["fecha"]  
    tuple = (temp,pres,date)  
    llista_dades.append(tuple)  
  
  
df = pd.DataFrame(llista_dades, columns=["temp", "press", "data"])  
  
print(df)  
max = df["temp"].idxmax()  
print(df.iloc[max])

```

