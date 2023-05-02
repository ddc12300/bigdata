import json
import csv
import pandas as pd
from glob import glob

# Creo una lista vacía para almacenar los datos de los tweets procesados
mis_datos = []

# Creo una lista vacía para almacenar los datos de los hashtags procesados
hashtags_datos = []

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

            # Añadir hashtags y tweet_id a hashtags_datos
            for hashtag in hashtags:
                hashtags_datos.append({"tweet_id": tweet["id"], "hashtag": hashtag})

            # Creo un diccionario con la información procesada del tweet
            tweet_procesado = {
                "tweet_id": tweet["id"],
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

            # Añado el tweet procesado a mi lista de datos
            mis_datos.append(tweet_procesado)

# Crear DataFrame
df = pd.DataFrame(mis_datos)

# Reemplazar los saltos de línea en la columna 'text' con un espacio
df['text'] = df['text'].str.replace('\n', ' ').replace('\r', ' ')

# Guardar el DataFrame en un archivo CSV utilizando el carácter de tabulación '\t' como delimitador
df.to_csv("tweets.csv", index=False, sep='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Crear DataFrame de hashtags
hashtags_df = pd.DataFrame(hashtags_datos)

# Guardar el DataFrame de hashtags en un archivo CSV
hashtags_df.to_csv("hashtags.csv", index=False)