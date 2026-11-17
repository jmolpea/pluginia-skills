# Protocolo de diagnóstico de AI Viva

Para la versión 1.3.2, revisado el 17-11-2026.

## Ficha mínima
Pedir según la consulta, no todo siempre:
- Versión de Moodle y del plugin; estado de la licencia que muestra la página de ajustes.
- Quién informa (administrador, docente, alumno) y qué mensaje exacto ve en pantalla.
- Paso en el que ocurre y estado del intento en la página de entregas (estado y estado de revisión), número de intento.
- Ajustes relevantes de la actividad: intentos, fechas, duraciones, tamaños, modelos, pesos, retención de notas, días de conservación, excepciones que afecten al alumno.
- Navegador, sistema y tipo de dispositivo del alumno; si el sitio usa HTTPS.
- Si el cron se ejecuta cada minuto y cuándo fue la última ejecución.
- Para calidad de evaluación: prompts de los tres pasos, personalidad de los examinadores, restricciones adicionales, desglose por paso, comentarios y, anonimizados, los análisis, la transcripción y la conversación.
- Para errores del servicio de IA: lo que diga el registro del servidor (lo aporta el administrador) y el estado de la cuenta de OpenAI.
No pedir claves ni acceso administrativo. Pedir anonimización.

## Árbol síntoma → causas → comprobación

### La actividad muestra un aviso de licencia y no deja trabajar
Causas: evaluación de 15 días terminada; clave caducada; clave emitida para otra dirección (cambio de dominio, de carpeta o de http a https).
Comprobar: estado bajo el campo «Clave de licencia»; dirección actual del sitio frente a la de la licencia.

### «El servicio de IA no pudo completar la solicitud»
Causas probables: clave de OpenAI ausente, incorrecta o revocada; cuenta sin saldo o con el límite de gasto alcanzado; saturación del servicio; tiempo de espera insuficiente en documentos muy largos; el servidor no puede salir a internet.
Comprobar: registro del servidor (ahí está el motivo real); panel de OpenAI; repetir con un PDF pequeño.
Nota: el alumno nunca ve el motivo real; no deducirlo del mensaje.

### El alumno se queda en «Analizando…» (documento o presentación)
Causas: cron parado o lento (el análisis quedó en cola); análisis largo en curso; el proceso que hacía el análisis en el momento de la subida fue interrumpido por el servidor.
Hecho (desde 1.3.1): hay una tarea de respaldo que repite el análisis 30 minutos después de la subida si el intento sigue sin avanzar. En 1.3.0 y anteriores no existía y el intento podía quedarse esperando indefinidamente.
Comprobar: versión instalada; que el cron corre; tareas en cola pendientes de AI Viva; tiempo transcurrido.
Salida: esperar al menos 30 a 40 minutos con el cron en marcha; si después sigue igual, el docente puede eliminar el intento para que el alumno empiece otro (acción irreversible).

### No puede subir el PDF
Causas: no es un PDF real (documento renombrado); supera «Tamaño máximo del PDF (MB)»; supera el límite de subida del servidor; actividad cerrada; falta el consentimiento.
Comprobar: mensaje exacto («Solo se aceptan archivos PDF», «El archivo supera el tamaño máximo», «No se ha podido subir el archivo»).

### No puede grabar o no se sube la grabación
Causas: navegador no compatible o móvil; sitio sin HTTPS; permisos de micrófono o de pantalla denegados; grabación mayor que el tamaño de vídeo de la actividad; límites de subida del servidor menores que ese tamaño; conexión lenta.
Comprobar: mensaje exacto; tamaño que indica la pantalla de revisión; límites del servidor con el equipo de sistemas.
Ajuste típico: compartir una ventana con diapositivas en lugar de vídeo en movimiento; reducir la duración.

### En el tribunal no se oye a los examinadores
Causas: altavoces o auriculares; fallo del servicio de voz (la pregunta aparece como texto y la sesión continúa); límite de llamadas por minuto alcanzado.
Comprobar: si el texto de la pregunta aparece; si otros alumnos lo sufren a la vez.

