
El siguiente código hace uso de la API de Twitch para obtener información sobre los 20 principales streams en español. Luego, crea un DataFrame de Pandas por cada stream, agregando información relevante como el tiempo de captura, el nombre de usuario, el juego, el título, la cantidad de espectadores, la hora de inicio y si el stream es para adultos. Finalmente, concatena todos los DataFrames individuales en un DataFrame único y lo exporta como un archivo CSV llamado "export.csv".

```python
from twitchAPI.twitch import Twitch  
import pandas as pd  
import datetime  
  
# Autenticación en la API de Twitch (Cambiar KEY por tu key de twitch)
twitch = Twitch('KEY')  
  
# Obtener 20 principales streams en español
stream = twitch.get_streams(first=20, language="es")  
  
dades = stream["data"]  
  
llista_dataframes = []  
  
# Crear un DataFrame por cada stream
for dada in dades:  
    time = datetime.datetime.now()  
    user_id = dada["user_id user_name = dada["user_name"]  
    game_id = dada["game_id"]  
    game_name = dada["game_name"]  
    title = dada["title"]  
    viewer_count = dada["viewer_count"]  
    started_at = dada["started_at"]  
    is_mature = dada["is_mature"]  
  
    df = pd.DataFrame({  
        "captured_at": time,  
        "user_id": user_id,  
        "user_name": user_name,  
        "game_id": game_id,  
        "game_name": game_name,
        "title": title,  
        "viewer_count": viewer_count,  
        "started_at": started_at,  
        "is_mature": is_mature,  
    }, index=[0])  
    llista_dataframes.append(df)  
  
# Concatenar todos los DataFrames individuales en un DataFrame único
final_dataframe = pd.concat(llista_dataframes)  

# Exportar el DataFrame final como un archivo CSV
final_dataframe.to_csv("export.csv", index=False)

```


Funciones:

Este código utiliza la API de Twitch para obtener información sobre los streams en español y catalán. Para cada lengua, el script recorre todas las páginas de resultados (hasta un máximo de 100 streams por página), creando un DataFrame de Pandas por cada stream. Luego, concatena todos los DataFrames individuales en un DataFrame único y lo exporta como un archivo CSV llamado "export{lang}.csv", donde {lang} es el código de idioma ("es" para español y "ca" para catalán).

El script utiliza una función recursiva `crida()` para recorrer todas las páginas de resultados de la API de Twitch. También incluye un tiempo de espera de 0.12 segundos entre cada llamada a la API para evitar superar el límite de solicitudes de la API por minuto.


```python
from twitchAPI.twitch import Twitch
import pandas as pd
import datetime
import time

# Inicializa la API de Twitch
twitch = Twitch('jhbumt1og6i9nsn3uwfvfxh2xwykw7', 'gzfkz2k4jxq94bdhdc4n5oydpjmjlc')
now = datetime.datetime.now()

# Lista de idiomas para buscar streams
idiomes = ["es", "ca"]
llista_dataframes = []
cursor_dummy = None

# Función para obtener streams y agregarlos a la lista de dataframes
def crida(cursor, lang):
    # Obtiene los streams para el idioma y cursor dados
    streams = twitch.get_streams(first=100, language=lang, after=cursor)
    dades = streams["data"]
    
    # Itera sobre cada stream y crea un dataframe con la información
    for dada in dades:
        viewer_count = dada["viewer_count"]
        user_name = dada["user_name"]
        user_id = dada["user_id"]  
        game_name = dada["game_name"]  
        title = dada["title"]  
        game_id = dada["game_id"]  
        started_at = dada["started_at"]  
        is_mature = dada["is_mature"]  
        captured_at = now  
        language = dada["language"]  
  
        df = pd.DataFrame({  
            "user_name": user_name,  
            "user_id": user_id,  
            "viewer_count": viewer_count,  
            "game_name": game_name,  
            "game_id": game_id,  
            "title": title,  
            "started_at": started_at,  
            "is_mature": is_mature,  
            "captured_at": captured_at,  
            "lang": language,  
        }, index=[0])  
        llista_dataframes.append(df)  
    
    # Verifica si hay más páginas de resultados
    try:  
        streams["pagination"]["cursor"]  
        cursor = streams["pagination"]["cursor"]  
        print(cursor)  
        print("dormint")  
        time.sleep(0.12)  # Espera antes de hacer otra llamada a la API para evitar superar el límite de solicitudes por minuto
        crida(cursor, lang)  # Llama a la función de forma recursiva con el nuevo cursor
    except KeyError:  
        print("Ultima Pagina")  # No hay más páginas de resultados
        pass

# Itera sobre cada idioma y llama a la función para obtener los streams
for lang in idiomes:
    crida(cursor_dummy, lang)  # Llama a la función con el idioma y un cursor vacío
    final_dataframes = pd.concat(llista_dataframes)  # Concatena todos los dataframes en uno solo
    final_dataframes.to_csv(f"export{lang}.csv", index=False)  # Guarda el dataframe en un archivo CSV
    print(final_dataframes)  # Imprime el dataframe final
```

