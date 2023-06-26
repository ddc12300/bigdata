
Introducción ejercicio 3


https://adriapadilla.github.io/bigdata-uab/ejercicios/ejercicio_3.html


```python

import pandas as pd

#Opció 1
#¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?
df = pd.read_csv("feb_23_es_simple.csv",sep="\t", usecols=["captured_at","viewer_count"])
df2 = df.groupby("captured_at")["viewer_count"].sum().reset_index()
df2.to_csv("test.csv")

#Opció 2

list = []

df = pd.read_csv("feb_23_es_simple.csv", chunksize=100000, sep="\t", usecols=["captured_at","viewer_count"])

for chunk in df:
    df2 = chunk.groupby("captured_at")["viewer_count"].sum().reset_index()
    list.append(df2)
    print(chunk)

final_frame_1 = pd.concat(list)
final_frame_2 = final_frame_1.groupby("captured_at")["viewer_count"].sum().reset_index()
final_frame_2.to_csv("test_2.csv")

```


