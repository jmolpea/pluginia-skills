# Configuración de RSMAX AI Tutor 1.8.1: todos los ajustes

Nombres tal como se ven en pantalla en español. Valores de fábrica verificados el 23-11-2026.
Manual público con explicaciones, maquetas y simuladores: https://claude.ai/artifact/FsE6HtPSgw77e3w7uVcKsk
Para el diseño de prompts y rúbricas, ver configuracion-pedagogica.md.

## Ajustes del sitio
Dónde: Administración del sitio › Extensiones › Extensiones locales › AI Tutor. Solo administradores. Una sola página, con estos apartados: Manual de configuración (enlace), Licencia, Configuración del proveedor de IA, Transcripción de audio, Usuario AI Tutor y Límites de peticiones.

| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Clave de licencia | Vacía (15 días de prueba) | Activa la corrección con IA. Ligada a la dirección exacta del sitio; se valida sin conexión. Debajo se muestra el estado. | Pedir clave nueva si cambia la dirección del sitio. Las de preproducción se emiten sin coste. |
| Proveedor de IA | OpenAI | Empresa que corrige: OpenAI, Anthropic (Claude), Google Gemini o DeepSeek. | DeepSeek no analiza imágenes. Al cambiar, sustituir la clave y revisar el modelo. |
| Clave de API | Vacía | Clave del proveedor elegido. Sin ella no se corrige. | Clave exclusiva para Moodle, con facturación activa y tope de gasto en la cuenta del proveedor. |
| Identificador de organización de OpenAI | Vacío | Solo OpenAI: a qué organización de la cuenta se carga el consumo. | Dejar vacío salvo cuentas con varias organizaciones. |
| Modelo de OpenAI | GPT-5.6 Luna | Modelo usado cuando el proveedor es OpenAI. Desde 1.8.1 incluye los GPT-6. | Cambiar solo por calidad, coste o lentitud. |
| Modelo de Anthropic | Claude Sonnet 4.6 | Modelo usado con Anthropic. Desde 1.8.1 incluye los Claude 5.5. | El formato de respuesta es algo menos estricto: revisar los primeros borradores. |
| Modelo de Gemini | Gemini 2.5 Flash | Modelo usado con Gemini. | Activar la facturación; las claves gratuitas tienen cupos muy bajos. |
| Modelo de DeepSeek | DeepSeek Chat | Modelo usado con DeepSeek. | Reasoner es más lento. |
| Identificador de modelo personalizado | Vacío | Nombre exacto de un modelo; si tiene algo, manda sobre todos los desplegables. | Usar solo cuando el proveedor retira o estrena un modelo. Vaciarlo al cambiar de proveedor. |
| Endpoint de la API (solo OpenAI) | La dirección oficial de OpenAI | Dirección a la que se envían las peticiones con OpenAI. Se ignora con los demás. | Cambiar solo para un servicio intermedio compatible que indique el equipo técnico. Debe ser https y pública. |
| Activar la transcripción de audio | No | Transcribe audios con OpenAI y corrige el texto. | Solo si hay entregas habladas. Se cobra por minuto de audio. La voz es dato personal. |
| Clave de API para transcripción (OpenAI) | Vacía | Clave de OpenAI solo para transcribir. | Obligatoria si el proveedor de corrección no es OpenAI. |
| Usuario AI Tutor por defecto para todo el sitio | Vacío | Nombre de usuario de la cuenta de reserva que firma cuando el usuario de la tarea ya no es válido. | Crear una cuenta «AI Tutor» y matricularla con rol que pueda calificar en los cursos. |
| Activar el límite de peticiones para todo el sitio | No | Enciende el tope por hora del sitio. | Útil como techo de gasto. |
| Máximo de peticiones por hora (todo el sitio) | 100 | Correcciones por hora de reloj en todo el sitio. | Dimensionar para el pico de una fecha límite. |
| Activar el límite de peticiones por usuario | No | Enciende el tope por hora de cada alumno. | Solo ante reenvíos abusivos. |
| Máximo de peticiones por hora (por usuario) | 10 | Correcciones por hora que puede provocar un alumno. | No bajarlo demasiado si hay varias tareas el mismo día. |
| Pruebas por usuario y día | 20 | Cuántas veces al día puede cada docente pulsar «Analizar prompt» o «Probar corrección». Cada una es una petición de pago. Con 0, sin límite. Está en el apartado «Límites de peticiones». | Subirlo si el profesorado prepara muchas tareas el mismo día; bajarlo para acotar el gasto en pruebas. |

