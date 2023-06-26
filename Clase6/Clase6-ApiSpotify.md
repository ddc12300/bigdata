#API de Spotify

Web: https://developer.spotify.com/

### Preparación

Antes de hacer cualquier solicitud, necesitamos importar las bibliotecas y establecer las credenciales de la API de Spotify. 

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Establecer las credenciales de la API de Spotify
SPOTIPY_CLIENT_ID = 'CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'CLIENT_SECRET'

# Autenticarse con las credenciales del cliente
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
```

### Obtención de listas de reproducción

Primero, vamos a obtener las listas de reproducción públicas del usuario 'spotify':

```python
playlists = sp.user_playlists('spotify')
```

### Mostrando las listas de reproducción

A continuación, iteraremos sobre las listas de reproducción para imprimirlas.

```python
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    
    # Verificación de si hay más páginas de resultados
    if playlists['next']:
        playlists = sp.next(playlists)  # Obtiene la siguiente página de resultados
    else:
        playlists = None  # No hay más páginas de resultados
```

## Grafos y Gephi

Un grafo consta de dos nodos que deben estar unidos por una arista. La arista puede ser dirigida o no dirigida. Una arista dirigida indica que un nodo se dirige hacia otro.

Para utilizar Gephi a través de archivos CSV, necesitamos generar un archivo que incluya las columnas "source" y "target" (origen y destino).

El grado de salida de un nodo es el número de recomendaciones que puede hacer. Podemos ajustar el tamaño de un nodo según su grado de salida, lo que nos permitirá identificar fácilmente los artistas que recomiendan a más artistas.



