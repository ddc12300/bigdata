

## Análisis de datos de Twitch 2023

El objetivo es analizar un dataset de Twitch, el cual contiene una captura de datos cada 15 minutos.

### Cargar dataset

``` Python
import pandas as pd  
import time

# Inicio del contador de tiempo
inicio = time.time()

# Cargar dataset
df = pd.read_csv("feb-full-2023.csv", sep='\t')

# Fin del contador de tiempo
fin = time.time()
print(fin - inicio)
```

### Explorar el dataset

```Python
# Extraer algunas filas del dataset
df = pd.read_csv("feb-full-2023.csv", sep='\t', nrows=2)

# Imprimir los nombres de las columnas de interes
for col in df.columns:
    print(col)
```

### Selección de columnas y preguntas clave

Queremos conocer los datos más relevantes, como stream más visto, streamers con más seguidores, etc.

```Python
df = pd.read_csv("feb-full-2023.csv", sep='\t', nrows=2, usecols=["captured_at", "viewer_count", "game_name", "stream_title"])
```

### Análisis de stream más visto

```Python
# Encontrar el stream con más espectadores
stream_mas_visto = max(df["viewer_count"])

# Localizar el streamer 
posicion = df["viewer_count"].idxmax()
result = df.iloc[posicion]
```

### Guardar datos de un streamer específico

Queremos obtener las estadísticas de la "Kings League" y guardarlas en un archivo CSV.

```Python
# Filtrar datos de Kings League
datos_kings_league = df[df["streamer_name"] == "kingsleague"]

# Guardar en un archivo CSV
datos_kings_league.to_csv("kingsleague.csv", index=False)
```

### Uso de chunks para procesar el dataset

En lugar de cargar todo el dataset en la memoria, podemos leerlo por partes usando chunks.

```Python
# Leer el dataset en chunks
df = pd.read_csv("feb-full-2023.csv", sep='\t', usecols=["captured_at", "viewer_count", "game_name", "stream_title"], chunksize=1000)

# Guardar datos de Kings League en una lista
lista_kings_league = []
for chunk in df:
    datos_kings_league = chunk[chunk["streamer_name"] == "kingsleague"]
    lista_kings_league.append(datos_kings_league)

# Unir los datos y guardar en un archivo CSV
final_frame = pd.concat(lista_kings_league)
final_frame.to_csv("kingsleague.csv", index=False)
```