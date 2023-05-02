# Ejercicio Individual 2 - De JSON a Gephi: Análisis de interacción en Twitter

## Introducción

Este informe presenta un análisis de la conversación social en Twitter sobre los candidatos a la alcaldía de Barcelona en las elecciones Municipales del 2023. Utilizando los datos obtenidos de la API de Twitter en formato JSON, se ha procesado la información y se ha generado un dataset analizable con Tableau y un grafo para analizar las relaciones de interacción con Gephi.

Los usuarios de los candidatos son los siguientes:

- @bashachanguerra - CUP
- @Adacolau - BComú (no sube contenido)
- @ernestmaragall - ERC
- @jaumecollboni - PSC
- @xaviertrias - Junts
- @annagrauarias - Cs
- @PareraEva - Valents
- @danielsirera - PP
- @gonzalodeoro - Vox (no sube contenido)
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

¿Cuál es el candidato más mencionado?

![cantidad menciones usuario](https://user-images.githubusercontent.com/116378134/235542453-767e88ef-c6db-4c70-a616-5e72eb572ad6.PNG)


¿Qué usuarios son más activos?

![usuarios más activos general](https://user-images.githubusercontent.com/116378134/235542471-8c27aae2-8e2d-4e92-8399-7423d81e4397.PNG)



¿Cuál es la actividad de cada candidato en sus cuentas oficiales? 

![candidatos mas activos](https://user-images.githubusercontent.com/116378134/235545054-5db2ba92-0f54-4853-973a-8c47cb8ab68a.PNG)


¿Qué temas destacan?

![hastags](https://user-images.githubusercontent.com/116378134/235701825-8be856e6-d893-4241-823a-6471f5b32c07.PNG)


![twets candidatos con más mg](https://user-images.githubusercontent.com/116378134/235547173-1af8f803-ef48-4f64-8399-7601ea1eb5ec.PNG)

![Tweet de candidatos con mas rt](https://user-images.githubusercontent.com/116378134/235547455-d1eeea11-709d-4ffa-a7f3-fc161075e441.PNG)



¿Qué temas despiertan más interés entre los usuarios?

![rt](https://user-images.githubusercontent.com/116378134/235543619-37ff62fc-dd1f-47c8-93dd-693afc059331.PNG)

![tw mg](https://user-images.githubusercontent.com/116378134/235543635-93b7c54f-4789-4dfa-b936-c311fbfb2cf9.PNG)

![tweet mas rt](https://user-images.githubusercontent.com/116378134/235547593-2c812611-e9ca-4aca-9c50-80093a0fe011.PNG)


¿En que idiomas se escriben los tweets?

![Idioma tweets](https://user-images.githubusercontent.com/116378134/235542425-9cbd17c0-745d-4b29-836f-152f89ea1ca3.PNG)


### B. Combinado de datos y Gephi


![gephi_final](https://user-images.githubusercontent.com/116378134/235697169-b6263c75-aec8-444a-b7c0-cfab5c56813e.png)


