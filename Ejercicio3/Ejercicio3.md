# Ejercicio de análisis de datos: Febrero en Twitch

Este análisis se basa en datos obtenidos de la API de Twitch correspondientes al mes de febrero.

## 1.  ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

![ej1](https://user-images.githubusercontent.com/116378134/232343563-4efd29cb-3b30-4096-bfbf-a466a6f22f2b.PNG)

Durante el mes de febrero, se ha observado una clara tendencia ascendente en la evolución de espectadores en la plataforma de streaming. Esta tendencia se ha mantenido regular durante todo el mes, pero lo que realmente llama la atención son los picos de audiencia que se producen en determinados momentos, especialmente en los los últimos días del mes.

Uno de los principales motivos de estos picos de audiencia es la "Kings League", una liga de fútbol llevada a cabo en twitch. Esta competición ha conseguido atraer a un gran número de espectadores, alcanzando el mayor pico del mes el día 26 de febrero. En este día, el famoso deportista Ronaldinho Gaúcho se unió al equipo de Ibai Llanos, Porcinos FC, lo que generó un gran interés entre los usuarios.

Además sucedieron en estos mismo dias otros sucesos como la presentación de la Velada del Año 3 de ibai y en anuncio de la partición de AuronPlay en los "Squid Craft Games".


## 2.  ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?

![ej2](https://user-images.githubusercontent.com/116378134/232343580-a8244379-3bc9-4064-9463-c7d0d4f84fa2.PNG)

En el primer grafico de barras observamos que las categorias más vistas según cantidad de viewers son las siguientes:

- Just Chatting: Es la categoría más popular entre los espectadores debido a su naturaleza. Los streamers pueden participar en conversaciones con sus seguidores y abordar una amplia variedad de temas, desde noticias de actualidad hasta experiencias personales. Esta interacción en tiempo real permite a los usuarios sentirse más conectados con los creadores de contenido y disfrutar de una experiencia más personalizada.
- Sports: Habria que analizar si otros meses esta categoria dispone de tanta audiencia, ya que para este mes, como he comentado en el ejercicio 1 se dio a cabo varios eventos de la Kings League lo que ha producido que esta sea la segunda caterogia más vista.
- League of legends y Minecraft: Estos videojuegos han sido siempre los más populares en Twitch desde sus inicios, destacar que son los juegos con más videojugadores por lo que es normal que existe una relación con la cantidad de viewers.
- Hogwarts Legacy: Debido al lanzamiento del juego, las transmisiones en Twitch tuvieron un aumento significativo, que luego fue disminuyendo.


![ej2-2](https://user-images.githubusercontent.com/116378134/232344217-83661102-86ed-4ae9-9f7c-ab03f9f5e28a.PNG)

Por otro lado tenemos que el juego con más horas emitidas es Fortnite, es normal ya que este tiene una popularidad global, es muy facil acceder a este desde cualquier plataforma. Si nos fijamos en el ranking no encontramos la categoria de sports, esto nos hace pensar que su gran cantidad de viewers viene dada dada principalmente de la Kings League.

## 3. ¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?

![ej3](https://user-images.githubusercontent.com/116378134/232344538-fffdc906-97a2-4b72-927d-8deec6b7f9fa.PNG)

A excepción de sports que ha dado picos en los días que se han realizado eventos de la kings league, el resto de categorias vemos que han sido relativamente estables en cuanto a viewers a lo largo del mes.


## 4. ¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?

Para distribuir los streamers por volumenes de audiencia y horas realizadas los clasifique según audiencia: baja < 10000 viewers, media < 50000 viewers y alta todo lo demás. Y por horas < 10 horas como pocas, menos de 50 moderadas y todo lo demás muchas. A partir de esto cree 3 graficos de dispersión según audiencia alta media y baja, añadiendo colores según las horas stremeadas para ver si se encuentra una relación entre horas stremeadas y cantidad de audiencia:

![ejj4-1](https://user-images.githubusercontent.com/116378134/232347423-5161fd28-8107-4355-aa95-120334656210.PNG)

Primero para una audiencia alta observamos que los streamers con una cantidad mayor de views no siempre va relacionado con las horas stremeadas,a destacar de nuevo el usuario kingsleague ya que con una cantidad de horas moderada se encuentra el número 1. Por otro lado con muchas horas encontramos streamers conocidos como Ibai, Illojuan, elxokas, entre otros. Más o menos con la misma cantidad de viewers encontramos a otros como Rubius o auronplay que pese a stremear de forma moderada disponen de una gran audidencia. Por último destacar por ejemplo viviendoenlacalle, un streamer famosos por realizar irl de su vida como indica su nombre en la calle, podriamos decir que su gran cantidad de audiencia podria tener algo de relación con la gran cantidad de horas que emite. En este grafico de audiencia alta apenas se observan streamers con pocas horas emitidas.

![ejj4-2](https://user-images.githubusercontent.com/116378134/232347428-81f89404-bc56-4203-851e-ed7b383425ec.PNG)

Por otro lado con una audiencia media observamos diferentes tendencias, no se observa que haya una relación significativa entre viewers y cantidad de horas emitidas, observamos streamers con pocas horas superando a muchos con moderadas y muchas, en este caso ya se empieza a ver una tendencia con streamers con más horas streameadas, pese que no significa que tengan más viewers.

![ejj4-3](https://user-images.githubusercontent.com/116378134/232347437-2ec3782f-5440-490f-b2a6-cad0871a636f.PNG)

Por ultimo en el grafico de audiencia baja vemos 3 columnas completas a la izquierda del grafico, cosa que nos da a entender que en principio no existe una relación de horas con cantidad de viewers, pero si nos fijamos en como transcurre el resto del grafico vemos una linea ascendiente, llegando sobre los 3k viewers y las 650 horas, sobre esto podemos deducir que para audiencias bajas la cantidad de horas emitidas puede llegar a influir algo.

## 5. ¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?


![ej5](https://user-images.githubusercontent.com/116378134/232343593-68151b7a-b6e2-474c-9ada-d30aa4009c2b.PNG)

La evolución de la desviación estándar en el volumen de espectadores puede analizarse examinando las capturas tomadas en diferentes momentos del período en estudio. Comparando la desviación estándar mínima de 49, que se registró el 23/02, con la máxima de 8329, ocurrida el 26/02, podemos identificar las fluctuaciones en la dispersión de la audiencia a lo largo del tiempo.

5En términos de polarización de audiencias, los momentos en los que las audiencias están más polarizadas se corresponden con los días en que la desviación estándar es más alta. Por ejemplo, el 26/02, con una desviación estándar de 8329, indica que hubo una gran variabilidad en el volumen de espectadores, lo que sugiere que ciertos eventos o streamers atrajeron a una cantidad significativamente mayor de espectadores en comparación con otros. Esto puede deberse a eventos especiales, como la participación de Ronaldinho Gaúcho en la "Kings League" o anuncios importantes por parte de streamers populares.

Por otro lado, los momentos en los que la distribución de audiencia es más uniforme coinciden con aquellos días en que la desviación estándar es más baja. En este caso, el 23/02, con una desviación estándar de 49, muestra una menor variabilidad en el volumen de espectadores, lo que indica que la audiencia estaba más equilibrada entre los diferentes streamers y contenidos ofrecidos en la plataforma.


