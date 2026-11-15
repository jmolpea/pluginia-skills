# Funcionamiento de AI Viva 1.3.0

Documentación funcional derivada de una revisión estática de la versión 1.3.0 (versión interna 2026100700), revisada el 15-11-2026. Todo lo que sigue es «hecho verificado en el código» salvo que se marque como hipótesis. No se ha ejecutado en un Moodle para escribir este documento.
Manual público: https://claude.ai/artifact/RckemidnHhdYikr8HM2XHQ

## Qué es
Actividad de Moodle (aparece como «AI Viva») para Moodle 4.5 a 5.3. El alumno defiende un trabajo en tres pasos: documento PDF, videopresentación con pantalla compartida y tribunal oral con tres examinadores de IA. La IA propone una nota con comentarios y el profesorado la revisa y publica.
Único proveedor de IA: OpenAI (modelos de texto, transcripción de voz y voces). No hay opción de otro proveedor ni de servidor propio.
Requisitos: sitio con HTTPS, cron de Moodle cada minuto, navegador de escritorio actual con micrófono y altavoces. No necesita programas adicionales en el servidor.

## Licencia
Sin clave, el plugin funciona completo durante un periodo de evaluación de 15 días desde su primer uso. Gestores y administradores ven un aviso con los días restantes; los alumnos no.
La clave está ligada a la dirección web exacta del sitio y se valida sin conexión. Puede tener fecha de caducidad o ser permanente.
Sin licencia válida (evaluación terminada, clave caducada o de otra dirección) la actividad muestra un mensaje de bloqueo en lugar de la defensa y no se hace ninguna llamada a la IA, tampoco desde tareas en segundo plano. Los datos ya guardados no se borran.

## Flujo del alumno
1. Aviso de privacidad. Se muestra antes de cada intento. Al marcar la casilla y pulsar el botón de inicio se crea el intento. Sin consentimiento no se puede subir nada.
2. Paso 1, documento. Sube un PDF y confirma; no puede cambiarlo en ese intento. El análisis se hace nada más subirlo; si el servidor no puede hacerlo en ese momento o falla, queda en cola para el cron. La página consulta el estado cada pocos segundos y avanza sola.
3. Paso 2, presentación. El navegador pide micrófono y después la pantalla o ventana a compartir. Cuenta atrás de 5 segundos, grabación con cronómetro y avisos cuando quedan 2 minutos y 1 minuto; al agotarse el tiempo se detiene sola. El alumno revisa la grabación y la envía o vuelve a grabar. Se suben tres cosas: el vídeo (para el docente), el audio en partes de 4 minutos (para transcribir) y capturas de pantalla periódicas (para el análisis visual). No se graba la cámara.
4. Paso 3, tribunal. Pantalla previa con prueba de micrófono obligatoria. Al iniciar, el presidente (miembro 1) da la bienvenida y pide un resumen. Después los examinadores preguntan por turnos en orden 1, 2, 3, 1… El alumno responde pulsando un botón, hablando y volviéndolo a pulsar. Cada respuesta se transcribe, se muestra en pantalla y genera la siguiente pregunta, que se oye con la voz del examinador. Si el audio no llega se reintenta y, si sigue sin llegar, la pregunta se muestra solo como texto.
5. Cierre. Al acabar el tiempo, el presidente se despide, el intento queda entregado y la evaluación se pone en cola. La página espera y se actualiza sola.
6. Resultados. Con la nota en revisión ve un mensaje de espera. Con la nota publicada ve la calificación sobre el máximo, los comentarios y, solo si ningún docente editó la nota, la tabla de puntuación de cada paso.

## El reloj del tribunal
Lo lleva el servidor. Empieza cuando el tribunal tiene lista su primera intervención (una caída de la IA antes de empezar no consume tiempo) y no se detiene ni se puede pausar.
Recargar la página o volver a entrar reanuda la misma sesión con la conversación y el tiempo restante; no la reinicia.
La sesión dura siempre el tiempo configurado: no hay botón para terminar antes y el cierre solo se acepta cuando el tiempo está prácticamente agotado.
Una respuesta enviada hasta 2 minutos después del final todavía se acepta.
Si el alumno se fue, una tarea programada (cada 10 minutos) cierra las sesiones cuyo tiempo terminó hace más de 15 minutos y pide su evaluación con lo que haya.
La ventana de apertura y cierre de la actividad no corta un tribunal ya iniciado.

