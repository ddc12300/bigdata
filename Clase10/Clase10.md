Requests y BeautifulSoup

- **Requests**: permite conectarse a sitios web y obtener su contenido.
- **BeautifulSoup**: interpreta el contenido HTML.
- Realizar *scrapping* de la Wikipedia de Eurovisión para extraer datos de cada año.

### Extraer lista de canciones de Eurovisión desde Wikipedia:

```Python
import requests
import pandas as pd
import lxml
from bs4 import BeautifulSoup

# Definir rango de años para buscar en Wikipedia
anys = range(2000, 2023, 1)

llista_df = []

# Para cada año, realizar solicitud web y extraer información de la tabla de Eurovisión
for any in anys:
    try:
        resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{any}")
        soup = BeautifulSoup(resposta.text, 'html.parser')
        final = soup.find('span', id="Final")
        tabla = final.find_next("table")
        
        # Convertir tabla HTML a DataFrame
        df = pd.read_html(tabla.prettify())[0]
        df["any"] = any
        df.columns.values[0] = "N."
        df.columns.values[5] = "Puntos"
        df.columns.values[2] = "Cantante"

        llista_df.append(df)
    except AttributeError:
        print(f"error {any}")

# Concatenar DataFrames y exportar a Excel
final = pd.concat(llista_df)
final.to_excel("llista_final(3).xlsx", index=False)
```

### Extraer información de Spotify utilizando la lista de canciones generada anteriormente (Código incompleto, ver más abajo el código completo):

```Python
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import lxml
from bs4 import BeautifulSoup

df = pd.read_excel("llista_final(3).xlsx")

client_id = 'clau_id'
client_secret = 'clau_secret'

# Autenticación para la API de Spotify
client_id = 'clau_id'
client_secret = 'clau_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Iterar en las filas de DataFrame y buscar información en Spotify
for index, row in df.iterrows():
    artista = row["Cantante"]
    track = row["Canción"]
    
    # Quitar comillas del título de la canción
    try:
        p_track = track.split("«")[1].split("»")[0]
    except IndexError:
        p_track = track

    print(artista, track)
    q = f"{p_track} {artista} eurovision"
    info = sp.search(q, limit=1, offset=0, type='track', market=None)
    print(info)
```