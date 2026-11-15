# Protocolo de casos

## Ficha mínima
Pedir según la consulta, nunca todo de golpe:
- Versión de Moodle y del plugin; estado de la licencia que muestra la página de ajustes.
- Proveedor de chat, proveedor de TTS, proveedor de reserva y modelos de la actividad.
- «Pasos de la sesión», número de bloques, intentos permitidos, fechas y si hay excepciones.
- Qué ve exactamente el alumno (mensaje literal) y en qué pantalla: portada, vídeo, práctica, conversación o resultado.
- Código ALS- completo, si lo hay, y la fila correspondiente de «Problemas técnicos».
- Estado del alumno en «Progreso de los alumnos» y, en la revisión, estado del intento y avisos.
- Navegador y dispositivo del alumno; si el sitio va por https.
- Para dudas de nota: rúbrica y pesos del bloque, puntuación por criterio, transcripción anonimizada y avisos.
No pedir claves API, clave de licencia ni acceso de administrador. Pedir anonimización antes de recibir conversaciones.

## Descifrar un código ALS-
Formato: ALS-, letra del momento, letra del motivo, estado HTTP si lo hubo, guion y referencia.
Momento: S al empezar la conversación (el reloj no había arrancado); T en un turno; V en la voz del avatar; C detectado por el navegador.
| Motivo | Significado | Primera comprobación |
|---|---|---|
| K | Clave ausente o no válida | «Probar la conexión»; revisar la clave del proveedor que usa el modelo de la actividad |
| Q | Cuota o límite del proveedor | Saldo y límites en la cuenta del proveedor |
| P | Fallo del proveedor | Página de estado del proveedor; proveedor de reserva |
| N | Sin conexión (servidor con proveedor, o alumno con el sitio) | Cortafuegos o proxy del servidor; red del alumno |
| B | Petición rechazada | Modelo retirado o no disponible: elegir otro |
| L | Límite de llamadas del propio sitio | Subir los límites de «Seguridad» |
| R | Respuesta inservible | Reintentar; si persiste, cambiar de modelo |
| A | El navegador no reprodujo el sonido | Volumen, permisos, otro navegador |
| T | La respuesta tardó demasiado en llegar | Red o intermediario que corta peticiones largas |
| X | Error inesperado | Registro de errores del servidor; consulta al mantenedor |
Un código sin referencia final (solo momento C) no estará en «Problemas técnicos»: el navegador no llegó al servidor.

## Árbol síntoma → causas → comprobación
| Síntoma | Causas a considerar | Comprobación |
|---|---|---|
| Aviso de licencia y actividad parada | Evaluación terminada, licencia caducada, dirección del sitio distinta | Estado bajo «Clave de licencia» |
| «Esta sesión todavía no está disponible» | Algún bloque incompleto | Lista «Falta:» del diseñador |
| «Esta sesión todavía no está abierta» o «está cerrada» | Fechas o excepción | Apertura, Cierre y excepciones del alumno o de su grupo |
| El docente en modo prueba no avanza el vídeo fuera de fechas | Versión anterior a la 1.0.2 | Actualizar; mientras tanto, probar dentro de fechas |
| El vídeo vuelve atrás o no avanza | Salto más allá de lo visto, velocidad superior a la permitida, pregunta pendiente | «Velocidad máxima»; preguntas del bloque |
| Nadie completa el vídeo | Final escrito mayor que la duración real; pregunta situada tras el final del fragmento (bloques guardados antes de la 1.0.2); vídeo privado | «Comprobar el vídeo»; tiempos de las preguntas frente a inicio y final |
| No aparece «Empezar a preparar» | Vídeo incompleto, otro intento en marcha, sin intentos, nota anterior sin publicar, fuera de fechas | Estado en el informe; intentos y publicación |
| «Debes prepararte un poco más» | Preparación mínima sin cumplir | Valor de «Preparación mínima» |
| La conversación no empieza (código S) | Clave, modelo o proveedor | Motivo del código; «Probar la conexión» |
| La conversación se corta (código T o L) | Límites del sitio, cuota del proveedor, caída | Motivo del código; alumnos simultáneos frente a límites |
| «El contenido fue marcado por el filtro» | Moderación de OpenAI | Si es un falso positivo recurrente, valorar el ajuste con el responsable |
| No se oye al avatar | Voz de servidor fallida, audio bloqueado, «Sin voz» | Proveedor de TTS y su clave; «Comprobar el sonido» |
| El alumno no puede hablar | Sin https, navegador sin reconocimiento, permiso denegado, red que bloquea el servicio de voz | Navegador y mensaje mostrado; escribir como alternativa |
| «En evaluación» durante mucho tiempo | Cron parado, clave o cuota, evaluación que falla y se reintenta o que agotó sus reintentos | Cron; «Probar la conexión»; pasados 30 minutos, «Evaluar de nuevo» en la revisión |
| «Un tutor está revisando tu resultado» | Espera validación; hay avisos; nota retirada | Filtro «Por revisar» |
| La nota se publicó sola | Validación desactivada en la actividad y sin avisos | Ajuste de la actividad y bloqueo del sitio |
| Nota baja «injusta» | Poca participación, criterio no evidenciado, entregable no subido (cuenta 0), pesos | Puntuación por criterio y citas; avisos; pesos del bloque |
| Aviso «La IA no ha podido leer la imagen» | Proveedor sin lectura de imágenes (DeepSeek), imagen ilegible, fallo del análisis | Proveedor del modelo de evaluación; ver la imagen en la revisión |
| Aviso «Algunas respuestas se han pegado» | El alumno pegó texto en el campo de respuesta | Modo de cada turno en la revisión |
| No puede repetir | Nota sin publicar, intentos agotados, fuera de fechas | Publicación; intentos; excepción |
| Falta la nota en el libro | Sin publicar, retirada, modo prueba, actividad antigua con escala o sin calificación | Estado del resultado; tipo de calificación |
| Borrador con IA no llega | Falta transcripción o misión, límite de 30 al día, cron, clave | Mensaje mostrado; cron |

## Dudas sobre la nota: tabla por criterio
| Criterio y peso | Qué dijo el alumno (cita) | Puntuación de la IA | ¿La cita sostiene el nivel? | Certeza |
Comparar después vídeo, entregable y conversación con los pesos del bloque, y la media de bloques. No rehacer la evaluación en el chat como si fuera la del plugin.

## Cierre del caso
Indicar causa confirmada, probable o no comprobable; ajuste propuesto; prueba de una sola variable; y qué evidencia falta. Escalar al mantenedor solo con pasos reproducibles y tras probar los ajustes.
