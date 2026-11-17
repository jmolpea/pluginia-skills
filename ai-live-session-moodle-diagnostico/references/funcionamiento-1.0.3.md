# Funcionamiento verificado de AI Live Session 1.0.3

Base: revisión estática del código que declara la versión 1.0.3 (versión interna 2026111700, Moodle 4.5 a 5.3, PHP 8.1 o posterior), el 17-11-2026. No se comparó el ZIP instalado ni se ejecutó Moodle para esta revisión. Manual público: https://claude.ai/artifact/J58N9JJybXxofoznCsvqro

## Qué es
Actividad de Moodle. Una sesión tiene uno o varios bloques que el alumno hace en orden. Cada bloque tiene hasta tres pasos: vídeo con preguntas, práctica cronometrada con entregable y conversación con un avatar de IA. El docente elige en «Pasos de la sesión» hasta dónde llega: solo vídeo, vídeo y práctica, o los tres.
Principio general: el servidor decide posición del vídeo, correcciones, relojes, cambios de fase y aritmética de la nota. El navegador solo muestra. Las respuestas correctas no se envían al navegador antes de que el alumno conteste.

## Requisitos para que un alumno pueda empezar
- Licencia válida o periodo de evaluación vigente (15 días desde el primer uso, con todas las funciones). Sin ello, la actividad muestra un aviso y no hace nada.
- Todos los bloques completos. Si falta algo, el alumno ve «Esta sesión todavía no está disponible» y el diseñador indica qué falta: vídeo, inicio y final, misión, avatar, rúbrica con pesos que sumen 100 o pesos de la nota que sumen 100. Solo se exige lo que usan los pasos elegidos.
- Dentro de las fechas de apertura y cierre (con sus excepciones). Las fechas no afectan al docente que prueba la sesión.
- Aceptar el aviso de datos de la portada.
- Para hablar: sitio en https y navegador con reconocimiento de voz (Chrome, Edge o Safari). Si no, escribe.

## Vídeo
- Fuentes: YouTube, Vimeo o archivo subido. Cada bloque reproduce un fragmento (inicio y final) y varios bloques pueden compartir un vídeo.
- El navegador informa de la posición de forma periódica. El servidor solo acepta avanzar al ritmo del tiempo real multiplicado por la «Velocidad máxima»; lo que vaya más allá no cuenta y las preguntas posteriores no se entregan. Se puede retroceder. Al cambiar de pestaña el vídeo se detiene. Si un aviso de posición falla, el vídeo espera, muestra «Problema de conexión» bajo el reproductor, lo reintenta solo y sigue al volver la conexión (desde la 1.0.1).
- El vídeo se detiene en cada pregunta. Tipos: opción única, opción múltiple (todas las correctas), verdadero o falso, decisión sobre un caso y encuesta (sin puntos; muestra el reparto del grupo).
- Solo puntúa la primera respuesta. Con «El vídeo solo continúa tras acertar», el alumno repite hasta acertar, pero la puntuación no cambia. Mientras deba repetir no se le muestra la solución.
- El vídeo se completa al llegar al final del fragmento (con unos segundos de tolerancia) sin preguntas pendientes. Su resultado es el porcentaje de puntos conseguidos a la primera; si no hay preguntas puntuables, no hay resultado de vídeo (en «Solo vídeo» cuenta como 100).
- En Vimeo, ocultar controles y cambiar la velocidad exigen cuenta de pago. Los archivos subidos no tienen subtítulos; el «Texto del vídeo» se ofrece debajo del reproductor.

## Práctica
- Tras el vídeo hay una pantalla de transición. El reloj empieza cuando el alumno pulsa el botón.
- El alumno escribe notas (se guardan solas cada pocos segundos), rellena los «datos corregidos» si existen y entrega una imagen, un texto o nada, según el bloque.
- Los datos corregidos los corrige el servidor sin IA: ignora mayúsculas, acentos, espacios y separadores, trata la coma decimal como punto y admite varias respuestas separadas por barra vertical.
- La preparación se cierra cuando el alumno dice que está listo (si ha pasado la «Preparación mínima») o cuando se agota el tiempo. Después no se puede cambiar nada.
- Al cerrarse, una tarea en segundo plano analiza el entregable: describe lo que ve y lo puntúa de 0 a 100 según la misión y «Qué debe mostrar la imagen». Si esa tarea falla, la evaluación lo vuelve a intentar.
- En sesiones de «Vídeo y práctica», cerrar la preparación entrega el trabajo y lanza la evaluación; una tarea periódica entrega las preparaciones cuyo tiempo terminó.

