# Protocolo de diagnóstico

## Ficha mínima
Pedir según la consulta, no todo siempre:
- Versión de Moodle y del plugin; estado de la licencia tal como se lee en los ajustes.
- Proveedor de chat, proveedor de TTS y motor de voz del sitio; modelos de la actividad.
- Resultado de «Ejecutar la prueba de conexión» (las filas y sus mensajes).
- Ajustes de la actividad: duración, intentos, fechas, número de avatares, micrófono, revisión del profesor.
- Qué ve exactamente el usuario: mensaje literal, en qué paso y con qué rol.
- Navegador, dispositivo, si el sitio usa https y si se concedió el micrófono.
- Para notas: estado del intento, «En revisión» o «Publicado», avisos, palabras dichas y desglose.
- Si el cron de Moodle se ejecuta y con qué frecuencia.
No pedir claves ni la clave de licencia. Pedir las conversaciones anonimizadas.

## Árbol síntoma → causas → comprobación

### La actividad muestra un aviso en lugar de su contenido
| Mensaje | Causa | Comprobación |
|---|---|---|
| «…no se ha introducido ninguna clave de licencia…» | Clave vacía | Ajustes del sitio, sección Licencia |
| «…la clave de licencia no corresponde a este sitio…» | Clave de otra dirección, incompleta o alterada | Comparar la dirección que cita el mensaje con la de la licencia |
| «…la licencia caducó el…» | Caducidad | Renovar con el proveedor del plugin |
| «Esta actividad se abre el…» / «…se cerró el…» | Fechas de la actividad o de una excepción | Disponibilidad y excepciones |
| «Has agotado los intentos permitidos…» | Intentos gastados | Intentos máximos y excepciones |

### El profesor no puede empezar la sesión
Causa confirmada por diseño: solo el rol de estudiante puede participar. Comprobación: probar con una cuenta de alumno matriculada.

### La sesión no arranca tras pulsar «Iniciar juego de roles»
1. «El plugin AI Roleplay no tiene configurada una clave API de… utilizable»: falta la clave del proveedor del modelo de esa actividad, o no se puede descifrar (por ejemplo, tras migrar el sitio): volver a pegarla.
2. «El servicio de IA no está disponible temporalmente»: error del proveedor. Ejecutar la prueba de conexión; causas habituales: clave incorrecta, saldo, modelo no disponible para la cuenta, caída.
3. «Debes dar tu consentimiento…»: el alumno no ha aceptado el aviso.
4. Límite de peticiones del sitio alcanzado.
Hecho: si la apertura falla, el intento no se gasta.

### El avatar contesta por escrito pero no suena
| Causa | Comprobación |
|---|---|
| Proveedor de TTS «Sin voz» | Ajustes del sitio |
| TTS de OpenAI o Gemini sin clave válida | Fila de voz de la prueba de conexión |
| Límite de llamadas por usuario alcanzado justo en la voz | Coincide con ritmo alto de turnos |
| Navegador sin sonido o bloqueando la reproducción | Probar otro navegador o dispositivo |
| TTS del navegador sin voces instaladas en ese idioma | Probar en otro equipo |

### El alumno tiene que escribir en vez de hablar
La página indica el motivo: micrófono bloqueado, sin micrófono, sitio sin https o navegador sin reconocimiento de voz. Comprobar navegador (Chrome, Edge, Safari), permiso del sitio y https. Redes que bloquean el servicio de voz del fabricante del navegador también lo impiden («No se ha podido acceder al servicio de reconocimiento de voz…»).

### La respuesta se envía antes de terminar o no se entiende
Manos libres envía tras unos 2 segundos de silencio; el ruido también interfiere. Cambiar «Micrófono» a «Pulsar para hablar y pulsar para enviar». Si el navegador cierra el micrófono repetidamente, el plugin cambia solo a pulsar para hablar. La calidad de la transcripción depende del navegador, no del plugin.

### «Has realizado demasiadas solicitudes» o límite de todo el sitio
Contar intervenciones por minuto y multiplicar por las llamadas por intervención (ver límites). Subir el límite por usuario o el del sitio. Hipótesis a comprobar: varias pestañas o varios alumnos con la misma cuenta.

### «El contenido fue marcado por el filtro de seguridad de la IA»
Moderación de OpenAI (si está activa y el modelo es de OpenAI) o filtro propio del proveedor. Revisar qué dijo el alumno y si el escenario lo propicia.

### La evaluación no llega
1. Estado «Pendiente de evaluación» persistente: el navegador no la pidió o falló, y el cron no se ejecuta. Comprobar el cron y la tarea de evaluación.
2. Fallo repetido del proveedor en la evaluación: prueba de conexión; valorar subir el tiempo de espera o cambiar el modelo de evaluación.
3. «Evaluándose» durante mucho tiempo: puede retomarse pasados 30 minutos; un profesor no puede recalcular mientras está en ese estado.
4. Licencia caducada entre la sesión y la evaluación: las tareas no llaman a la IA.

### Nota 0 o muy baja
| Evidencia en el detalle del intento | Interpretación |
|---|---|
| Aviso «El estudiante no dijo nada…» | No se registró ninguna palabra del alumno; no se llamó a la IA. Muy probable problema de micrófono o de reconocimiento |
| Aviso «El estudiante habló muy poco…» | Menos de 20 palabras; poca evidencia |
| Muchas palabras de avatares y pocas del alumno | La nota solo valora al alumno |
| Conversación correcta y nota baja | Revisar desglose y comentarios; valorar instrucciones de evaluación |
| Sin conversación y texto de consentimiento retirado | El alumno retiró su consentimiento; no recalcular (la nota pasaría a 0) |

### El alumno no ve su nota o no está en el libro de calificaciones
«En revisión»: falta publicar, la revisión está activada o bloqueada por el administrador, o el intento tiene avisos. Solo las notas publicadas llegan al libro, y llega la mejor. Si el alumno retiró su consentimiento, no ve resultados hasta aceptarlo de nuevo.

### La nota no encaja con la escala
La nota se guarda ya convertida a la «Calificación máxima» vigente al evaluar. Si la escala se cambió después, las notas anteriores no se reconvierten: comprobar fechas del cambio y de los intentos.

### El tiempo real no se activa o se corta
Requisitos: motor elegido en el sitio, clave de ese proveedor y un solo avatar. Si falla la conexión, la sesión sigue por turnos con un aviso. Comprobar nombre del modelo de tiempo real, saldo y red del alumno. Gemini Live no está declarado como probado de extremo a extremo.

### El avatar habla en un idioma inesperado o se sale del papel
Idioma: el de Moodle del alumno en ese momento (o el forzado del curso). Papel: revisar personalidad, escenario y restricciones; un escenario vacío produce conversación genérica.

### Un profesor no ve a un alumno en «Entregas»
Grupos separados sin acceso a todos los grupos, o filtro de grupo activo.

## Cierre del diagnóstico
Indicar causa confirmada, probable o no comprobable; el ajuste propuesto; la prueba y quién la ejecuta. Si se sospecha un defecto del plugin, redactar para el mantenedor: versión, pasos exactos, resultado esperado y obtenido, mensajes literales y capturas sin datos personales.