Avisos de la página: enlace al manual al principio; estado de la licencia bajo la clave; aviso amarillo «Migración desde la versión anterior» si el plugin antiguo sigue instalado.
Al cambiar de proveedor hay que cambiar tres cosas: proveedor, clave y, si se usó, el identificador de modelo personalizado.

## Ajustes de la tarea de Moodle de los que depende AI Tutor
Dónde: Tarea › Configuración. No son del plugin, pero condicionan su comportamiento.

| Ajuste de Moodle | Efecto sobre AI Tutor |
|---|---|
| Flujo de trabajo de calificación | Imprescindible para que existan borradores. Sin él, todo lo que corrige la IA lo ve el alumno al momento. La página de AI Tutor de la tarea avisa cuando no está activado. |
| Tipo de retroalimentación «Comentarios de retroalimentación» | Imprescindible para que se guarden el texto de la IA y las notas de entrega ilegible o no calificada. |
| Tipos de entrega y tipos de archivo aceptados | Conviene limitarlos a los formatos que el plugin lee. |
| Calificación: puntos, escala o ninguna | Determina si la IA propone número, valor de escala o solo comentario. |
| Método de calificación avanzada: rúbrica o guía | Se usa solo si en la página de AI Tutor se elige usarla. Debe estar definida y lista. |
| Intentos adicionales | Determinan qué es una reentrega para el plugin: un intento nuevo. |
| Requerir que los alumnos pulsen el botón de envío | Si está desactivado, cada guardado de la entrega provoca una corrección y gasta cuota del alumno. |
| Entregas en grupo | La nota se aplica a todo el grupo. |
| Descripción | Solo llegan a la IA sus primeros 8.000 caracteres de texto. |

## Ajustes de AI Tutor en la tarea
Dónde: Tarea › Más › AI Tutor («Configuración de AI Tutor»). Profesor con edición y gestor. Mientras la primera casilla está sin marcar, el resto no se ve. Al principio hay un enlace al manual y, si la tarea no usa el flujo de trabajo de calificación, un aviso.

| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Activar AI Tutor en esta tarea | No | Interruptor de la tarea. Bloqueado si la licencia no es válida. | Activar antes de que empiecen a entregar; lo anterior no se corrige. |
| Usuario que responde como IA | Obligatorio al activar | Cuenta a cuyo nombre se guarda la nota. Lista: matriculados en el curso que pueden calificar. Si deja de poder calificar, las entregas no se envían a la IA y quedan con una nota. | Usar una cuenta específica «AI Tutor», no la del docente. |
| Prompt para AI Tutor | Plantilla completa | Instrucciones de corrección. Máximo 16.000 caracteres. Vacío = plantilla. | Añadir lo propio de la materia; no repetir formato, idioma, enunciado ni rúbrica. Sin datos personales. |
| Método de calificación | Solo retroalimentación y calificación (sin rúbrica) | La otra opción: «Usar la rúbrica o guía de evaluación de la tarea (si está configurada)». | Usar la rúbrica siempre que exista y sus nombres sean inequívocos. |
| Retrasar la respuesta de la IA 1 hora | No | Espera mínima de una hora antes de corregir. | Para que la respuesta no parezca instantánea. |
| Publicar la calificación directamente | No | Publica las primeras entregas con confianza suficiente y nota limpia. | Empezar sin marcar; activarla tras revisar las primeras tandas. Requiere el flujo de trabajo de calificación. |
| Publicar también las reentregas | No | Las reentregas siguen las reglas de una primera entrega. Solo visible y efectiva con la anterior marcada. | Para cursos autoformativos sin tutor. |
| Umbral mínimo de confianza | 7 | Por debajo, la corrección queda para revisión con aviso. | 8 o 9 si se publica sin revisión. No bajarlo para ocultar borradores. |
| Número máximo de calificaciones por alumno | 3 | Tope de correcciones por alumno en la tarea. No se reinicia. | Intentos permitidos más uno. Subirlo si un alumno lo agota. |
| Texto de aviso | «Esta retroalimentación ha sido generada por un asistente de IA. Tu profesor la revisará antes de que sea tu calificación definitiva.» | Se añade al final de la retroalimentación. Vacío = sin aviso. | Cambiarlo si nadie va a revisar: el texto de fábrica promete revisión. |
| Límite diario de peticiones para esta tarea | 50 | Correcciones al día en la tarea. | Ponerlo por encima de los alumnos que pueden entregar el mismo día. |

