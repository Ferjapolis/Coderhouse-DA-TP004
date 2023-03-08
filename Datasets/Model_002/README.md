Proveedor de datos: NASA
Nombre del proyecto de análisis de datos: Conjunto de datos de terremotos

El conjunto de datos de investigación sísmica contiene información valiosa sobre terremotos de todo el mundo. Este conjunto de datos incluye información sobre la ubicación del terremoto, la fecha y hora, la magnitud y la profundidad. Además, se proporciona información sobre el número de personas afectadas y los daños causados.

El conjunto de datos es útil para investigadores que deseen estudiar la actividad sísmica y su impacto en la población y la infraestructura. Además, los expertos en prevención y respuesta ante desastres naturales pueden utilizar este conjunto de datos para comprender mejor cómo se desarrollan los terremotos y cómo pueden mitigar sus efectos.

Este conjunto de datos también es útil para el público en general, ya que proporciona información sobre los terremotos más importantes que han ocurrido en todo el mundo. Además, esta información puede ser utilizada por los gobiernos y organizaciones internacionales para establecer políticas y programas de prevención de desastres.


## Tipos de análisis implementados:

**Descriptivo**: 


### Slide 1: Introducción

### Slide 2: 

### Slide 3: 

### Slide 4: Conclusiones


## Descripcion de campos del dataset:
- Dimensiones del dataset: 
- Período de análisis:1/1/2001 al 1/1/2023
- Formato: CSV

breve descripcion de los datos que podemos encontrar en el dataset.
- title: título nombre dado al terremoto
- magnitud: La magnitud del terremoto
- date_time: fecha y hora
- cdi: la intensidad máxima informada para el rango del evento
- mmi: La intensidad instrumental máxima estimada para el evento
- alerta: El nivel de alerta - "verde", "amarillo", "naranja" y "rojo"
- tsunami: "1" para eventos en regiones oceánicas y "0" en caso contrario
- sig: Un número que describe cuán significativo es el evento. Los números más grandes indican un evento más - significativo. Este valor se determina en función de una serie de factores, que incluyen: magnitud, MMI máximo, informes de sensación e impacto estimado
- net: El ID de un contribuyente de datos. Identifica la red considerada como la fuente de información preferida para este evento.
- nst: El número total de estaciones sísmicas utilizadas para determinar la ubicación del terremoto.
- dmin: Distancia horizontal del epicentro a la estación más cercana
- brecha: La mayor brecha azimutal entre estaciones azimutalmente adyacentes (en grados). En general, cuanto más pequeño es este número, más confiable es la posición horizontal calculada del terremoto. Las ubicaciones de terremotos en las que la brecha azimutal supera los 180 grados suelen tener grandes incertidumbres de ubicación y profundidad
- magType: el método o algoritmo utilizado para calcular la magnitud preferida para el evento
- profundidad: La profundidad donde el terremoto comienza a romperse
- latitud/longitud: sistema de coordenadas mediante el cual se puede determinar y describir la posición o ubicación de cualquier lugar en la superficie terrestre
- ubicación: ubicación dentro del país
- continente: continente del país golpeado por el terremoto
- país: país afectado