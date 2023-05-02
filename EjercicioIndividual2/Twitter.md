# Ejercicio Individual 2 - De JSON a Gephi: Análisis de interacción en Twitter sobre candidatos a la alcaldía de Barcelona

## Introducción

Este informe presenta un análisis de la conversación en Twitter sobre los candidatos a la alcaldía de Barcelona en las elecciones municipales de 2023. Utilizando datos obtenidos de la API de Twitter en formato JSON, se ha procesado la información y se ha generado un dataset analizable con Tableau y un grafo para analizar las relaciones de interacción con Gephi.

Los usuarios de los candidatos son los siguientes:

- @bashachanguerra - CUP
- @Adacolau - BComú (no sube contenido)
- @ernestmaragall - ERC
- @jaumecollboni - PSC
- @xaviertrias - Junts
- @annagrauarias - Cs
- @PareraEva - Valents
- @danielsirera - PP
- @gonzalodeoro - Vox (no sube contenido) - (Incluido en los gráficos aunque no se extrajeron datos de este)
- @VosselerDaniel - Barcelona Ets Tu
- @ivanguijarrov - pacma
- @RogerMallola - PRIMÀRIES 

## Procesamiento de datos

1. Análisis y comprensión de la estructura del archivo .json.

 **data**: Contiene una lista de tweets, donde cada tweet es un objeto con información relevante, como el ID del autor, el texto del tweet, la fecha y hora de creación, y las entidades (menciones, hashtags, URLs, etc.).

**includes**: Contiene información adicional relacionada con los tweets, como detalles sobre los usuarios, los tweets citados y el contenido multimedia. Esta sección se divide en varias subsecciones:

   - **users**: Lista de objetos de usuario con información sobre el ID, el nombre y las métricas públicas (seguidores, seguidos, recuento de tweets y recuento de listas) de cada usuario.
   - **tweets**: Lista de objetos de tweets citados con información adicional, como el autor y las entidades.
   - **media**: Lista de objetos de medios con información sobre el tipo de contenido multimedia (foto, video, etc.) y su URL.
   - **places**: Lista de objetos de lugares con detalles sobre la ubicación geográfica, como el nombre completo y el ID del lugar.

**meta**: Contiene metadatos sobre la respuesta JSON, como el recuento de resultados, el ID del tweet más antiguo y más reciente, y un token para obtener la siguiente página de resultados.

2. Extracción de datos relevantes para el análisis.

### A. Extracción de dataset y Tableau

#### ¿Cuál es el candidato más mencionado?

