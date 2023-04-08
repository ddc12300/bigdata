https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album

Cada vez que hacemos una peticion 

```python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
SPOTIPY_CLIENT_ID='9137f3f08bd94b3db5a7407605c21da1'  
SPOTIPY_CLIENT_SECRET='bac8514357354703be8253f77355a593'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlists = sp.user_playlists('spotify')  
while playlists:  
    for i, playlist in enumerate(playlists['items']):  
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))  
    if playlists['next']:  
        playlists = sp.next(playlists)  
    else:  
        playlists = None

```



un graph tiene

2 nodos que deben estar unidos por una aresta y esta aresta puede ser dirigida o no dirigida, una aresta dirigida dice que un nodo dirige hacia otro.

necesito generar un fichero que diga source y target.

la cantidad de recomendaciones que puede hacer un nodo es el grado de salida. El tamaño del nodo hazmelo segun el nodo de salida, y podriamos saber que artistas recomiendan a mas artistas.

buscar como utilizar gephi a traves de csv.

