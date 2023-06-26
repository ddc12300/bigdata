
- Examinar documentos y cómo están almacenados (por ejemplo, separador es el tabulador).
- Usar **.glob** para leer más de un documento dentro de una misma carpeta.

### Código para leer múltiples documentos de Twitch:

```Python
import pandas as pd
import glob

dataset = glob.glob("datasets/twitch_*")

for data in datasets:
    df = pd.read_csv(data, sep="\t")
    print(df)
```

- Procesar datos en chunks (por ejemplo, 100 archivos a la vez) es más óptimo que procesar todo en conjunto (200 archivos).

### Código para procesar datos de Twitch en chunks:

```Python
import pandas as pd
import glob

datasets = glob.glob("datasets/twitch_*")

llista = []
llista_streamers = ["auronplay", "IlloJuan"]

for data in datasets:
    df = pd.read_csv(data, sep="\t")
    df2 = df[df['steamer_name']] == steamer]
    llista.append(df)
    print(df)

df_final = pd.concat(llista)
df_final.to_csv(f"{steamer}-dataset.csv", index=False)
```

---

## Tableau

- Guardar en Tableau Public usando servidor.
- Datos final-dataset: extraer datos y guardarlos.

---

## Consejos

- Utilizar glob para la nueva práctica, ejercicio 4.

---

## Análisis de JSON en Twitter

- Analizar campo "entities": identifica automáticamente hashtags con IA.
- Campo "referenced_tweets": indica si el tweet proviene de otro tweet.