## Conversación
- El alumno la inicia. Primero se genera la frase inicial del avatar y solo entonces arranca el reloj: si la IA falla al empezar, no se pierde tiempo.
- Cada turno: el alumno habla (su navegador lo transcribe) o escribe; el servidor guarda el texto, pide la respuesta al modelo y, si hay voz de servidor, genera el audio. Es la única llamada a la IA dentro de la petición del alumno.
- El avatar conoce: su nombre, papel, tono y personalidad; la misión; los nombres de los criterios de la rúbrica; un resumen de los bloques anteriores; las preguntas del vídeo que el alumno falló o repitió; sus datos corregidos; sus notas; su texto entregado y el análisis de su entregable; y su nombre de pila. No conoce apellidos, usuario ni correo (se sustituyen por un código si aparecen en el texto).
- Responde en el idioma de la interfaz del alumno, en frases cortas pensadas para oírse. Según el tono presiona más o menos; solo el tono «Acompañante» da pistas o explicaciones.
- Termina por: el alumno pulsa terminar, se agota el tiempo, o el avatar la cierra cuando ya ha salido todo lo que buscaba.
- Si el navegador se cierra, el reloj se detiene tras un minuto y medio sin señal, hasta el máximo de «Tiempo que el reloj puede detenerse». Una tarea que corre cada 5 minutos cierra las conversaciones agotadas; si el navegador no estaba, las marca como interrumpidas.
- Si la IA falla en un turno: el alumno ve un mensaje sencillo con un código ALS-, se le devuelve el tiempo perdido y puede reintentar sin duplicar su respuesta. Si hay «Proveedor de reserva», el avatar sigue con él sin que el alumno lo note y el fallo queda registrado.
- Si falla solo la voz, el texto se muestra igual y el navegador intenta leerlo con su propia voz.
- Moderación: con modelo de OpenAI y el ajuste activado, cada respuesta del alumno pasa antes por el filtro de OpenAI; si la marca, no se contesta. Si el filtro no responde, la conversación sigue.

## Evaluación y nota
- Siempre en segundo plano (depende del cron de Moodle). Si falla, Moodle la reintenta más tarde con esperas crecientes, hasta un número limitado de veces. Si un intento lleva más de 30 minutos esperando, el tutor ve «Evaluar de nuevo» en la revisión y puede volver a lanzarla (desde la 1.0.2).
- La IA recibe la misión, la rúbrica con sus tres niveles, las instrucciones del docente para la evaluadora y la conversación etiquetada. Puntúa cada criterio de 0 a 100 citando frases del alumno; solo cuentan las palabras del alumno. La respuesta debe ser estructurada y con números en rango; si no, se rechaza y se reintenta.
- Nota de la conversación: media de los criterios ponderada por sus pesos.
- Nota del entregable: la del análisis de la imagen o texto; si además hay datos corregidos, la media de ambas. Una imagen pedida y no subida cuenta 0. Si no se pudo analizar, el entregable no cuenta y queda un aviso.
- Nota del bloque con conversación: vídeo, entregable y conversación con los pesos del bloque; la parte que no existe reparte su peso. En «Vídeo y práctica»: media simple de vídeo y entregable. En «Solo vídeo»: porcentaje del vídeo.
- Nota de la sesión: media simple del mejor intento evaluado de cada bloque, convertida a la puntuación máxima de la actividad. Solo se propone cuando todos los bloques tienen su último intento evaluado. Si se cambia la puntuación máxima, las notas que aún no están en el libro de calificaciones se recalculan en proporción; con notas ya en el libro, Moodle no deja cambiar el máximo.
- Con varios bloques y conversación, otra tarea redacta un comentario general a partir de los comentarios de cada bloque, sin puntuar nada.
- Avisos posibles: sin participación, participación insuficiente (menos de 20 palabras), respuestas pegadas, posible intento de manipular a la IA, conversación interrumpida, entregable no leído, y los que señale la propia IA. Sin ninguna palabra del alumno no se llama a la IA: la conversación puntúa 0.

## Publicación
- Con «Un tutor valida la nota…» activo: queda «Por revisar», los tutores que pueden ver al alumno reciben un aviso y el alumno ve que un tutor lo está revisando. El tutor puede cambiar nota y comentario y publica.
- Desactivado: se publica sola, salvo si hay algún aviso o si esa nota fue retirada antes por un tutor.
- Si el administrador bloquea el ajuste del sitio, manda sobre todas las actividades.
- Publicar escribe en el libro de calificaciones y avisa al alumno. «Retirar la nota» la saca del libro.
- «Evaluar de nuevo»: si un tutor ya validó, su nota se conserva y solo cambia la propuesta; si se publicó sola, sale del libro y espera a un tutor.
- Otro intento: solo con la nota de la sesión publicada y con intentos disponibles. Repite práctica y conversación del bloque; el resultado del vídeo se conserva.
- Finalización («El alumno debe terminar una conversación»): se cumple al cerrar el último paso de todos los bloques, sin esperar a la nota.