## Estados de un intento
«Sin empezar» (consentimiento dado), «Analizando documento», «Paso de presentación» (pendiente de grabar o analizándose), «Paso de tribunal», «Pendiente de evaluación», «Evaluándose», «Calificada».
Estado de revisión de un intento calificado: «En revisión» (el alumno no ve la nota, no está en el libro de calificaciones) o «Publicado».
Si el análisis del documento o de la presentación falla en la tarea en cola, el intento avanza igualmente al paso siguiente con ese análisis vacío; el alumno no queda bloqueado por ello.

## Qué se envía a OpenAI y qué no
Se envía: el PDF completo tal como lo subió el alumno; el audio de la presentación y de cada respuesta al tribunal (para transcribirlos); hasta 40 capturas de la pantalla; las transcripciones y análisis resultantes; los textos del docente (nombre y descripción de la actividad, instrucciones y prompts de cada paso, personalidad de los examinadores, restricciones adicionales); el texto de cada intervención de los examinadores (para ponerle voz).
No se envía: el nombre ni el correo del alumno en Moodle (se usa un código seudónimo estable por sitio), ni el archivo de vídeo.
El contenido puede identificar al alumno (portada del PDF, lo visible en pantalla, la voz). El plugin no lo anonimiza.
Cada instrucción a la IA marca el contenido del alumno como datos y pide ignorar órdenes incluidas en él. Es una mitigación, no una garantía.
El idioma de análisis, preguntas y comentarios es el del perfil de Moodle del alumno.

## Cómo se construye la evaluación
Análisis del documento: la IA recibe el PDF entero con el encargo y el prompt del paso 1. Si ese envío falla (por ejemplo, el PDF supera los límites del servicio), se recurre a extraer solo el texto del PDF, que es menos fiable y casi vacío en PDF escaneados.
Análisis de la presentación: transcripción completa más capturas, con el encargo y el prompt del paso 2.
Informe para el tribunal: antes de empezar, la IA resume tesis, temas a explorar, puntos fuertes, debilidades y líneas de pregunta a partir de los análisis. Los examinadores lo usan como guía y no deben revelarlo.
Evaluación final: recibe el encargo, los prompts de los pasos 1 y 2 como criterios, el prompt de evaluación final, el PDF original si sigue guardado, los dos análisis, la transcripción de la presentación y la conversación completa. Puntúa cada paso de 0 a 100 con un comentario, redacta comentario general, puntos fuertes, aspectos a mejorar y, si procede, alertas de integridad académica.
La nota no la calcula la IA: el plugin aplica los tres pesos a las tres puntuaciones y lo convierte a la calificación máxima.
Si al evaluar falta un análisis pero los archivos siguen guardados, se intenta generarlo de nuevo antes de evaluar.
La evaluación siempre se hace en segundo plano (cron). Si falla, Moodle la reintenta más tarde y el intento vuelve a «Pendiente de evaluación»; mientras tanto un docente puede calificar a mano.

## Retención y publicación de la nota
Con «Retener las calificaciones para revisión del profesor» activado (valor de fábrica), la primera evaluación deja la nota «En revisión» y avisa a los docentes que pueden calificar a ese alumno.
Desactivado, la nota se publica sola y se avisa al alumno, excepto en dos casos que siempre esperan a un docente: la IA no pudo leer parte del trabajo, o señaló alguna alerta de integridad académica.
Al libro de calificaciones solo llegan notas publicadas; con varios intentos, la más alta de las publicadas.
Un intento nuevo solo puede empezar cuando el anterior está calificado y publicado, la actividad está abierta para ese alumno y no se ha alcanzado su máximo de intentos.

