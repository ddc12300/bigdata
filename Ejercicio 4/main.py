import json
import csv
import pandas as pd
from glob import glob

# Creo una lista vacía para almacenar los datos de los tweets procesados
mis_datos = []

# Itero sobre todos los archivos JSON en la carpeta 'api_responses'
for archivo in glob("api_responses/*.json"):
    # Abro y leo el archivo JSON
    with open(archivo, "r") as f:
        respuesta_json = json.load(f)

        # Extraigo los tweets y los usuarios del JSON
        tweets = respuesta_json["data"]
        usuarios = respuesta_json["includes"]["users"]

        # Proceso cada tweet
        for tweet in tweets:
            author_id = tweet["author_id"]
            username = None
            followers_count = None

            # Busco el nombre de usuario y el recuento de seguidores para author_id
            for usuario in usuarios:
                if usuario["id"] == author_id:
                    username = usuario["username"]
                    followers_count = usuario["public_metrics"]["followers_count"]
                    break

            # Extraigo hashtags
            hashtags = []
            if "entities" in tweet and "hashtags" in tweet["entities"]:
                hashtags = [hashtag["tag"] for hashtag in tweet["entities"]["hashtags"]]

            # Creo un diccionario con la información procesada del tweet
            tweet_procesado = {
                "text": tweet["text"],
                "author_id": author_id,
                "username": username,
                "followers_count": followers_count,
                "hashtags": hashtags,
                "retweet_count": tweet["public_metrics"]["retweet_count"],
                "reply_count": tweet["public_metrics"]["reply_count"],
                "like_count": tweet["public_metrics"]["like_count"],
                "quote_count": tweet["public_metrics"]["quote_count"],
                "created_at": tweet["created_at"],
                "conversation_id": tweet["conversation_id"],
                "lang": tweet["lang"],
            }

            # Extraigo menciones

            # Si el tweet contiene un campo llamado "entities" y dentro de "entities" hay otro campo llamado "mentions", entonces procedo a extraer las menciones.
            if "entities" in tweet and "mentions" in tweet["entities"]:

                # Las menciones son otros usuarios de Twitter que han sido mencionados en el tweet.
                # tweet_procesado["mentions"] es una lista que contendrá los nombres de usuario de las menciones.
                # Utilizo una comprensión de lista para iterar sobre cada mención en tweet["entities"]["mentions"].
                # Para cada mención, extraigo el nombre de usuario utilizando mention["username"] y lo agrego a la lista.

                tweet_procesado["mentions"] = [mention["username"] for mention in tweet["entities"]["mentions"]]
            # Si no hay "entities" o "mentions" en el tweet, entonces no hay menciones.
            else:
                # En este caso, asigno una lista vacía a tweet_procesado["mentions"] para indicar que no hay menciones en este tweet.
                tweet_procesado["mentions"] = []

            # Añado el tweet procesado a mi lista de datos
            mis_datos.append(tweet_procesado)

# Crear DataFrame
df = pd.DataFrame(mis_datos)

# Reemplazar los saltos de línea en la columna 'text' con un espacio
df['text'] = df['text'].str.replace('\n', ' ').replace('\r', ' ')

# Guardar el DataFrame en un archivo CSV utilizando el carácter de tabulación '\t' como delimitador
df.to_csv("tweets.csv", index=False, sep='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Extraigo menciones y las guardo en un archivo CSV para Gephi

# Creo una lista vacía llamada edges
# Esta lista almacenará las relaciones entre los usuarios y las menciones en los tweets.
# Cada elemento de la lista será una tupla que contiene el nombre de usuario del autor del tweet (Source) y el nombre de usuario de la mención (Target).
edges = []

# Itero sobre cada fila del dataframe creado anteriormente
for _, fila in df.iterrows():
    # Extraigo el nombre de usuario del autor del tweet de la fila actual y lo guardo en la variable 'user'
    user = fila["username"]

    # Añado cada mención como una tupla de (usuario, mención) a la lista de 'edges'
    # Itero sobre cada mención en la columna "mentions" de la fila actual
    for mention in fila["mentions"]:
        # Creo una tupla con el nombre de usuario del autor del tweet (user) y el nombre de usuario de la mención (mention)
        # Añado la tupla a la lista 'edges'
        edges.append((user, mention))

# Creo un DataFrame con las relaciones de menciones y lo guardo en un archivo CSV
edges_df = pd.DataFrame(edges, columns=["Source", "Target"])
edges_df.to_csv("edges_gephi.csv", index=False)