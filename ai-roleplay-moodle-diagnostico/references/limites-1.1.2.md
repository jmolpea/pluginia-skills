# Límites y valores por defecto: AI Roleplay 1.1.2

Verificados leyendo la versión 1.1.2 (interna 2026111700), revisión del 17-11-2026. Un límite confirmado no demuestra que haya causado un incidente concreto.

## Sesión, intentos y fechas
| Elemento | Valor verificado |
|---|---|
| Duración de la sesión | 5, 10, 15, 20 o 30 minutos. De fábrica 10. El reloj lo lleva el servidor; no hay pausa. |
| Aviso de final | Señal sonora y mensaje «Queda 1 minuto» al faltar 60 segundos. |
| Margen tras el final | 45 segundos: dentro de ese margen aún se aceptan la última respuesta y la despedida. |
| Cierre de sesiones abandonadas | Tarea cada 5 minutos; una sesión abandonada puede tardar hasta unos 5 minutos más en cerrarse. |
| Evaluación en segundo plano | Se encarga con unos 2 minutos de retraso tras el cierre desde el navegador; inmediata si cierra la tarea. |
| Intentos máximos (actividad) | 1, 2, 3, 4, 5, 10 o Ilimitado. De fábrica 2. |
| Intentos máximos (excepción) | 1 a 20, Ilimitado o «Por defecto». Es un total, no un añadido. |
| Qué gasta un intento | Que la sesión llegue a empezar. Un intento creado y no empezado no cuenta. |
| Fechas | «Permitir sesiones desde» y «Cerrar sesiones a partir de», opcionales; el cierre debe ser posterior a la apertura. Solo limitan el inicio de sesiones nuevas. |
| Excepciones | Una por usuario y una por grupo. La de usuario manda; entre varias de grupo se aplica lo más favorable por campo. |
| Avatares | 1, 2 o 3. De fábrica 1. Nombre obligatorio en los que se usan. |

## Texto: tamaños y recortes
| Elemento | Valor verificado |
|---|---|
| Nombre de la actividad | 255 caracteres. |
| Respuesta escrita del alumno | El cuadro de texto admite 2.000 caracteres. |
| Respuesta del alumno en el servidor | Se usan los primeros 5.000 caracteres; se eliminan las etiquetas HTML. Una respuesta vacía se rechaza («Tu respuesta estaba vacía…»). |
| Frase en tiempo real | Cada frase guardada se limita a 5.000 caracteres. |
| Respuesta de un avatar | Pedida de 1 a 3 frases, con un tope fijo y corto de longitud, independiente del ajuste de tokens del sitio. |
| Restricciones de contenido adicionales | Se usan los primeros 2.000 caracteres. |
| Escenario en la evaluación | Primeros 3.000 caracteres del texto sin formato. En la conversación no se ha verificado ningún recorte. |
| Rol del participante en la evaluación | Primeros 1.000 caracteres. |
| Instrucciones de evaluación | Primeros 8.000 caracteres; se eliminan caracteres de control. |
| Conversación enviada al evaluador | Hasta 60.000 caracteres. Si se supera, se descartan los turnos más antiguos y se conserva el final. |
| Reanudación en tiempo real | Al reconectar se recuerdan los últimos 40 turnos, hasta 1.000 caracteres cada uno. |
| Editor del escenario | Sin archivos ni imágenes adjuntas. |

## Evaluación y notas
| Elemento | Valor verificado |
|---|---|
| Rúbrica | Comunicación 30 %, adherencia al rol 25 %, manejo del escenario 25 %, calidad del lenguaje 20 %. Fija. |
| Puntuación por parte | 0 a 100; la nota global se recalcula en el servidor con dos decimales. |
| Calificación máxima | Entero de 1 a 10000. De fábrica 100. Al cambiarla, las notas ya guardadas se convierten a la nueva escala (desde la 1.1.1). |
| Participación mínima | Menos de 20 palabras del alumno: aviso y revisión obligatoria. 0 palabras: nota 0 sin llamar a la IA. |
| Nota manual del profesor | Entre 0 y la calificación máxima. |
| Recalcular evaluación | No disponible en intentos calificados sin conversación guardada. Espera de 5 minutos entre dos recálculos del mismo intento por el mismo profesor; máximo 5 al día (día UTC) por profesor e intento. |
| Espera del alumno | La página consulta el estado cada 5 segundos durante unos 10 minutos; después indica que puede salir y volver. |
| Evaluación atascada | Tras 30 minutos «Evaluándose» puede volver a tomarse. |
| Al libro de calificaciones | La mejor nota entre los intentos publicados. |

