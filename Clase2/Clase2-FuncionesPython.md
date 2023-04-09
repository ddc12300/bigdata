
Función append:


```python
llista = ["jaume", "carme"]

# Añade el valor de la variable 'nou_nom' al final de la lista 'llista'
nou_nom = "rafa"
llista.append(nou_nom)

# Imprime la lista 'llista' después de agregar el nuevo nombre
print(llista)
```


Imprimir elemento de una lista:

```python
llista = ["jaume", "carme"]

# Imprime el primer elemento de la lista 'llista' (en la posición 0)
print(llista[0])
```


If - else en python:

```python
llista = ["jaume", "carme"]

# Inicia un bucle for que recorre la lista de nombres
for nom in llista:
    # Verifica si el nombre actual es igual a "carme"
    if nom == "carme":
        # Imprime un mensaje indicando que 'carme' no es 'jaume'
        print(f"{nom} no es el jaume")
    else:
        # Imprime un mensaje indicando que 'jaume' no es 'carme'
        print(nom + " no es la carme")
```



Función index:

```python
llista = ["adria", "carla", "joan", "pere"]

nom = "joan"

# Verifica si el valor de la variable 'nom' se encuentra en la lista 'llista'
if nom in llista:
    # Imprime 'si' si el nombre está en la lista
    print("si")
    # Obtiene el índice de la posición del nombre en la lista y lo guarda en la variable 'position'
    position = llista.index(nom)
    # Imprime el valor de la variable 'position'
    print(position)
else:
    # Imprime 'no' si el nombre no está en la lista
    print("no")
    
```


Funciones set() y len():

```python
llista = ["adria", "carla", "joan", "pere", "pere", "joan"]

# Convierte la lista 'llista' en un conjunto (set) que elimina los valores duplicados
valors_unics = set(llista)
# Imprime la longitud (cantidad de elementos) del conjunto 'valors_unics'
print(len(valors_unics))
```

Función count():

```python
lista = [
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
    "agusti",
    "adria",
    "joan",
]

# Convierte la lista 'lista' en un conjunto (set) que elimina los valores duplicados
unics = set(lista)

# Inicia un bucle for que recorre el conjunto 'unics'
for nom in unics:
    # Cuenta cuántas veces aparece el nombre actual en la lista 'lista'
    contador = lista.count(nom)
    # Imprime un f-string que muestra el nombre actual y la cantidad de veces que aparece en 'lista'
    print(f"{nom} apareix {contador} vegades")
```


Función zip:

```python
# Declaramos 2 listas
notas = ["5", "7", "6", "4", "8", "2"]
alumnos = ["jaume", "carla", "pere", "adrià", "rafael", "agnès"]

# Inicia un bucle for que recorre las listas de notas y alumnos simultáneamente usando la función zip()
for nota, nom in zip(notas, alumnos):
    # Imprime la nota incrementada en 1 y el nombre del alumno en cada iteración
    print(int(nota) + 1, nom)
```
