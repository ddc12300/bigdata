
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

# Declaramos variable cadena
cadena = "esto es un ejercicio"

# Imprime la cadena de texto 'esto es un ejercicio'
print(cadena)

# Declaramos otras variables
nota_examen = 10
asignatura = "vr"

# Imprimimos por pantalla texto y las variables declaradas utilizando un f-string 
print(f"En la asignatura {asignatura} he obtenido un {nota_examen}")

# Modificamos el valor de la variable 'nota_examen'
nota_examen=5

# Declaramos la variable 'frase' con texto y variables utilizando de nuevo un f-string
frase=(f"En la asignatura {asignatura} he obtenido un {nota_examen}")
# Imprime el valor de la variable 'frase'
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
# Declaramos 2 listas
notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  

# Inicia un bucle for que recorre la lista de notas
for n in notas:
	# Inicia un bucle for que recorre la lista de alumnos
    for a in alumnos:  
	    # Imprimimos por pantalla el nombre del alumno 'x' con la nota 'y' incrementada en 1
        print(f"{a} ha obtenido un {int(n)+1}")
     # Rompe el bucle for después de la primera iteración  
    break
```

Solución profe:

Emparejar listas en python con la función zip

```python
# Declaramos 2 listas
notas = ["5", "7", "6", "4", "8", "2"]
alumnos = ["jaume", "carla", "pere", "adrià", "rafael", "agnès"]

# Inicia un bucle for que recorre las listas de notas y alumnos simultáneamente usando la función zip()
for nota, nom in zip(notas, alumnos):
    # Imprime la nota incrementada en 1 y el nombre del alumno en cada iteración
    print(int(nota) + 1, nom)
```



