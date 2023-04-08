Apuntes de Python:

```Python
# Creamos una lista con dos nombres
lista = ["juan", "david"]

# Iteramos sobre la lista y mostramos un mensaje por cada nombre
for nom in lista:
    print(f"En {nom} no ha vingut")

```

```python
# Creamos una lista con números
num1 = [1, 5, 6, 7, 8, 10]

# Definimos un número adicional
num2 = 2

# Iteramos sobre la lista de números y sumamos num2 a cada número
for num in num1:
    final = num + num2
    # Imprimimos el resultado de cada suma
    print(f"Nota final= {num} + {num2} =", final)

```