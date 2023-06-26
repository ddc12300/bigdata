
Ejercicio 2 Pandas - Clase 2

```Python

import pandas as pd

# Importar el dataset
dataset = pd.read_csv('./dataset_youtube.csv')

# Mostrar número de filas y columnas del dataset
print(f"El dataset completo tiene {dataset.shape[0]} filas y {dataset.shape[1]} columnas")

# Mostrar nombres de las columnas del dataset
print("Las columnas del dataset son: ")
print(list(dataset.columns))

#limpiar datos

# Eliminar columnas innecesarias
dataset = dataset.drop(['position'], axis=1, inplace=True)

# Contar vídeos por canal
videos_por_canal = dataset['channelTitle'].value_counts()
print(f"El canal NPR ha publicado {videos_por_canal['NPR Music']} vídeos y el canal KEXP ha publicado {videos_por_canal['KEXP']} vídeos")

# Calcular promedio de espectadores, comentarios y likes por canal
promedios_por_canal = dataset.groupby('channelTitle')['viewCount', 'commentCount', 'likeCount'].mean()


print("El promedio de espectadores/comentarios/likes para el canal NPR es:")
print(promedios_por_canal.loc['NPR Music'])
print("El promedio de espectadores/comentarios/likes para el canal KEXP es:")
print(promedios_por_canal.loc['KEXP'])

# Calcular desviación de cada vídeo respecto al promedio de espectadores, comentarios y likes
desviacion_por_canal = dataset.groupby('channelTitle')['viewCount', 'commentCount', 'likeCount'].apply(lambda x: x - x.mean())
dataset['espectadores_desv'] = desviacion_por_canal['viewCount']
dataset['comentarios_desv'] = desviacion_por_canal['commentCount']
dataset['likes_desv'] = desviacion_por_canal['likeCount']

print(dataset['espectadores_desv'])

print(dataset['comentarios_desv'])

print(dataset['likes_desv'])

# Encontrar el vídeo más visto y más comentado por canal
mas_visto_por_canal = dataset.loc[dataset.groupby('channelTitle')['viewCount'].idxmax()]

print(f"mas visto del canal {mas_visto_por_canal}")

mas_comentado_por_canal = dataset.loc[dataset.groupby('channelTitle')['commentCount'].idxmax()]

print(f"mas comentado del canal {mas_comentado_por_canal}")

# Crear nuevo dataset final
nuevo_dataset = dataset[['channelTitle', 'publishedAt', 'viewCount', 'commentCount', 'likeCount', 'espectadores_desv', 'comentarios_desv', 'likes_desv']]

```




