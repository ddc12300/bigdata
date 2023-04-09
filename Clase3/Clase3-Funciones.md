
Tuplas en Python:

```python

llista1 = [6, 9]
llista2 = ["josep", "dani"]

llista_final = []

# Inicia un bucle for que recorre las listas 'llista1' y 'llista2' simultáneamente usando la función zip()
for nota, nom in zip(llista1, llista2):
    # Crea una tupla 'conjunt' con los elementos actuales de 'llista1' y 'llista2'
    conjunt = (nota, nom)
    # Añade la tupla 'conjunt' a la lista 'llista_final'
    llista_final.append(conjunt)

# Inicia un bucle for que recorre la lista 'llista_final'
for t in llista_final:
    # Obtiene los elementos de la tupla 't' usando su posición (índice)
    nota = t[0]
    nom = t[1]
    # Imprime el nombre 'nom' y la nota 'nota' en cada iteración
    print(nom, nota)
```