### «No se ha oído voz en tu respuesta» o la respuesta es «demasiado corta»
Causas: micrófono equivocado o silenciado; pulsó y soltó sin hablar; ruido sin voz.
Comprobar: la barra de nivel de la prueba de micrófono.

### «Has realizado demasiadas solicitudes»
Causa: límite de llamadas por usuario y minuto. Cada respuesta gasta unas tres.
Comprobar: valor del ajuste (30 de fábrica; 0 equivale a 1). El reloj no se detiene mientras espera.

### El tribunal «se cortó» o se cerró solo
Hechos: el reloj no se pausa; al acabar el tiempo se cierra; si el alumno salió, se cierra por tarea programada 15 minutos después del final.
Comprobar: duración configurada, hora de inicio y turnos guardados en el detalle del intento.
Salida: no se puede reabrir. Opciones del docente: evaluar lo que hay, calificar a mano, o eliminar el intento / dar un intento más con una excepción.

### El intento sigue en «Pendiente de evaluación» o «Evaluándose»
Causas: cron parado; el servicio de IA falla y la tarea se reintenta; el filtro de moderación bloquea el contenido en cada reintento; límite de llamadas; respuesta no válida de la IA.
Comprobar: cola de tareas y su último error; estado de la cuenta de OpenAI; si la materia puede activar el filtro.
Salida: el docente puede calificar a mano desde el detalle del intento sin esperar.

### La nota no aparece en el libro de calificaciones o el alumno no la ve
Causas: está «En revisión» (retención activada, trabajo no leído del todo o alerta de integridad); se retiró después de publicarla; hay otro intento publicado con nota más alta.
Comprobar: estado de revisión de cada intento del alumno.

### Aviso «La IA no pudo leer parte de este intento»
Hecho: falta el análisis del documento o la transcripción de la presentación; ese paso pudo puntuarse como no realizado.
Salida: «Re-analizar todo» (si la grabación no se ha borrado) o calificar a mano antes de publicar.

### El alumno no puede iniciar otro intento
Causas: el anterior no está calificado y publicado; alcanzó su máximo (actividad o excepción); la actividad no está abierta para él.
Comprobar: intentos del alumno, excepciones de usuario y de sus grupos.

### La evaluación parece injusta, genérica o incoherente
Comprobar por este orden: prompts vacíos o contradictorios; criterios situados en el paso equivocado; pesos; modelo elegido; análisis vacíos; PDF escaneado o por encima de los límites del servicio (análisis solo con texto); transcripción pobre por mal audio; idioma del perfil del alumno; duración del tribunal demasiado corta para el número de preguntas esperado.
Construir la tabla por paso: evidencia, qué recibió la IA, puntuación y comentario, explicación y certeza.
No reevaluar el trabajo en el chat como si fuera el plugin.

### Las grabaciones han desaparecido
Hecho: borrado nocturno según «Conservar las grabaciones (días)». Se conservan PDF, transcripciones y notas.
Comprobar: versión instalada (la regla cambió en 1.3.1), días configurados, fecha de publicación de la nota y fecha de fin del tribunal (ver reglas en límites).

### La IA responde en un idioma inesperado
Hecho: usa el idioma del perfil de Moodle del alumno, no el del curso ni el del documento.

## Grado de certeza
Confirmado: evidencia directa del caso y regla documentada aplicable.
Probable: mecanismo compatible con el síntoma, pendiente de una comprobación identificada.
No comprobable: falta la evidencia decisiva; decir cuál.

## Escalado al mantenedor
Entregar una ficha con: versiones, síntoma, comportamiento esperado, configuración relevante, pasos para reproducirlo con un alumno de prueba, resultados observados, ajustes probados y su resultado, hipótesis descartadas y evidencia que falta.
No incluir claves, datos personales ni código. No afirmar que la solicitud se ha enviado. Contacto: julio@rsmax.es.