## Llamadas a la IA, tiempos y cuotas
| Elemento | Valor verificado |
|---|---|
| Máx. llamadas API por usuario por minuto | De fábrica 10. Mínimo efectivo 1 (0 no lo desactiva). Ventana de un minuto de reloj. |
| Máximo de llamadas por minuto (todo el sitio) | De fábrica 300. Mínimo efectivo 1. Incluye conversación, voz, evaluación, tareas y la prueba de conexión. |
| Llamadas por intervención | Dos con voz de OpenAI o Gemini (respuesta y voz); una con voz del navegador o sin voz. La moderación de OpenAI no consume cuota. |
| Regla de dimensionado del sitio | Unas 5 llamadas por minuto por alumno en sesión simultánea. |
| Tiempo de espera de la solicitud API | De fábrica 120 s. Mínimo efectivo 30 s. Afecta sobre todo a la evaluación. |
| Respuesta de un avatar | Como máximo 45 s de espera (o el ajuste anterior si es menor). |
| Voz de servidor | Como máximo 25 s por frase. |
| Moderación de OpenAI | Como máximo 10 s; si falla, la conversación sigue sin filtrar. |
| Conexión de tiempo real | 20 s para establecerla. Máximo de 6 conexiones por alumno y minuto; por encima, la sesión sigue por turnos. |
| Frases guardadas en tiempo real | Máximo de 120 por alumno y minuto; las que excedan no se guardan. |
| Reintentos | Hasta 3 intentos por llamada ante saturación o error del proveedor, con esperas crecientes y sin superar el tiempo disponible. |
| Máximo de tokens por llamada API | De fábrica 4096. Mínimo efectivo 256. Con modelos que razonan, el plugin eleva el tope (hasta 16.000 en evaluación) aunque el ajuste sea menor. |
| Proceso de evaluación | Hasta 5 minutos cuando lo pide el alumno; hasta 10 al recalcular. |

## Modelos
| Proveedor | Conversación (de fábrica) | Evaluación (de fábrica) | Otros ofrecidos |
|---|---|---|---|
| OpenAI | GPT-6 Sol | GPT-6 Sol | GPT-6 Luna (económico), GPT-6 Astra (premium) |
| Anthropic | Claude Sonnet 5 | Claude Sonnet 5 | Claude Haiku 4.5 (económico), Claude Opus 5.5 (premium), Claude Opus 5 |
| Google Gemini | Gemini 3.8 Flash | Gemini 3.8 Flash | Gemini 3.5 Flash-Lite (económico), Gemini 3.1 Pro (vista previa) |
| DeepSeek | DeepSeek V4.1 Flash | DeepSeek V4 Pro | — |
Modelos de generación anterior (varios GPT-5.x, GPT-4.x, Claude 4.x y Gemini 2.5) no se ofrecen para elegir, pero siguen funcionando en actividades que ya los usan y aparecen como «(generación anterior)». Algunos modelos retirados por DeepSeek y Google se sustituyen automáticamente por su reemplazo.
El proveedor de cada actividad se deduce del modelo que tiene guardado, no del proveedor actual del sitio.
Tiempo real, de fábrica: modelo de OpenAI Realtime «gpt-realtime-2.1-mini» y de Gemini Live «gemini-3.8-live». Nombres de hasta 100 caracteres (letras, números, punto, guion y guion bajo).

## Voces
| Uso | Voces | De fábrica |
|---|---|---|
| OpenAI por turnos | Alloy, Ash, Coral, Echo, Fable, Onyx, Nova, Sage, Shimmer | Avatares 1-3: Onyx, Nova, Echo |
| Gemini por turnos | Aoede, Charon, Fenrir, Kore, Leda, Orus, Puck, Zephyr | Avatares 1-3: Charon, Kore, Puck |
| Navegador o sin voz | «Automática (voz del navegador en el idioma del curso)» | Automática |
| OpenAI Realtime | marin, cedar, alloy, ash, ballad, coral, echo, sage, shimmer, verse | marin |
| Gemini Live | Kore, Puck, Charon, Fenrir, Aoede, Leda, Orus, Zephyr | Kore |
Si la voz guardada en un avatar no existe en el proveedor actual, suena la voz por defecto de ese proveedor (Onyx en OpenAI, Kore en Gemini). En tiempo real se usa la voz del avatar 1 si existe en el motor; si no, la «Voz en tiempo real por defecto».
Anthropic y DeepSeek no ofrecen voces.

## Archivos e imágenes
| Elemento | Valor verificado |
|---|---|
| Imagen personalizada del avatar | Un archivo por avatar; PNG, JPG, JPEG, GIF o WebP; hasta 2 MB. Se muestra fija. |
| Avatares incluidos | Tres, animados (en reposo y hablando). |
| Sin imagen subida con «Imagen personalizada» | Se muestra el avatar incluido que corresponde a su número. |

## Otros
| Elemento | Valor verificado |
|---|---|
| Sal de anonimización | Vacía, o de 32 a 128 caracteres (letras, números, guion, guion bajo). Vacía: se usa un identificador interno del sitio. |
| Navegadores con voz | Chrome, Edge y Safari. Otros, o sin micrófono: respuestas escritas. |
| Coste orientativo que muestra el plugin | Sesión de 10 minutos: 0,05–0,15 USD con modelos recomendados de OpenAI o Anthropic; 0,01–0,04 USD con los económicos, Gemini Flash o DeepSeek Flash. Voz de servidor: unos 0,01 USD por respuesta. Voz del navegador: gratis. Tiempo real: «bastante más por minuto», sin cifra. Son estimaciones, no mediciones. |
| Control de gasto | El plugin no mide ni limita dinero; solo llamadas por minuto, duración e intentos. El tope de gasto se fija en la cuenta del proveedor. |
