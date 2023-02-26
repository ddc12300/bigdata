Clase 2

```python

llista = ["jaume", "carme"]  
  
nou_nom = "rafa"  
  
llista.append(nou_nom)  
  
print(llista)

```


```python
llista = ["jaume", "carme"]  
  
print(llista[0])

```


```python
llista = ["jaume", "carme"]  
  
for nom in llista:  
    if nom == "carme":  
        print(f"{nom} no es el jaume")  
    else:  
        print(nom + " no es la carme")

```


----

# Ejercicios Básicos

A continuación tienes una lista de tareas a realizar, puedes realizar cada una de ellas en una nueva línea de código.

## Cosas básicas con _print()_

1.  Crea una variable, que contenga la cadena "esto es un ejercicio".
2.  Imprime esa variable.
3.  Crea una nueva variable que contenga la nota que has obtenido en el último examen que has realizado.
4.  Crea una variable que contenga el nombre de la asignatura de dicho examen.
5.  Imprime las dos últimas variables de forma que se pueda en el terminal: "En la asignatura _variable_n_ he obtenido un _variable_n_".


## Ejercicios de documentación

### Ejercicio A

1.  Mete el texto del último _print()_ del ejercicio anterior en una variable.
2.  Debes substituir la nota obtenida por otra (cualquiera) y volver a imprimir.

```python
cadena = "esto es un ejercicio"  
  
print(cadena)  
  
nota_examen = 10  
asignatura = "vr"  
  
print(f"En la asignatura {asignatura} he obtenido un {nota_examen}")  
  
  
nota_examen=5  
frase=(f"En la asignatura {asignatura} he obtenido un {nota_examen}")  
print(frase)
```



### Ejercicio B

Un compañero te ha mandado dos listados: las notas y los nombres de los alumnos a quienes corresponden dichas notas:

notas = ["5","7","6","4","8","2"]
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]

1.  Debes sumar 1 punto a cada una de las notas.
2.  Imprime el resultado junto al nombre del correspondiente alumno de tal manera que:  
    "_var_alumno_ ha obtenido un _var_nota_".


Mi solución:
```python

notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  
  
for n in notas:  
    for a in alumnos:  
        print(f"{a} ha obtenido un {int(n)+1}")  
    break
```

Solución profe:

Emparejar listas en python

Función zip

```python

notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  
  
for nota, nom in zip(notas, alumnos):  
    print(int(nota)+1, nom)

```



----

revisar antes de subir a github


```python
notes = ["5", "3", "7", "8", "9.5", "4", "6.2"]  
alumnes = ["adria", "agnès", "josep", "rafa", "cristina", "Gemma", "Eduard"]  
  
# Imprime la nota de cada alumno  
for nota in range(len(alumnes)):  
    print("El alumno/a", alumnes[i], "ha obtenido un", notes[i])  
  
# Convierte las notas en una lista de números  
notes = [float(n) for n in notes]  
  
# Calcula e imprime la nota promedio del aula  
average_note = sum(notes) / len(notes)  
print("La nota promedio del aula es:", round(average_note, 1))  
  
# Calcula e imprime la nota más alta junto al nombre del alumno  
max_note = max(notes)  
max_note_index = notes.index(max_note)  
print("La nota más alta es un", max_note, "obtenida por el alumno/a", alumnes[max_note_index])  
  
# Calcula e imprime la nota más baja junto al nombre del alumno  
min_note = min(notes)  
min_note_index = notes.index(min_note)  
print("La nota más baja es un", min_note, "obtenida por el alumno/a", alumnes[min_note_index])

```


funcion index

limpieza de datos

funcion zip