## Roles
- Administrador: ajustes del sitio, prueba de conexión y detalle técnico de los problemas.
- Profesor con edición y gestor: diseñador, borradores con IA, excepciones, reinicios, modo prueba, informe y validación.
- Profesor sin edición: modo prueba, informe, problemas técnicos y validación.
- Alumno: participa; puede retirar su consentimiento (borra sus datos de la sesión y necesita que un tutor lo reinicie para volver).
- Modo prueba: IA real con coste real, puede saltar entre bloques y nada llega al libro de calificaciones.
- Resumen de actividades del curso (página «Actividades», solo en Moodle 5.0 o posterior; en 4.5 no existe): quien puede ver el informe ve, por actividad, «Fecha de cierre», «Estudiantes que empezaron» (aceptaron el aviso de datos) y «Estudiantes que terminaron» (nota propuesta o publicada), ambos sobre el total de alumnos, «Notas pendientes de un tutor» y un botón «Ver» que abre el informe, filtrado por «Por revisar» si hay notas esperando (con un indicador del número). El alumno ve «Fecha de cierre» (con sus excepciones), «Tu estado» (Sin empezar, En curso, En evaluación, Pendiente de un tutor, Publicada o Consentimiento retirado) y su nota cuando está publicada. Quienes solo prueban la sesión no cuentan. Antes de la 1.0.3 la página decía que la información no estaba disponible.
- Grupos separados: el resumen del curso cuenta solo a los alumnos de los grupos del docente; informe, revisión, avisos, excepciones y problemas técnicos se limitan a los alumnos que el tutor puede ver.

## Qué se guarda y qué sale del sitio
- Se guarda en Moodle: consentimiento, progreso del vídeo, respuestas, intentos (notas, datos, texto, análisis, puntuaciones, relojes), turnos de la conversación con su modo (hablado, escrito o pegado), resultado y comentario, excepciones, problemas técnicos y borradores del docente. La imagen entregada se guarda como archivo.
- No se graba ni se guarda audio.
- Al proveedor de IA: textos de la actividad, nombre de pila, lo dicho o escrito, notas, datos, texto e imagen entregados. A YouTube o Vimeo: lo propio de cargar su reproductor. Al fabricante del navegador: posiblemente el audio del reconocimiento de voz.
- La licencia se comprueba sin conexión; el plugin no contacta con el vendedor.
- Copias de seguridad: incluyen contenido y, con datos de usuario, todo lo del alumno; no incluyen problemas técnicos ni borradores. Sin datos de usuario solo viajan las excepciones de grupo.

## Cambios respecto a la 1.0.0
- 1.0.1: reintento automático de los avisos del vídeo y aviso «Problema de conexión»; mejoras de pantalla completa y de tablas en móvil.
- 1.0.2: las fechas ya no frenan el modo prueba; el editor rechaza un «Final del bloque» que deje preguntas en ese punto o después; el formulario de la actividad exige calificación por puntuación con máximo de 1 o más (las actividades guardadas antes con escala o «Ninguna» siguen pudiendo editarse tal como están); «Evaluar de nuevo» para evaluaciones que no llegan; al borrar un bloque se propone la nota de quienes ya habían terminado los demás; la lista de excepciones muestra «Ilimitado»; la revisión distingue «Preparado, sin empezar la conversación»; enlace al manual en los ajustes del sitio y en el formulario de la actividad.
- 1.0.3: columnas propias en el resumen de actividades del curso de Moodle 5.0 o posterior.

## Limitaciones conocidas de la 1.0.3 (verificadas leyendo el código)
- Un bloque guardado con una versión anterior puede conservar una pregunta situada después del final del fragmento: nadie completa ese vídeo hasta moverla o borrarla. La 1.0.2 lo impide al guardar los cortes, pero no corrige lo ya guardado.
- Una actividad guardada antes con escala o sin calificación sigue sin poder validar notas hasta que se cambie a puntuación.
- «Evaluar de nuevo» en un intento sin evaluar aparece solo pasados 30 minutos, y respeta la espera de 5 minutos y el máximo de 5 al día.
- Al borrar un bloque en una sesión de «Solo vídeo» o con notas ya propuestas, las notas existentes de quienes no tenían intentos en ese bloque no se recalculan.
