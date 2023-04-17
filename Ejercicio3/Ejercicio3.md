# Ejercicio de análisis de datos: Febrero en Twitch

Este análisis se basa en datos obtenidos de la API de Twitch correspondientes al mes de febrero.

## 1.  ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

![ej1](https://user-images.githubusercontent.com/116378134/232343563-4efd29cb-3b30-4096-bfbf-a466a6f22f2b.PNG)

Durante el mes de febrero, se ha registrado una tendencia ascendente en el número de espectadores en la plataforma de streaming. Esta tendencia se ha mantenido constante a lo largo del mes; sin embargo, lo que realmente resalta son los picos de audiencia que ocurren en momentos específicos, especialmente en los últimos días del mes.

Investigando noticias en internet sobre eventos relevantes que sucedieron en esos días, encontramos los siguientes acontecimientos destacados:

Uno de los principales factores detrás de estos picos de audiencia es la "Kings League", una liga de fútbol llevada a cabo en Twitch. Esta competición ha logrado atraer a un gran número de espectadores, alcanzando su máximo pico el 26 de febrero. En ese día, el famoso deportista Ronaldinho Gaúcho se unió al equipo de Ibai Llanos, Porcinos FC, generando un gran interés entre los usuarios.

Además, en esos mismos días ocurrieron otros eventos relevantes, como la presentación de la Velada del Año 3 de Ibai el 27 de febrero y el regreso de AuronPlay a Twitch después de un tiempo sin emitir, anunciando su participación en la serie Squid Craft Games 2 el 28 de febrero.

Estos acontecimientos han contribuido a los picos de audiencia observados en la plataforma durante el mes de febrero, demostrando el poder de atracción de eventos especiales, competiciones y la participación de personalidades conocidas en el ámbito del streaming. La colaboración entre estos elementos parece un factor clave para mantener el interés de la audiencia y generar un mayor engagement.


## 2.  ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?

![ej2](https://user-images.githubusercontent.com/116378134/232343580-a8244379-3bc9-4064-9463-c7d0d4f84fa2.PNG)

En el primer gráfico de barras observamos que las categorías más vistas según cantidad de viewers son las siguientes:

- Just Chatting: Esta categoría es la favorita de los espectadores debido a su versatilidad. Los streamers pueden interactuar con sus seguidores y tratar diversos temas, desde noticias hasta experiencias personales. La interacción en tiempo real permite a los usuarios sentirse más conectados con los creadores de contenido y disfrutar de una experiencia más personalizada.
- Sports: Habria que analizar si otros meses esta categoria dispone de tanta audiencia, ya que para este mes, como he comentado en el ejercicio 1 se dio a cabo varios eventos de la Kings League lo que ha producido que esta sea la segunda caterogia más vista.
- League of legends y Minecraft: Estos videojuegos han sido siempre los más populares en Twitch desde sus inicios, destacar que son los juegos con más videojugadores por lo que es normal que existe una relación con la cantidad de viewers.
- Hogwarts Legacy: Debido al lanzamiento del juego, las transmisiones en Twitch tuvieron un aumento significativo, que luego fue disminuyendo.


![ej2-2](https://user-images.githubusercontent.com/116378134/232344217-83661102-86ed-4ae9-9f7c-ab03f9f5e28a.PNG)

Por otro lado, las categorías con más horas de transmisión en Twitch son Fortnite, VALORANT, Just Chatting, League of Legends y Minecraft, debido a su popularidad, accesibilidad, naturaleza competitiva o creativa, y la posibilidad de interactuar con espectadores y compartir experiencias. Estos factores motivan a los streamers a dedicar más horas a la transmisión en estas categorías.

Además, eventos especiales, torneos, y actualizaciones constantes en estos juegos ayudan a mantener el interés de la audiencia y fomentan la participación de los streamers. La combinación de estos elementos contribuye a la alta cantidad de horas de transmisión en estas categorías, consolidando su presencia en la plataforma Twitch.

Si nos fijamos en el ranking no encontramos la categoria de sports, esto nos hace pensar que su gran cantidad de viewers viene dada principalmente de la Kings League.

## 3. ¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?

![ej3](https://user-images.githubusercontent.com/116378134/232344538-fffdc906-97a2-4b72-927d-8deec6b7f9fa.PNG)

La mayoría de las categorías muestran una tendencia estable en cuanto a espectadores, siendo los picos observados el resultado de eventos específicos realizados para dichas categorías. Cabe destacar nuevamente la categoría Sports, donde se aprecian picos en distintas fechas correspondientes a las emisiones de la Kings League, a partir de esto podemos concluir que no existen otros streamings de magnitud similar en esta categoría durante los días en que no se lleva a cabo la Kings League.


## 4. ¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?

Para distribuir los streamers por volumenes de audiencia y horas realizadas los clasifique según:

1. Audiencia:
- Baja: menos de 10,000 espectadores. Este rango incluye a los streamers con una audiencia relativamente pequeña, lo que puede indicar que están comenzando en la plataforma o que su contenido está dirigido a nichos específicos.
- Media: entre 10,000 y 50,000 espectadores. Los streamers en este rango tienen una audiencia significativa y son considerados populares en la plataforma, pero aún no han alcanzado el estatus de superestrella.
- Alta: más de 50,000 espectadores. Este rango se reserva para los streamers más exitosos y reconocidos en la plataforma, que han logrado captar la atención de una gran cantidad de usuarios.

2. Horas de transmisión:
- Pocas: menos de 10 horas. Los streamers en este rango pueden ser ocasionales, transmitiendo sólo en momentos específicos o durante eventos particulares.
- Moderadas: entre 10 y 50 horas. Este rango incluye a los streamers que dedican un tiempo considerable a la plataforma, lo que puede indicar que están comprometidos con sus seguidores y buscan mantener su audiencia.
- Muchas: más de 50 horas. Los streamers en este rango pasan una gran cantidad de tiempo en la plataforma, lo que puede reflejar una dedicación a tiempo completo al streaming o un enfoque en el crecimiento y la consolidación de su audiencia.

Estas clasificaciones permiten analizar y comparar a los streamers de manera más efectiva, facilitando la identificación de tendencias y patrones en relación con el volumen de audiencia y las horas de transmisión. A partir de esto cree 3 graficos de dispersión según audiencia alta media y baja, añadiendo colores según las horas stremeadas para ver si se encuentra una relación entre horas stremeadas y cantidad de audiencia:

![ejj4-1](https://user-images.githubusercontent.com/116378134/232347423-5161fd28-8107-4355-aa95-120334656210.PNG)

En primer lugar, al observar a los streamers con audiencia alta, notamos que la cantidad de visitas no siempre está relacionada con las horas transmitidas. Un ejemplo destacado es el usuario "Kingsleague", que se encuentra en el primer lugar con un número moderado de horas de transmisión. Por otro lado, streamers conocidos como Ibai, Illojuan y Elxokas, transmiten muchas horas, mientras que otros como Rubius y Auronplay, a pesar de transmitir de forma moderada, también cuentan con una gran audiencia. Un caso interesante es "Viviendoenlacalle", un streamer famoso por transmitir en vivo su vida en la calle; su gran cantidad de audiencia podría estar relacionada con la gran cantidad de horas que transmite y la originalidad de su contenido. En este grupo de audiencia alta, rara vez se observan streamers con pocas horas transmitidas, lo que podría indicar que la dedicación y la constancia son factores importantes para alcanzar una audiencia numerosa.

![ejj4-2](https://user-images.githubusercontent.com/116378134/232347428-81f89404-bc56-4203-851e-ed7b383425ec.PNG)

En el caso de los streamers con audiencia media, observamos diferentes tendencias y no parece existir una relación significativa entre la cantidad de visitas y las horas emitidas. Se pueden ver streamers con pocas horas de transmisión superando a muchos con moderadas y muchas horas. Sin embargo, en este grupo ya se empieza a notar una tendencia en la que los streamers con más horas transmitidas podrían tener cierta ventaja, aunque esto no necesariamente se traduzca en más visitas. Esto podría deberse a que los streamers con audiencia media están en proceso de consolidar su base de seguidores y la interacción frecuente con su audiencia es crucial para mantener su interés.

![ejj4-3](https://user-images.githubusercontent.com/116378134/232347437-2ec3782f-5440-490f-b2a6-cad0871a636f.PNG)

Por último, en el gráfico de audiencia baja, inicialmente no parece existir una relación entre las horas de transmisión y la cantidad de visitas, pero al analizar más a fondo el gráfico, se observa una línea ascendente que llega aproximadamente a los 3,000 espectadores y las 650 horas. A partir de esto, se podría inferir que para audiencias bajas, la cantidad de horas transmitidas puede llegar a influir en cierta medida en la cantidad de espectadores. Esto podría deberse a que los streamers con menor audiencia necesitan dedicar más tiempo a construir su base de seguidores y conectar con ellos, lo que podría lograrse a través de una mayor presencia en la plataforma y ofreciendo contenido atractivo y de calidad.

## 5. ¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?


![ej5](https://user-images.githubusercontent.com/116378134/232343593-68151b7a-b6e2-474c-9ada-d30aa4009c2b.PNG)

La evolución de la desviación estándar en el volumen de espectadores puede analizarse examinando las capturas tomadas en diferentes momentos del período en estudio. Comparando la desviación estándar mínima de 49, que se registró el 23/02, con la máxima de 8329, ocurrida el 26/02, podemos identificar las fluctuaciones en la dispersión de la audiencia a lo largo del tiempo.

En términos de polarización de audiencias, los momentos en los que las audiencias están más polarizadas se corresponden con los días en que la desviación estándar es más alta. Por ejemplo, el 26/02, con una desviación estándar de 8329, indica que hubo una gran variabilidad en el volumen de espectadores, lo que sugiere que ciertos eventos o streamers atrajeron a una cantidad significativamente mayor de espectadores en comparación con otros. Esto puede deberse a eventos especiales, como la participación de Ronaldinho en la Kings League o anuncios importantes por parte de streamers populares.

Por otro lado, los momentos en los que la distribución de audiencia es más uniforme coinciden con aquellos días en que la desviación estándar es más baja. En este caso, el 23/02, con una desviación estándar de 49, muestra una menor variabilidad en el volumen de espectadores, lo que indica que la audiencia estaba más equilibrada entre los diferentes streamers y contenidos ofrecidos en la plataforma.

## Conclusiones

En conclusión, el análisis de los datos de Twitch durante el mes de febrero nos permite identificar diversas tendencias y patrones en la plataforma. Entre los hallazgos más destacados se encuentran la evolución ascendente en la cantidad de espectadores, con picos de audiencia relacionados a eventos específicos como la "Kings League" y la participación de personalidades famosas en las transmisiones.

En cuanto a las categorías más vistas, Just Chatting y Sports encabezan la lista, mientras que en términos de horas de directo, Fortnite se mantiene como el juego más transmitido. La evolución de estas categorías a lo largo del mes muestra que, en general, mantienen una tendencia estable, con picos relacionados a eventos puntuales.

Al analizar la distribución de los streamers según el volumen de audiencia y las horas de transmisión, se observa que no existe una relación directa entre ambas variables, pero se pueden identificar ciertas tendencias que podrían estar influyendo en el éxito de los creadores de contenido. Por ejemplo, en el caso de audiencias bajas, las horas de transmisión podrían llegar a influir en la cantidad de espectadores, mientras que para audiencias altas, factores como la originalidad del contenido y la dedicación podrían ser más relevantes.

Por último, al examinar la evolución de la desviación estándar en el volumen de espectadores, se pueden identificar momentos de polarización de audiencias y momentos de distribución más uniforme. Estas fluctuaciones podrían estar relacionadas con eventos especiales o anuncios importantes por parte de streamers populares.

En resumen, el análisis de los datos de Twitch durante febrero ofrece una visión valiosa sobre las dinámicas de la plataforma, permitiendo identificar tendencias y patrones que podrían resultar útiles para los creadores de contenido y para la propia plataforma en su estrategia de crecimiento y consolidación en el mercado de streaming.