Herramientas de la misma página, que no son ajustes y no guardan nada (desde 1.8.0):

| Elemento | Dónde | Qué hace |
|---|---|---|
| Revisión del prompt › «Analizar prompt» | Bajo el campo del prompt | La IA valora si el prompt encaja con la descripción, la escala y la rúbrica de la tarea, y propone uno reescrito. |
| «Usar este prompt» | Bajo el resultado del análisis | Copia el prompt propuesto al campo. No se guarda hasta «Guardar cambios». |
| Probar el tutor con una entrega de ejemplo | Sección al final de la página | Campos «Texto de ejemplo» y «Archivos de ejemplo» (hasta 5) y botón «Probar corrección». Muestra la nota, la rúbrica, la confianza, los avisos, qué pasaría con una entrega real y la retroalimentación. |

Junto a los botones se indica cuántas pruebas le quedan hoy al docente. Las dos herramientas usan lo que hay escrito en la página, guardado o no. Si falta la licencia o la clave de API del sitio, aparece un aviso de «no disponible» en su lugar.

Mensajes del formulario: «La configuración de AI Tutor se ha guardado correctamente»; errores si falta usuario, o si alguno de los dos topes es menor que 1.

## Combinaciones habituales
| Situación | Configuración |
|---|---|
| Preparar una tarea nueva | Marcar la casilla de activar, escribir el prompt, «Analizar prompt», probar tres ejemplos (bueno, flojo y fuera de tema) con «Probar corrección» y guardar. |
| El docente revisa todo | Flujo de trabajo activado; publicar directamente sin marcar. Es la de fábrica. |
| El docente revisa solo lo dudoso | Publicar directamente marcado; reentregas sin marcar; umbral 8; adaptar el texto de aviso. |
| Curso sin tutor | Publicar directamente y reentregas marcados; umbral 8; intentos adicionales en la tarea; máximo por alumno acorde; texto de aviso sin promesa de revisión. Alguien debe mirar periódicamente los borradores. |
| Fotos o escaneados | Proveedor distinto de DeepSeek; JPG o PNG de menos de 4 MB; como mucho 5 por entrega. |
| Entregas habladas | Transcripción activada con clave de OpenAI; audios de menos de 25 MB. |
| Fecha límite masiva | Límite diario de la tarea y tope por hora del sitio por encima del número de alumnos. |

## Lo que no existe en 1.8.1
No hay ajustes por curso ni por categoría, ni configuración por defecto para tareas nuevas.
No hay reintentos automáticos ni botón para volver a corregir una entrega, ni para corregir las anteriores a la activación, ni para reiniciar contadores.
No hay panel de uso, de coste ni de historial; solo el evento en los registros de Moodle. Las pruebas y los análisis del prompt no se guardan ni se pueden consultar después.
No se puede probar una entrega ya hecha por un alumno ni comparar varios prompts a la vez: la prueba usa un ejemplo aportado en el momento.
No hay ajustes de temperatura, de longitud de respuesta, de tiempo de espera ni de duración del retraso.
No funciona con cuestionarios, foros, talleres ni otras actividades: solo con la actividad Tarea.
No es un chat: el alumno no puede conversar con la IA.
