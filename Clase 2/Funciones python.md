
index

```python

llista = ["adria", "carla", "joan", "pere"]  
  
nom = "joan"  
  
if nom in llista:  
    print("si")  
    position = llista.index(nom)  
    print(position)  
else:  
    print("no")

```



set() y len()

```python
llista = ["adria", "carla", "joan", "pere", "pere", "joan"]  
  
valors_unics = set(llista)  
print(len(valors_unics))

```

count()


---

Ejercicio

## Ejercicio A (Easy mode)

La UAB acaba de celebrar sus jornadas de puertas abiertas y los futuros estudiantes han acudido a las sesiones informativas. Cada vez que una persona entra en una sesión se anota su nombre. Alguien ha juntado todos los nombres en una sola lista... ¿Puedes sacar información útil de este listado?

1.  ¿Cuantas personas han asistido a las jornadas de puertas abiertas?
2.  ¿Cuantas personas han asistido a más de dos sesiones?
3.  ¿Qué porcentaje de los asistentes accede a más de dos sesiones?

llista = [
    "david",
    "dani",
    "marta",
    "jaume",
    "adria",
    "carla",
    "joan",
    "pere",
    "carla",
    "pere",
    "adria",
    "quico",
    "pere",
    "joan",
    "agustí",
    "adria",
    "joan",
    "adria",
    "siscu",
    "carles",
    "dani",
    "carla"
    ]


```python
llista = [  
    "david",  
    "dani",  
    "marta",  
    "jaume",  
    "adria",  
    "carla",  
    "joan",  
    "pere",  
    "carla",  
    "pere",  
    "adria",  
    "quico",  
    "pere",  
    "joan",  
    "agustí",  
    "adria",  
    "joan",  
    "adria",  
    "siscu",  
    "carles",  
    "dani",  
    "carla"  
    ]  
  
count = 0  
lista_unica=set(llista)  
  
print(f"Personas que han asistido {len(lista_unica)}")  
  
for nom in lista_unica:  
    num_ses=llista.count(nom)  
    print(f"{nom} ha asistido {num_ses} veces")  
    if num_ses > 1:  
        count +=1  
  
print(count)  
  
print(f"{count*100//len(lista_unica)}%")
```


```python
llista = [  
    "david",  
    "dani",  
    "marta",  
    "jaume",  
    "adria",  
    "carla",  
    "joan",  
    "pere",  
    "carla",  
    "pere",  
    "adria",  
    "quico",  
    "pere",  
    "joan",  
    "agustí",  
    "adria",  
    "joan",  
    "adria",  
    "siscu",  
    "carles",  
    "dani",  
    "carla"  
    ]  
  
count = 0  
lista_unica=set(llista)  
  
print(f"Personas que han asistido {len(lista_unica)}")  
  
for nom in lista_unica:  
    num_ses=llista.count(nom)  
    print(f"{nom} ha asistido {num_ses} veces")  
    if num_ses > 1:  
        count +=1  
  
print(count)  
  
print(f"{100*(count/len(lista_unica))}%")
```

## Ejercicio B (dificultad media*)

Tienes dos listas, una para notas y otra para el nombre de los alumnos:

notes = ["5","3","7","8","9.5","4","6,2"]
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]

1.  Crea un código que imprima, para cada alumno, la nota correspondiente, con el texto "El alumno/a _var_alumnos_ ha obtenido un _var nota_".
2.  Calcula e imprime la nota promedio del aula con un decimal
3.  Calcula e imprime la nota más alta junto al nombre del alumno.
4.  calcula e imprime la nota más baja junto al nombre del alumno.

*Este ejercicio exige buscar soluciones en StackOverflow o cualquier otra fuente.