## Qué puede hacer el profesorado (página de entregas)
Ver cada intento: PDF, vídeo, transcripción, análisis, conversación con el audio de cada respuesta, puntuación por paso y alertas.
Guardar una nota y comentarios editados (queda marcada como editada), publicar, retirar una nota publicada, eliminar el intento.
Regenerar: solo el análisis del documento, solo el de la presentación, solo la evaluación final, o todo. Cualquier opción termina repitiendo la evaluación final. Solo en intentos ya entregados.
Efectos de regenerar: no se notifica al alumno; una nota o comentarios editados por un docente se conservan (solo se actualizan la propuesta de la IA y el desglose); el estado de revisión se mantiene, salvo que la actividad no retenga notas y la nueva evaluación no tenga motivos de retención, en cuyo caso pasa a publicada.
Con grupos separados, un docente sin acceso a todos los grupos solo ve, descarga y regenera intentos de alumnos de sus grupos.

## Tareas programadas
Cierre de tribunales abandonados: cada 10 minutos.
Borrado de grabaciones antiguas: cada noche a las 02:30. Borra vídeo, audios de la presentación, capturas y audios de las respuestas. Nunca borra el PDF, las transcripciones, los análisis ni las notas. Ver condiciones en el documento de límites.
Tareas en cola: análisis del documento, análisis de la presentación (solo cuando no pudieron hacerse al subir) y evaluación final (siempre).

## Qué se guarda
Por intento: consentimiento y su fecha, estado, número de intento, análisis del documento, transcripción y análisis de la presentación, informe para el tribunal, hora de inicio del tribunal, cada turno de la conversación con su hora, nota propuesta por la IA, nota final, comentarios, desglose por paso, respuesta completa de la evaluación, quién editó la nota, estado de revisión y fechas.
Archivos: PDF, vídeo, partes de audio, capturas, audio de cada respuesta e imágenes de avatar personalizadas.
No se guarda un historial de las instrucciones enviadas a la IA ni de cada llamada. El detalle de un error del servicio de IA solo va al registro del servidor; el alumno ve un mensaje genérico.

## Permisos de fábrica (nombres visibles en Moodle)
«Añadir una actividad AI Viva»: profesor con edición y gestor.
«Ver la actividad AI Viva»: alumno, profesores y gestor; invitados no.
«Enviar una presentación»: solo alumno; denegado a profesores y gestores, que por eso no pueden hacer la defensa con su cuenta.
«Ver todas las entregas» y «Calificar entregas»: profesores (con y sin edición) y gestor. Calificar incluye publicar, retirar, regenerar y eliminar.
«Gestionar anulaciones de usuario y grupo»: profesor con edición y gestor.
«Gestionar la configuración del plugin»: gestor; solo sirve para ver el aviso del periodo de evaluación. La página de ajustes del sitio la controla el permiso general de administración de Moodle.

## Privacidad, copias de seguridad y finalización
Implementa la API de privacidad de Moodle: exporta y borra intentos, conversaciones, archivos y excepciones de usuario; de un docente exporta las notas que editó y, al borrar sus datos, la nota se conserva marcada como editada.
Copia de seguridad: la configuración de la actividad, los avatares personalizados y las excepciones de grupo viajan siempre; intentos, archivos y excepciones de usuario solo si se incluyen datos de usuario. Las claves de API y la licencia no viajan.
Finalización: condición propia «completar los tres pasos», que se cumple al terminar el tribunal aunque la nota no esté publicada. También admite las condiciones estándar por calificación.
Notificaciones: «Calificación de AI Viva publicada» (alumno) y «Entrega de AI Viva pendiente de revisión» (docentes); cada usuario las gestiona en sus preferencias.

## Lo que la versión 1.3.0 no hace
No tiene entregas en grupo, ni eventos de calendario para las fechas, ni informe de costes o de uso, ni exportación de evaluaciones.
El reinicio de curso de Moodle no elimina los intentos de AI Viva (no se encontró esa función en la revisión): hay que eliminarlos desde la página de entregas o borrar la actividad.
No detecta plagio ni compara trabajos entre alumnos: las alertas de integridad salen solo de incoherencias entre el documento y lo dicho.