![cantidad menciones usuario](https://user-images.githubusercontent.com/116378134/235542453-767e88ef-c6db-4c70-a616-5e72eb572ad6.PNG)

En este primer gráfico, se ha realizado un filtro para analizar a los usuarios que han mencionado a los diferentes candidatos en twitter. El objetivo de este análisis es poder determinar cuál ha sido la relevancia de cada uno de los candidatos en las conversaciones que se han generado.

Tras el análisis de los datos, a destacar los 3 primeras puestos:

Se puede observar que Ada Colau es el candidato que ha sido mencionado con mayor frecuencia por los usuarios de Twitter. Este hecho puede deberse al hecho de que Colau es una figura muy conocida en el ámbito político y social, gracias a su trayectoria como activista y su labor al frente del Ayuntamiento de Barcelona.

En segundo lugar, encontramos a Parera Eva, que también ha sido mencionada con una frecuencia bastante elevada. Este hecho puede deberse a la labor que ha realizado en el ámbito político y a su presencia en diferentes medios de comunicación.

Por último, Daniel Sirera es el candidato que ha sido mencionado con menor frecuencia. Este hecho puede deberse a que no cuenta con una presencia tan destacada en el ámbito político y social como los otros dos candidatos mencionados anteriormente.

Destacar por otro lado el candidato menos mencionado es gonzalodeoro.

Es importante tener en cuenta que los candidatos tienen diferentes perfiles y trayectorias políticas, y que su presencia en las redes sociales puede variar en función de diversos factores, como la estrategia de comunicación, la interacción con los usuarios, la viralidad de los contenidos, entre otros.

#### Candidatos con más seguidores (de los cuales publican)

![seguidores](https://user-images.githubusercontent.com/116378134/235714175-20e2d506-cbb2-4a4f-88c9-52f09ef253b6.PNG)

Observamos que el usuario con más seguidores es PareraEva. Sin embargo, es interesante notar que danielsirera, a pesar de tener menos seguidores, cuenta con más "me gusta" en sus publicaciones. Por otro lado, bashachanguerra se encuentra en la última posición en cuanto a seguidores y "me gusta"

#### ¿Qué usuarios son más activos?

![usuarios más activos general](https://user-images.githubusercontent.com/116378134/235542471-8c27aae2-8e2d-4e92-8399-7423d81e4397.PNG)

Es interesante destacar que, en el análisis de los usuarios con más tweets relacionados con los candidatos, se han encontrado cuentas que se dedican a compartir noticias y medios de comunicación, lo que puede indicar la importancia que tienen los medios en la difusión de información y en la opinión pública.

A su vez, es importante tener en cuenta que también se han encontrado cuentas extremistas en ambos sentidos, lo que puede indicar la polarización que existe en la sociedad en torno a ciertos temas políticos y sociales.

Por último, es relevante mencionar que también se han encontrado cuentas de partidos políticos, como CUPBarcelona, Valents_bcn, EnComu_Podem, lo que puede indicar la importancia que tienen las redes sociales en la estrategia de comunicación política y en la difusión de información por parte de los partidos políticos y sus programas electorales.

##### ¿Cuál es la actividad de cada candidato en sus cuentas oficiales? 

![candidatos mas activos](https://user-images.githubusercontent.com/116378134/235545054-5db2ba92-0f54-4853-973a-8c47cb8ab68a.PNG)

Es interesante destacar que, en el análisis de la actividad de los candidatos en Twitter, se observa que no todos ellos publican tweets con la misma frecuencia y regularidad. Por ejemplo, Ada Colau lleva sin publicar desde 2021, lo que puede indicar que ha decidido centrar su estrategia de comunicación en otros medios o plataformas.

Entre los candidatos que sí publican tweets, se observa que PareraEva es la candidata con más tweets publicados, seguido de danielsirera y bashachanguerra. Es importante tener en cuenta que el número de tweets publicados no siempre refleja la calidad o la relevancia de la información que se comparte, y que la estrategia de comunicación puede variar en función de las preferencias y objetivos de cada candidato.

Por último, se ha observa que Xavier Trias es el candidato que menos publica.

#### ¿Qué temas destacan?

![hastags](https://user-images.githubusercontent.com/116378134/235701825-8be856e6-d893-4241-823a-6471f5b32c07.PNG)

En el análisis de los hashtags más utilizados en las publicaciones relacionadas con los candidatos, se ha observado que existen algunos términos que se repiten con mayor frecuencia. Entre los hashtags más utilizados se encuentran "URGENTE", "Barcelona", "Colau", "ÚLTIMAHORA", "BCN", "Opinión", "loharemos" y "valents".

Estos hashtags pueden reflejar la importancia que tienen ciertos temas en la opinión pública y en la discusión política en la ciudad de Barcelona, como la urgencia de ciertas medidas, la situación actual de la ciudad, la figura de Ada Colau, las noticias de última hora, la opinión de los ciudadanos, entre otros.

![twets candidatos con más mg](https://user-images.githubusercontent.com/116378134/235547173-1af8f803-ef48-4f64-8399-7601ea1eb5ec.PNG)

En cuanto a los tweets con más "me gusta", vemos que son los de danielsirera, el segundo candidato que publica más tweets. Destacar que estos son un poco radicales y critican a la izquierda.

Seguidamente encontramos los tweets de annagrauarias, destacar que también critican a Ada Colau.

![Tweet de candidatos con mas rt](https://user-images.githubusercontent.com/116378134/235547455-d1eeea11-709d-4ffa-a7f3-fc161075e441.PNG)

Por otro lado, se observa que PareraEva es la candidata con más retweets. Sin embargo, es importante destacar que algunos de sus tweets más virales son bastante radicales. Por otro lado, los demás candidatos presentan una estrategia similar al criticar a su competencia y utilizar el radicalismo para destacar en Twitter. En cuanto a los retweets, los demás candidatos están bastante igualados. Estos resultados pueden ser útiles para que los candidatos revisen su estrategia de comunicación en redes sociales y ajusten su mensaje para llegar a un público más amplio.

#### ¿Qué temas despiertan más interés entre los usuarios?

![rt](https://user-images.githubusercontent.com/116378134/235543619-37ff62fc-dd1f-47c8-93dd-693afc059331.PNG)

![tw mg](https://user-images.githubusercontent.com/116378134/235543635-93b7c54f-4789-4dfa-b936-c311fbfb2cf9.PNG)

Es importante resaltar que el tweet con más "me gusta" y retweets es el mismo y pertenece a WillyTolerdo, una cuenta paródica de Willy Toledo. Su contenido se centra en criticar a la izquierda mediante el uso de la ironía, lo cual parece estar atrayendo a un gran número de audiencia.

Este tweet en particular comenta una frase de Yolanda Díaz dirigida a Ada Colau (se incluye el tweet a continuación).

El contenido de este tweet se repite en otros con muchos "me gusta" y retweets, que también critican a Ada Colau y la situación en la que se encuentra Barcelona bajo su mandato.

Cabe destacar que también encontramos tweets en inglés y alemán que critican a Ada Colau.

![tweet mas rt](https://user-images.githubusercontent.com/116378134/235547593-2c812611-e9ca-4aca-9c50-80093a0fe011.PNG)

#### ¿En qué idiomas se escriben los tweets?

![langg](https://user-images.githubusercontent.com/116378134/235736683-7f040118-894d-40c5-9ae2-282c359be5d8.PNG)

Podemos observar que la mayoría de los tweets están escritos en español, seguido del catalán, que es la segunda lengua oficial de Barcelona. Tal como mencioné anteriormente, también encontramos tweets en otros idiomas como inglés, alemán, neerlandés, portugués, francés, entre otros.

Cabe añadir que el cuarto idioma que aparece como 'zxx' corresponde a los tweets cuyo idioma no ha sido reconocido por la API.

### B. Combinación de datos y Gephi

El siguiente grafo se ha creado a partir de las menciones entre usuarios en Twitter. Debido a la gran cantidad de usuarios, se ha aplicado un filtro utilizando el parámetro Ego, centrándose en la cuenta OnVasBarcelona y estableciendo un nivel de profundidad de 2. Esta cuenta se opone a Ada Colau, por lo que es natural que las cuentas más cercanas a ella tengan una mayor relación entre sí, mientras que las más alejadas tengan menos.

Junto a OnVasBarcelona, encontramos la cuenta de AdaColau. Esto es esperable, ya que en la mayoría de sus tweets probablemente esté mencionando a su propio usuario.

En la parte superior derecha del gráfico, encontramos al usuario previamente mencionado, 'WillyTolerdo', que es el más grande debido a la gran cantidad de menciones que ha recibido a raíz de su tweet que ha sido ampliamente retuiteado. Junto a él, encontramos otras cuentas de temática humorística como FroilLannister o ToroenReposo.

Dirigiéndonos hacia el centro del gráfico, nos encontramos con cuentas de partidos políticos como la CUP, PareraEva, Esquerra, entre otros.

Más abajo, localizamos otra cuenta que muestra cierta oposición a Colau, pero aparentemente con un enfoque más serio: 'Educardo54812683'.


![gephi_final](https://user-images.githubusercontent.com/116378134/235697169-b6263c75-aec8-444a-b7c0-cfab5c56813e.png)

## Conclusiones

En base al análisis de la interacción en Twitter sobre los candidatos a la alcaldía de Barcelona, se puede concluir que Ada Colau es la candidata más mencionada en la plataforma, lo cual puede deberse a su prominencia en la política y su trayectoria como activista. A pesar de tener menos seguidores, Daniel Sirera obtiene más "me gusta" en sus publicaciones, lo que indica una mayor interacción y compromiso de su audiencia. 

El estudio también revela la importancia de los medios de comunicación y las cuentas extremistas en la difusión de información y la polarización de la opinión pública en torno a temas políticos y sociales. Además, se observa que los candidatos tienen diferentes niveles de actividad en Twitter, lo que puede reflejar distintas estrategias de comunicación y enfoques en la plataforma.

Los temas de interés en la opinión pública se reflejan en los hashtags más utilizados, mencionando la urgencia de ciertas medidas, la situación actual de Barcelona y la figura de Ada Colau, entre otros. Los tweets que generan más interés suelen ser aquellos que critican a Colau y la situación en Barcelona bajo su mandato. 

Por último, aunque la mayoría de los tweets están escritos en español y catalán, también se encuentran tweets en otros idiomas como inglés, alemán y francés. Esto demuestra la diversidad de la conversación y la presencia de usuarios internacionales interesados en las elecciones municipales de Barcelona.

Teniendo en cuenta el análisis realizado, se puede agregar que el uso de las redes sociales, en particular Twitter, es un aspecto fundamental en la comunicación política y en la difusión de información sobre los candidatos y sus programas electorales. La plataforma permite a los candidatos interactuar con la ciudadanía y presentar sus propuestas, pero también puede ser un espacio para la crítica y la polarización.

Añadir que la presencia de cuentas humorísticas y paródicas, como la de WillyTolerdo, juega un papel relevante en la conversación en Twitter. Estas cuentas pueden atraer la atención de la audiencia y generar discusiones en torno a temas políticos y sociales, utilizando el humor y la ironía como herramientas para divulgar mensajes críticos.
