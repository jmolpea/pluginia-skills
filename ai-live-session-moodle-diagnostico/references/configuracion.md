# Configuración de AI Live Session 1.0.0

Nombres tal como aparecen en pantalla (idioma español). Revisado el 15-11-2026. Detalle visual y simuladores en el manual: https://claude.ai/artifact/J58N9JJybXxofoznCsvqro

## Ajustes del sitio
Dónde: Administración del sitio › Extensiones › Módulos de actividad › AI Live Session. Solo administradores.

| Apartado | Ajuste | Qué hace | Recomendación |
|---|---|---|---|
| Licencia | Clave de licencia | Activa el plugin; debajo muestra el estado | Pedir otra si cambia la dirección del sitio |
| Claves API | Clave API principal de OpenAI | Chat GPT, voces de OpenAI y moderación | Clave propia para Moodle con límite de gasto |
| Claves API | Clave API de Anthropic / de Google Gemini / de DeepSeek | Modelos de cada proveedor (y voces de Gemini) | Solo la del proveedor que se use; DeepSeek trata datos en China |
| Claves API | Clave API secundaria de OpenAI (opcional) | La voz de OpenAI usa esta clave | Solo para separar el gasto de la voz |
| Claves API | Probar la conexión › Ejecutar la prueba | Petición mínima al chat y a la voz | Tras cada cambio de clave o proveedor; no prueba la reserva |
| Proveedor de chat y modelos | Proveedor de chat | Quién conversa, lee entregables y evalúa | OpenAI si no hay preferencia |
| Proveedor de chat y modelos | Modelos de (proveedor) | Qué modelos pueden elegir los docentes | Dejar recomendado y económico para contener el gasto |
| Proveedor de chat y modelos | Proveedor de reserva para las conversaciones | Sustituye al principal si falla en un turno | Activarlo antes de convocatorias grandes; necesita su clave |
| Texto a voz | Proveedor de TTS | Cómo suena el avatar y qué voces se ofrecen | OpenAI o Gemini para voz natural; navegador para coste cero |
| Calificación | Un tutor valida las notas antes de publicarlas (+ Bloqueado) | Valor inicial de las actividades; bloqueado, se impone | Activado; bloquear si es política del centro |
| Seguridad | Activar moderación de contenido de OpenAI | Filtra cada respuesta del alumno (solo con modelos de OpenAI) | Activado |
| Seguridad | Máximo de tokens por llamada API | Tope de longitud de cada respuesta de la IA | No bajarlo |
| Seguridad | Tiempo de espera de la solicitud API (segundos) | Espera máxima; se aplica entero a la evaluación | 120; subir solo si las evaluaciones fallan por tiempo |
| Seguridad | Máx. llamadas API por usuario por minuto | Freno por persona | 30; nunca por debajo de 15 |
| Seguridad | Máximo de llamadas a la API por minuto (todo el sitio) | Freno global | Al menos 8 por cada alumno que pueda conversar a la vez, con margen |

Además: el cron de Moodle debe ejecutarse cada minuto; el sitio debe ir por https; los avisos «Un intento espera validación» y «Tu nota se ha publicado» se ajustan en las preferencias de mensajes.

## Ajustes de la actividad
Dónde: formulario de configuración de la actividad.

| Sección | Ajuste | Qué hace | Recomendación |
|---|---|---|---|
| General | Nombre, Descripción | Identifican la actividad | — |
| General | Pasos de la sesión | Solo vídeo / Vídeo y práctica / Vídeo, práctica y conversación | Decidir antes de abrir; «Solo vídeo» no usa IA |
| Disponibilidad | Apertura, Cierre | Ventana de la sesión | Excepciones para casos individuales |
| Disponibilidad | Intentos permitidos | Repeticiones de práctica y conversación por bloque | 1 en exámenes; cada intento con conversación cuesta |
| Nota y revisión | Un tutor valida la nota antes de que la vea el alumno | La propuesta espera a un tutor | Activado salvo en «Solo vídeo» |
| Ajustes avanzados | Velocidad máxima | Tope de velocidad del vídeo | 1x si importa el tiempo de visionado |
| Ajustes avanzados | Mostrar los subtítulos del vídeo si los tiene | Subtítulos de YouTube o Vimeo | Activado |
| Ajustes avanzados | Tiempo que el reloj puede detenerse | Pausa máxima por cortes del navegador | 5 min en exámenes |
| Ajustes avanzados | Modelo de IA para la conversación / para la evaluación | Modelo de cada tarea | El recomendado |
| Calificación | Puntuación máxima | Escala de la nota | Tipo «Puntuación» |
| Finalización | El alumno debe terminar una conversación | Completa al cerrar el último paso de todos los bloques | Según el curso |

## Diseñador (por bloque)
Dónde: barra «Tutor» de la actividad › Diseñador › Editar.

| Paso | Campos | Claves |
|---|---|---|
| Vídeo y cortes | Título del bloque; Fuente; Enlace al vídeo o Archivo de vídeo; Comprobar el vídeo y leer su duración; Inicio y Final del bloque; Texto del vídeo | Comprobar siempre el vídeo. El final no puede pasar del final real. La transcripción con marcas de tiempo mejora los borradores |
| Preguntas | Tipo; Tiempo del vídeo; Pregunta; Opción, Correcta, Feedback de esta opción; Feedback tras responder; El vídeo solo continúa tras acertar; Puntos; Repasar desde | Una pregunta cada pocos minutos, dentro del fragmento. Solo puntúa el primer intento |
| Práctica | El caso; Preparación máxima y mínima; Qué entrega el alumno; Qué debe mostrar la imagen; Datos corregidos | Misión concreta. Describir la solución para la IA. Varias respuestas válidas con barra vertical |
| Conversación | Nombre y Papel del avatar; Tono; Personalidad y qué debe intentar el avatar; Duración máxima; Aspecto; Imagen del avatar; Voz | Plantillas: Patrocinador, Cliente, Mentor. De 8 a 12 minutos |
| Evaluación | Criterio, Peso, Excelente, Suficiente, Insuficiente; Instrucciones adicionales para la IA evaluadora; Pesos de la nota | Plantillas: Defender un trabajo, Hablar con un cliente. Criterios observables en lo que dice el alumno |

Borradores con IA: preguntas y misión necesitan el «Texto del vídeo»; avatar y rúbrica necesitan la misión. Las preguntas se añaden; lo demás sustituye. Nada cambia hasta pulsar «Usar este borrador».

## Excepciones
Barra «Tutor» › Excepciones. Por usuario o por grupo: Intentos, Apertura, Cierre. La del usuario manda sobre las de sus grupos; entre varios grupos se aplica lo más generoso.

## Recomendaciones de redacción
- Misión: un caso realista y una tarea con resultado comprobable.
- Personalidad del avatar: qué necesita, qué va a cuestionar y cómo reacciona; no repetir la rúbrica.
- Rúbrica: 3 o 4 criterios que se puedan oír en una conversación; cada nivel descrito con conductas.
- Instrucciones para la evaluadora: la solución del caso y lo que no debe penalizar (pronunciación, muletillas).
- No incluir datos personales en los textos de la actividad: se envían al proveedor de IA.
