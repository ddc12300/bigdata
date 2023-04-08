```python

from twitchAPI.twitch import Twitch  
import pandas as pd  
import datetime  
  
twitch = Twitch('jhbumt1og6i9nsn3uwfvfxh2xwykw7', 'gzfkz2k4jxq94bdhdc4n5oydpjmjlc')  
  
stream = twitch.get_streams(first=20, language="es")  
  
dades = stream["data"]  
  
llista_dataframes = []  
  
for dada in dades:  
    time = datetime.datetime.now()  
    user_id = dada["user_id"]  
    user_name = dada["user_name"]  
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
        "title": title,  
        "viewer_count": viewer_count,  
        "started_at": started_at,  
        "is_mature": is_mature,  
    }, index=[0])  
    llista_dataframes.append(df)  
  
final_dataframe = pd.concat(llista_dataframes)  
final_dataframe.to_csv("export.csv", index=False)

```


funciones:

```

variable = "hola"  
  
def loquesea(variable):  
    print(variable)  
  
loquesea(variable)

```

revisar funcion

```pyhton

from twitchAPI.twitch import Twitch  
import pandas as pd  
import datetime  
import time  
  
twitch = Twitch('jhbumt1og6i9nsn3uwfvfxh2xwykw7', 'gzfkz2k4jxq94bdhdc4n5oydpjmjlc')  
now = datetime.datetime.now()  
  
idiomes=["es","ca"]  
llista_dataframes = []  
cursor_dummy= None  
def crida(cursor,lang):  
    streams = twitch.get_streams(first=100, language=lang, after=cursor)  
    dades = streams["data"]  
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
    print(len(llista_dataframes))  
    try:  
        streams["pagination"]["cursor"]  
        cursor= streams["pagination"]["cursor"]  
        print(cursor)  
        print("dormint")  
        time.sleep(0.12)  
        crida(cursor,lang)  
    except KeyError:  
        print("Ultima Pagina")  
        pass  
  
for lang in idiomes:  
    crida(cursor_dummy,lang)  
    final_dataframes = pd.concat(llista_dataframes)  
    final_dataframes.to_csv(f"export{lang}.csv", index=False)  
    print(final_dataframes)

```

