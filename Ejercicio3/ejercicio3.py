import pandas as pd

# Funciones para clasificar audiencia y horas ejercicio 4
def clasificar_audiencia(x):
    if x < 10000:
        return "Baja"
    elif x < 50000:
        return "Media"
    else:
        return "Alta"

def clasificar_horas(x):
    if x < 10:
        return "Pocas"
    elif x < 50:
        return "Moderadas"
    else:
        return "Muchas"

# 1. Evolución de espectadores (captura a captura) durante el periodo
# Cargamos el csv en un dataframe escogiendo solo las columnas necesarias
df1 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["captured_at", "viewer_count"])

# Convierto la columna captured_at a tipo de dato datetime
df1["captured_at"] = pd.to_datetime(df1["captured_at"])

# Agrupo los datos en un dataframe por captured_at y viewer count, calculando la suma de viewers
evolucion_espectadores_df = df1.groupby("captured_at")["viewer_count"].sum().reset_index()

# guardo el resultado en un csv
evolucion_espectadores_df.to_csv("evolucion_espectadores.csv", index=False)

# imprimo las primeras filas del dataset
print(evolucion_espectadores_df.head())

# 2. Categorías más vistas y en las que más horas de directo se han realizado
# Cargamos el csv en un dataframe escogiendo solo las columnas necesarias
df2 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["game_name", "viewer_count"])

# Calculo la suma total de espectadores y el número de capturas por categoría
categorias_mas_vistas_df = df2.groupby("game_name")["viewer_count"].agg(['sum', 'count']).reset_index()

# Renombro las columnas
categorias_mas_vistas_df.columns = ["game_name", "total_viewers", "num_captures"]

# Calcular las horas de directo aproximadas dividiendo el número de capturas por 4
categorias_mas_vistas_df["hours_direct"] = categorias_mas_vistas_df["num_captures"] / 4

# Guardo el nuevo dataset en un archivo csv
categorias_mas_vistas_df.to_csv("categorias_mas_vistas.csv", index=False)

# imprimo primeras filas
print(categorias_mas_vistas_df.head())

# 3. Evolución (captura a captura) de las categorías a lo largo del mes
# Cargamos el csv en un dataframe escogiendo solo las columnas necesarias
df3 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["captured_at", "game_name", "viewer_count"])

# cambio tipo de dato captured_at de nuevo
df3["captured_at"] = pd.to_datetime(df3["captured_at"])

# Extraigo las 5 categorías con más espectadores a partir del df del ejercicio 2
top5_categorias_viewers = categorias_mas_vistas_df.nlargest(5, "total_viewers")["game_name"].tolist()

# Filtro el dataframe para incluir solo las 5 categorías con más espectadores
df3 = df3[df3["game_name"].isin(top5_categorias_viewers)]

# Calcula la evolución (captura a captura) de las categorías a lo largo del mes
evolucion_categorias_df = df3.groupby(["captured_at", "game_name"])["viewer_count"].sum().reset_index()

# Creo un nuevo csv
evolucion_categorias_df.to_csv("evolucion_categorias.csv", index=False)

# Imprimo primeras filas
print(evolucion_categorias_df.head())

# 4. Distribución de los streamers si los clasificamos por volúmenes de audiencia y horas realizadas

# Nuevo dataframe con solo las columnas necesarias
df4 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["streamer_name", "viewer_count", "captured_at"])

# cambio tipo de dato captured_at
df4["captured_at"] = pd.to_datetime(df4["captured_at"])

# Agrupo los datos por la columna "streamer_name" y calculo la suma de espectadores y el conteo de capturas para cada streamer
streamers_df = df4.groupby("streamer_name").agg({"viewer_count": "sum", "captured_at": "count"}).reset_index()
streamers_df.columns = ["streamer_name", "viewer_count", "num_captures"]

# Calcular las horas de directo aproximadas dividiendo el número de capturas por 4
streamers_df["hours_streamed"] = streamers_df["num_captures"] / 4

# Creo un nuevo csv a partir del dataframe
streamers_df.to_csv("streamers.csv", index=False)

# Muestro primeras filas
print(streamers_df.head())

# 5. Evolución (captura a captura) de la desviación estándar en el volúmen de espectadores
# Creo un df con las columnas necesarias
df5 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["captured_at", "viewer_count"])
# Cambio tipo de dato captured_at
df5["captured_at"] = pd.to_datetime(df5["captured_at"])

# Agrupo los datos por la columna "captured_at" y calculo la desviación estándar de espectadores
desviacion_espectadores_df = df5.groupby("captured_at")["viewer_count"].std().reset_index()
desviacion_espectadores_df.to_csv("desviacion_espectadores.csv", index=False)

# Imprimo primeras filas
print(desviacion_espectadores_df.head())