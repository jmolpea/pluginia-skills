# Configuración de Forumia (versión 1.8.4)

Nombres tal como aparecen en Moodle en español. Revisado el 23-11-2026. Manual con ejemplos y simuladores: https://claude.ai/artifact/Qg9adYg7HtbnatxfFCi825

## Ajustes del sitio
Dónde: Administración del sitio › Extensiones › Extensiones locales › Forumia - Asistente IA para foros. Solo administradores. Una sola página, con un enlace al manual de configuración al principio.

| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Clave de licencia | Vacía (15 días de prueba) | Activa el plugin. Ligada a la dirección exacta del sitio. Debajo se ve el estado. | Introducirla al recibirla. Pedir otra si cambia la dirección del sitio. Una clave errónea desactiva el asistente aunque quede prueba. |
| Deshabilitado en todo el sitio | No | Parada general. La marca el propio plugin cuando el proveedor rechaza la clave de API; mientras está marcada no se hace ninguna petición en ningún foro. Se desmarca sola al guardar una clave, un proveedor o un endpoint distintos. | Tras un aviso de clave rechazada: guardar la clave correcta o, si es la misma, desmarcarla y guardar. También sirve para parar todo el sitio a mano. |
| Proveedor de IA | OpenAI | Empresa que genera respuestas, resúmenes y evaluaciones en todo el sitio. | Elegir el proveedor con el que la institución tenga acuerdo de tratamiento de datos. |
| Clave de API de OpenAI / Anthropic / Google Gemini / DeepSeek | Vacías | Credencial del proveedor. Solo se muestra la del proveedor elegido; las demás se conservan. | Crear una clave solo para Moodle y poner un tope de gasto en la web del proveedor. |
| Modelo de OpenAI | GPT-5.6 Luna | Modelo usado con OpenAI. Lista cerrada; desde 1.8.4 incluye los GPT-6. | Mantener, o bajar a uno mini o nano para gastar menos. |
| Endpoint de API | Dirección oficial de OpenAI | Dirección a la que se envían las consultas con OpenAI. | No tocar salvo que se use Azure OpenAI. Otra dirección no permitida hace que el asistente deje de responder. |
| Modelo de Anthropic | Claude Haiku 4.5 | Modelo usado con Anthropic. Desde 1.8.4 la lista incluye los Claude 5.5. | Mantener. |
| Modelo de Gemini | Gemini 2.5 Flash | Modelo usado con Gemini. Flash y Pro razonan antes de responder y tardan más. | Para el más económico, elegir Flash-Lite a mano. |
| Modelo de DeepSeek | DeepSeek Chat | Modelo usado con DeepSeek. | Mantener. |
| Activar límite de frecuencia de todo el sitio | No | Enciende el tope diario global de peticiones. | Activarlo cuando haya varios foros con asistente. |
| Máximo de peticiones por día (todo el sitio) | 100 | Valor del tope global. También es el valor que se propone como límite al configurar un foro nuevo. | Estimar respuestas diarias de todos los foros más un margen. |
| Usuario IA predeterminado del sitio | Vacío | Nombre de usuario o identificador de la cuenta con la que publica el asistente y cuenta de reserva. | Crear un usuario dedicado, con nombre que deje claro que es una IA. Sin él, los docentes no pueden habilitar el asistente. |

Otros puntos del sitio:
- Varias cuentas de asistente: asignar a cada una, a nivel de sistema, el permiso «Ser designado como cuenta que publica las respuestas de IA de Forumia».
- Horarios: en Administración del sitio › Servidor › Tareas › Tareas programadas se cambian «Forumia – Resumen diario», «Forumia – Calificación por IA» y «Forumia – Comprobación de inactividad». La hora del resumen diario es la de su tarea.
- Notificaciones al administrador: «Forumia: el proveedor de IA ha rechazado la clave de API» y «Forumia: el asistente se ha desactivado en un foro».

## Permisos
| Permiso (nombre en pantalla) | Quién lo tiene de fábrica | Para qué |
|---|---|---|
| Gestionar la configuración del Asistente IA de un foro | Profesor con edición, gestor (a nivel de curso) | Ver «Asistente IA» en el foro y guardar su configuración. |
| Ser designado como cuenta que publica las respuestas de IA de Forumia | Nadie | Convierte una cuenta en cuenta del asistente si se asigna a nivel de sistema. |
| Calificar en el foro (permiso propio de Moodle) | Profesores y gestores | Página de sugerencias y posibilidad de activar el modo Automática. |

## Configuración de cada foro
Dónde: dentro del foro, menú de ajustes del foro › «Asistente IA». Página «Configuración del Asistente IA». Botón «Guardar configuración IA». Vale solo para ese foro.

| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Habilitar el Asistente IA en este foro | No | Interruptor del foro; también condiciona reactivación y calificación. | Activarlo solo tras elegir cuenta y revisar límites. |
| Usuario de respuestas IA | Sin elegir | Cuenta con la que se publica en este foro. Solo ofrece cuentas designadas. | Obligatorio al habilitar. Si la lista está vacía, debe actuar el administrador. |
| Modo de respuesta | Inmediato | Inmediato: responde a cada mensaje de estudiante. Diario: un resumen al día. | Inmediato en grupos pequeños o cursos sin tutor; Diario en foros muy activos. |
| Retrasar la respuesta IA 1 hora | No | Publica la respuesta una hora después. Solo en modo Inmediato. | Activarlo para dejar que respondan antes compañeros o docente. |
| Prompt para el modo inmediato | Texto de fábrica (docente ayudante, 80 a 150 palabras) | Instrucciones para responder a cada estudiante. | Añadir tema del curso y tono. No indicar idioma. Vacío = texto de fábrica. |
| Prompt para el modo diario | Texto de fábrica (resumen de 150 a 250 palabras) | Instrucciones del resumen. | Solo si se quiere otra estructura. |
| Texto de aviso legal | «Revísalo con criterio y consulta a tu docente ante cualquier duda.» | Texto opcional tras el aviso fijo de IA. | Adaptarlo a la política del centro; admite formato sencillo. |
| Límite diario de peticiones para este foro | Máximo del sitio (100) | Tope diario del foro para todas las funciones. | Estudiantes activos más margen para evaluaciones y reactivaciones. |
| Calificación por IA | Desactivada | Desactivada, Sugerir o Automática. | Sugerir con docente; Automática en autoformación. |
| Horas antes de evaluar a un estudiante | 12 | Espera desde el primer mensaje del estudiante. De 1 a 720. | Igualarlo a la duración de la actividad; no hay segunda evaluación. |
| Criterios de calificación (IA) | Pertinencia 30 %, Fundamentación 30 %, Profundidad y aporte propio 25 %, Interacción y claridad 15 %, con tramos de referencia | Criterios que aplica la IA. | Usar los de la guía docente, con pesos y descriptores observables. |
| Límite diario de peticiones por usuario | 1 | Respuestas diarias por estudiante en el foro. 0 = sin límite. | Subir a 2 o 3 si se quiere diálogo; mantener 1 en foros grandes. |
| Reactivar debates inactivos | No | Publica en debates parados. | Activar con fecha límite. |
| Días de inactividad antes de publicar | 7 | Días sin mensajes de personas. | 3 o 4 en cursos intensivos. |
| Días entre publicaciones de reactivación | 7 | Separación mínima entre intervenciones en el mismo debate. | Valor alto para que insista poco. |
| Fecha límite de reactivación | Desactivada | Fecha tras la cual no reactiva. Sin ella usa la fecha límite del foro. | Ponerla siempre que el curso termine. |
| Prompt para respuestas de reactivación | Texto de fábrica (60 a 120 palabras, una pregunta abierta) | Instrucciones de la reactivación. | Normalmente no tocar. |

Notas de formulario:
- Los cuadros de prompt vienen rellenos con el texto de fábrica en el idioma de quien abre el formulario por primera vez; al guardar, ese texto queda fijado en el foro.
- Las etiquetas HTML se eliminan al guardar los prompts y el aviso.
- Los campos de calificación y de reactivación solo se muestran al activar cada función.
- Mensajes de validación visibles: falta de cuenta al habilitar; cuenta no designada; límite del foro menor que 1; límite por usuario negativo; días de inactividad o de repetición menores que 1; horas fuera de 1 a 720; foro sin calificación del foro completo en puntos; falta de permiso para calificar al elegir Automática.

## Ajustes del propio foro de Moodle que influyen
- Descripción del foro: es el único contexto del curso que recibe la IA (primeros 500 caracteres). Poner ahí la consigna.
- Calificación del foro completo: tipo Puntuación y calificación simple directa, imprescindible para la calificación por IA.
- Fecha límite de entrega del foro: detiene la reactivación si no hay fecha propia.
- Roles: solo se responde y evalúa a quien está matriculado y no tiene en el curso un rol de profesorado o gestión, sea estándar o creado a partir de uno estándar.

## Página «Forumia: sugerencias de calificación por IA»
Columnas: Estudiante, Publicaciones evaluadas, Calificación sugerida, Justificación de la IA, Calificación actual, Acciones. Botones: Aceptar, Descartar, Aceptar todas las sugerencias. En modo Automática solo muestra lo que no pudo aplicarse.
