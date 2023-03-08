Proveedor de datos: Spotify
Nombre del proyecto de análisis de datos: "Análisis de usabilidad de la aplicación de Spotify"

## Tipos de análisis implementados:

**Descriptivo**: Se utilizó el análisis descriptivo para comprender los patrones y tendencias en el consumo de música en Spotify. Se recolectaron datos sobre el número de veces que se escucharon canciones y artistas específicos, la duración de las sesiones de escucha y las listas de reproducción creadas.


### Slide 1: Introducción

Breve introducción a la empresa Spotify y su importancia en la industria de la música en línea.

### Slide 2: Tipos de análisis de consumo
- Análisis de consumo:
- Top 10 temas musicales
- Top 10 artistas
- Top 10 géneros musicales

### Slide 3: Tipos de análisis de sentimiento y tendencias
- Análisis de sentimiento
- Tendencias de sentimiento

### Slide 4: Conclusiones
Resumen de los resultados del proyecto y las conclusiones clave.
Recomendaciones para futuras iniciativas de análisis de datos en Spotify.
Resumen de los resultados del proyecto y las conclusiones clave. Recomendaciones para futuras iniciativas de análisis de datos en Spotify.

Nota: Se debe tener en cuenta que el análisis sentimental puede no ser puntual dado que esta basado en la pista musical y no en registro de estado emocional.

## Descripcion de campos del dataset:
- Dimensiones del dataset: 68144 registros
- Período de análisis: 05/21 al 02/23
- Formato: CSV

breve descripcion de los datos que podemos encontrar en el dataset.
- ts: marca de tiempo de la reproducción de la canción (formato ISO 8601)
- username: nombre de usuario de Spotify
- platform: sistema operativo y versión del dispositivo utilizado para reproducir la canción
- ms_played: duración en milisegundos de la reproducción de la canción
- conn_country: país de la conexión del usuario al servidor de Spotify
- ip_addr_decrypted: dirección IP del usuario, descifrada para proteger la privacidad del usuario
- user_agent_decrypted: información sobre el agente de usuario del dispositivo utilizado para reproducir la canción, descifrada para proteger la privacidad del usuario
- master_metadata_track_name: nombre de la canción reproducida
- master_metadata_album_artist_name: nombre del artista del álbum de la canción reproducida
- master_metadata_album_album_name: nombre del álbum de la canción reproducida
- spotify_track_uri: URI de la canción reproducida en Spotify
- episode_name: nombre del episodio, en caso de que la reproducción fuera un episodio de podcast
- episode_show_name: nombre del programa de podcast, en caso de que la reproducción fuera un episodio de podcast
- spotify_episode_uri: URI del episodio de podcast reproducido en Spotify, en caso de que la reproducción fuera un episodio de podcast
- reason_start: razón por la cual se inició la reproducción de la canción (por ejemplo, "appload" si se inició al abrir la aplicación de Spotify)
- reason_end: razón por la cual se detuvo la reproducción de la canción (por ejemplo, "trackdone" si se detuvo al finalizar la canción)
- shuffle: indicador booleano que muestra si la reproducción estaba en modo aleatorio o no
- skipped: indicador booleano que muestra si la canción fue saltada o no
- offline: indicador booleano que muestra si la reproducción fue en modo sin conexión o no
- offline_timestamp: marca de tiempo en milisegundos de la última vez que se sincronizó la canción en modo sin conexión
- incognito_mode: indicador booleano que muestra si el usuario estaba en modo incógnito durante la reproducción de la canción
- Es importante tener en cuenta que la estructura de metadatos puede variar según los objetivos específicos del proyecto.- 
