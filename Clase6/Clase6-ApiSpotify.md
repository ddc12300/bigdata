https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album

Cada vez que hacemos una peticion 

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Establece las credenciales de la API de Spotify
SPOTIPY_CLIENT_ID = 'CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'CLIENT_SECRET'

# Autentica con las credenciales del cliente
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Obtiene las listas de reproducción públicas del usuario 'spotify'
playlists = sp.user_playlists('spotify')

# Itera sobre las listas de reproducción y las imprime
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s%s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    
    # Verifica si hay más páginas de resultados
    if playlists['next']:
        playlists = sp.next(playlists)  # Obtiene la siguiente página de resultados
    else:
        playlists = None  # No hay más páginas de resultados

```

Un graph tiene

- 2 nodos que deben estar unidos por una aresta y esta aresta puede ser dirigida o no dirigida, una aresta dirigida dice que un nodo dirige hacia otro.

Necesito generar un fichero que diga source y target.

La cantidad de recomendaciones que puede hacer un nodo es el grado de salida. El tamaño del nodo hay que hacerlo según el nodo de salida, y podriamos saber que artistas recomiendan a mas artistas.

Buscar como utilizar gephi a traves de csv.

