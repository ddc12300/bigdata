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

# Cargo el csv en un dataframe escogiendo solo las columnas necesarias para optimizar la carga
# La función pd.read_csv() lee un archivo .csv y lo convierte en un dataframe 
df1 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["captured_at", "viewer_count"])

# Convierto la columna captured_at a tipo de dato datetime
# La función pd.to_datetime() convierte una columna a tipo de dato datetime
df1["captured_at"] = pd.to_datetime(df1["captured_at"])

# Agrupo los datos en un dataframe por captured_at y viewer count utilizando la función groupby(), y utilizo la función .sum() para sumar los valores de 'viewer_count' para cada captura y finalmente utilizo reset_index() para convertir los índices en una columna del nuevo dataframe que creo llamado que llamo evolucion_espectadores_df
evolucion_espectadores_df = df1.groupby("captured_at")["viewer_count"].sum().reset_index()

# guardo el resultado en un csv
# La función .to_csv() guarda el dataframe en un archivo .csv
evolucion_espectadores_df.to_csv("evolucion_espectadores.csv", index=False)

# imprimo las primeras filas del dataset
# La función .head() muestra las primeras filas del dataframe
print(evolucion_espectadores_df.head())

# 2. Categorías más vistas y en las que más horas de directo se han realizado

# Cargamos el csv en un dataframe escogiendo solo las columnas necesarias
df2 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["game_name", "viewer_count"])

# Calculo la suma total de espectadores y el número de capturas por categoría
# Con groupby() agrupo el dataframe por categoría (game_name), luego utilizo .agg() para calcular la suma total de espectadores ('sum') y el número de capturas por streamer con ('count') para cada categoria, y finalmente utilizo reset_index() para convertir los índices en una columna del nuevo dataframe que creo llamado categorias_mas_vistas_df
categorias_mas_vistas_df = df2.groupby("game_name")["viewer_count"].agg(['sum', 'count']).reset_index()

# Renombro las columnas
categorias_mas_vistas_df.columns = ["game_name", "total_viewers", "num_captures"]

# Calculo las horas de directo aproximadas dividiendo el número de capturas por 4, ya que se hace una captura cada 15 min 60/15=4, creando una nueva columna llamada hours_direct
categorias_mas_vistas_df["hours_direct"] = categorias_mas_vistas_df["num_captures"] / 4

# Guardo el nuevo dataset en un archivo csv
categorias_mas_vistas_df.to_csv("categorias_mas_vistas.csv", index=False)

# imprimo primeras filas
print(categorias_mas_vistas_df.head())

# 3. Evolución (captura a captura) de las categorías a lo largo del mes
# Cargo el csv en un dataframe escogiendo solo las columnas necesarias
df3 = pd.read_csv("feb_23_es_simple.csv", sep="\t", usecols=["captured_at", "game_name", "viewer_count"])

# cambio tipo de dato captured_at de nuevo
df3["captured_at"] = pd.to_datetime(df3["captured_at"])

# Extraigo las 5 categorías con más espectadores a partir del df del ejercicio 2
# La función .nlargest() devuelve las n filas con los valores más grandes de una columna y con tolist() lo convierto en una lista
top5_categorias_viewers = categorias_mas_vistas_df.nlargest(5, "total_viewers")["game_name"].tolist()

# Filtro el dataframe para incluir solo las 5 categorías con más espectadores
# La función .isin() filtra el dataframe por aquellos valores que coinciden con los de la lista creada 
df3 = df3[df3["game_name"].isin(top5_categorias_viewers)]

# Calculo la evolución (captura a captura) de las categorías a lo largo del mes agrupando por captured_at y game_name, y sumando los espectadores para cada categoria
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

# Calculo las horas de directo aproximadas dividiendo el número de capturas por 4
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
# Con la función .std() calculo la desviación estándar de la columna viewer_count
desviacion_espectadores_df = df5.groupby("captured_at")["viewer_count"].std().reset_index()
desviacion_espectadores_df.to_csv("desviacion_espectadores.csv", index=False)

# Imprimo primeras filas
print(desviacion_espectadores_df.head())
