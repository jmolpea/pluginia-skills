# Funcionamiento de AI Roleplay 1.1.2

Documentación funcional derivada de una revisión estática de la versión 1.1.2 (interna 2026111700), revisada el 17-11-2026. Todo lo que sigue está verificado leyendo esa versión salvo lo marcado como «no verificado». Manual público: https://claude.ai/artifact/9rrxnBoMsHAgMzhKErn92D

## Qué es
Actividad de Moodle (aparece como «AI Roleplay» al añadir una actividad). El alumno conversa, hablando o escribiendo, con 1 a 3 avatares interpretados por una IA dentro de un escenario redactado por el docente. Al acabar el tiempo, una IA evalúa lo que dijo el alumno con una rúbrica fija de cuatro partes, pone nota y redacta comentarios. El profesorado revisa conversaciones y notas en la página «Entregas».
Requisitos declarados: Moodle 4.5 a 5.3, https (el micrófono lo exige), cron en marcha, clave de un proveedor de IA y una clave de licencia válida para la dirección del sitio.

## Licencia
La clave se comprueba sin conexión y está ligada a la dirección exacta del sitio. No hay periodo de prueba. Una licencia con fecha de caducidad vale hasta el final de ese día. Estados visibles en los ajustes: «Sin configurar», «Válida — caduca el…», «Válida — licencia permanente», «Caducada el…», «No válida — la clave no corresponde a este sitio».
Sin licencia válida, la actividad muestra un aviso («AI Roleplay no está disponible porque…») en lugar de su contenido y no se realiza ninguna llamada a la IA, tampoco desde tareas en segundo plano. Los datos no se borran.

## Recorrido del alumno y estados del intento
1. Consentimiento. La primera vez en cada actividad ve el aviso de privacidad y debe aceptarlo. Al aceptar se crea su primer intento en estado «Sin empezar».
2. Inicio. Pulsa «Iniciar juego de roles». Moodle comprueba fechas e intentos, pide a la IA la frase de apertura del avatar 1 y solo si llega pone el intento «En curso» y arranca el reloj. Si el proveedor falla en ese momento, el intento no se gasta.
3. Conversación. Cada respuesta del alumno se guarda y se envía al modelo junto con el historial. Si el avatar no llega a contestar (límite de peticiones, tiempo de espera, caída del proveedor), esa respuesta se retira de la conversación para que no quede repetida cuando el alumno la diga otra vez; una respuesta rechazada por el filtro de contenido sí se conserva, para que el profesor la vea. Cuando todo va bien, contesta un avatar con 1 a 3 frases, que se muestran y, si hay voz, se reproducen. Con varios avatares contesta el que el alumno nombra; si no nombra a ninguno, se turnan.
4. Cierre. Un intento que no ha llegado a empezar no se puede cerrar. Al agotarse el tiempo, o si el alumno pulsa dos veces «Terminar conversación», el intento pasa a «Pendiente de evaluación», el avatar 1 se despide y se marca la finalización si está configurada.
5. Evaluación. El navegador la pide en el momento; el intento pasa por «Evaluándose» y termina en «Calificado». Si el navegador no la pide (pestaña cerrada), una tarea en segundo plano la hace unos 2 minutos después del cierre.
6. Resultados. Con la nota publicada el alumno ve calificación, retroalimentación, puntos fuertes, aspectos a mejorar y desglose. Si está en revisión, lee que su profesor la está revisando. Solo se muestran los resultados del intento más reciente.
7. Nuevo intento. Con el último intento «Calificado», intentos disponibles y la actividad abierta, aparece «Empezar un nuevo intento».
El reloj lo lleva el servidor. Recargar la página reanuda la sesión con el tiempo realmente restante y la conversación ya mantenida. La sesión no se puede pausar. Una sesión ya en curso puede terminarse aunque haya pasado la fecha de cierre.
Un intento consume cupo desde que pasa a «En curso», aunque se abandone.

## Voz: quién hace qué
- Modo por turnos (de fábrica). La voz del alumno la convierte en texto el reconocimiento de voz del navegador (Chrome, Edge o Safari). El plugin no graba ni guarda audio y al proveedor de IA solo le llega texto. El navegador puede enviar el audio a los servidores de su fabricante para transcribirlo. Firefox no reconoce voz: el alumno escribe.
- Voz de los avatares. Según «Proveedor de TTS»: la genera el servidor con OpenAI o Gemini, la genera el navegador del alumno, o no hay voz y solo se ve el texto. Si la voz del servidor falla (falta de clave, error del proveedor), la frase se muestra igualmente sin sonido y la sesión continúa.
- Modos de micrófono por actividad: manos libres (el micrófono se abre tras cada frase del avatar y la respuesta se envía tras unos 2 segundos de silencio; se puede pausar), pulsar para hablar y pulsar para enviar, y mantener pulsado (botón o barra espaciadora). Safari y los navegadores que no mantienen el micrófono abierto pasan solos de manos libres a pulsar para hablar.
- Si no hay micrófono, se deniega el permiso, el sitio no usa https o el reconocimiento no está disponible, la página lo explica y el alumno escribe sus respuestas. La evaluación es la misma.
- Tiempo real (opcional, ajuste del sitio «Motor de voz»): con OpenAI Realtime o Gemini Live la voz del alumno va en directo al proveedor, que responde con su propia voz y admite interrupciones. Moodle abre la conexión con su clave; la clave no llega al navegador. Solo se aplica con un avatar y con la clave del proveedor puesta; en otro caso la actividad funciona por turnos. Si la conexión falla, la sesión sigue por turnos («La conexión de voz en directo no está disponible…»). El texto de cada frase se guarda igual que por turnos; lo comunica el navegador del alumno, con un máximo de 120 frases por minuto, y cada alumno puede abrir como mucho 6 conexiones en directo por minuto (por encima, la sesión sigue por turnos). En tiempo real no actúan la moderación de OpenAI ni el modo de micrófono de la actividad, y conversa el modelo de tiempo real, no el modelo de conversación de la actividad. Al cerrarse el intento, el servidor cuelga la llamada de OpenAI. El mantenedor declara probado OpenAI Realtime y no probado de extremo a extremo Gemini Live.

## Qué se envía a la IA y qué no
Se envía: el escenario (como texto sin formato), el rol del participante, nombre, papel y personalidad de los avatares, las restricciones adicionales de la actividad, el idioma, el nombre de pila del alumno, el texto de la conversación y, en la evaluación, además las instrucciones de evaluación del docente.
Antes de enviar texto del alumno se sustituyen sus apellidos, nombre de usuario y correo, cuando aparecen como palabras completas, por un código anónimo estable. No se detectan otros datos personales que el alumno mencione.
No se envía: audio en el modo por turnos, la descripción general de la actividad, notas de otras actividades ni datos de otros alumnos.
Los avatares responden en el idioma en que el alumno usa Moodle en ese momento. Los comentarios de la evaluación se redactan en el idioma forzado del curso; si no lo hay, en el del perfil del alumno; si no, en el del sitio.
El contenido que el alumno dice se trata como datos y no como órdenes. Si su texto parece un intento de manipular a la IA evaluadora, el intento queda marcado para revisión.

## Evaluación
Rúbrica fija: comunicación 30 %, adherencia al rol 25 %, manejo del escenario 25 %, calidad del lenguaje 20 %. Cada parte se puntúa de 0 a 100. El servidor recalcula la nota con esas cuatro puntuaciones y la convierte a la «Calificación máxima» de la actividad. No se pueden cambiar pesos ni criterios; las «Instrucciones de evaluación» solo orientan.
Solo cuentan las intervenciones del alumno; las frases de los avatares son contexto.
Si el alumno no dijo ninguna palabra, no se llama a la IA: nota 0, comentario estándar y aviso para revisión.
Avisos que obligan a revisión del profesor aunque la publicación sea automática: el alumno no dijo nada; habló menos de 20 palabras; texto con apariencia de manipulación; rúbrica incompleta (en ese caso la nota es la estimación global de la IA). La IA también puede añadir avisos propios por motivos graves, que igualmente llevan a revisión.
Si la evaluación falla, el intento vuelve a «Pendiente de evaluación» y se reintenta en segundo plano. Una evaluación atascada en «Evaluándose» más de 30 minutos puede volver a tomarse.

## Publicación de notas
Cada intento calificado queda «En revisión» o «Publicado». Con «Revisión del profesor antes de publicar» activada (o con aviso), queda en revisión y se avisa a los profesores con permiso para calificar. Sin ella y sin avisos, se publica sola y se avisa al alumno si la actividad lo tiene marcado.
El administrador puede bloquear este ajuste para todo el sitio; entonces manda su valor también en actividades ya creadas.
Al libro de calificaciones va la mejor nota entre los intentos publicados. Las notas en revisión no llegan al libro.
En «Entregas» el profesor puede: leer la conversación y las estadísticas, ver avisos y desglose, recalcular la evaluación, cambiar nota y comentario, guardar sin publicar, publicar, retirar una nota publicada y borrar un intento (devuelve ese intento al alumno).
Recalcular sustituye la evaluación anterior; si corresponde revisión, una nota ya publicada vuelve a «En revisión» y sale del libro de calificaciones. Un intento calificado que ya no tiene conversación guardada (el alumno retiró su consentimiento) no se puede recalcular: el botón no aparece y, si se intenta, se lee «Este intento no tiene ninguna conversación guardada…»; la nota se conserva y el profesor puede seguir cambiándola a mano.
Si el docente cambia la «Calificación máxima» cuando ya hay intentos, las notas guardadas de esa actividad se convierten a la nueva escala y el libro de calificaciones se actualiza. Las actividades cuya escala se cambió con una versión anterior a la 1.1.1 no se corrigen solas.

## Consentimiento y datos guardados
Se guarda: el texto de cada turno, la evaluación, la nota, los comentarios, fechas y quién calificó. No se guarda audio.
El alumno puede retirar el consentimiento cuando no tiene una sesión en curso ni en evaluación. Se borran sus conversaciones y los comentarios y desgloses de la IA de todos sus intentos en esa actividad; se conservan el número de intentos gastados y las notas. Después debe aceptar de nuevo el aviso para ver la actividad.
El plugin se integra con las herramientas de privacidad de Moodle (exportación y borrado) y con copia de seguridad, restauración y reinicio de curso (casillas para borrar intentos y excepciones).

## Tareas en segundo plano y avisos
- Cada 5 minutos se cierran las sesiones «En curso» cuyo tiempo acabó (más 45 segundos de margen) y se encarga su evaluación.
- La evaluación en segundo plano se reintenta si falla.
- Avisos de Moodle: «Calificación de AI Roleplay publicada» (al alumno) y «Sesión de AI Roleplay lista para revisión» (a profesores). De fábrica, por notificación web y correo.
Sin cron, las sesiones abandonadas no se cierran y las evaluaciones que no pidió el navegador no se hacen.

## Permisos y roles (valores de fábrica)
| Permiso (nombre en pantalla) | Estudiante | Profesor sin edición | Profesor | Gestor |
|---|---|---|---|---|
| Ver la actividad AI Roleplay | sí | sí | sí | sí |
| Participar en una sesión de juego de roles | sí | impedido | impedido | impedido |
| Ver todas las entregas | no | sí | sí | sí |
| Calificar entregas | no | sí | sí | sí |
| Gestionar excepciones de usuarios y grupos | no | no | sí | sí |
| Añadir una actividad AI Roleplay | no | no | sí | sí |
Consecuencia: un profesor no puede hacer la sesión; para probar hace falta una cuenta con rol de estudiante. Los invitados no pueden ver la actividad.
Con grupos separados, un profesor sin acceso a todos los grupos solo ve, califica y recalcula a los alumnos de sus grupos.

## Resumen de actividades del curso (Moodle 5.0 o posterior)
Desde la 1.1.2 la página de resumen de actividades del curso (en el curso, «Actividades» y luego AI Roleplay) muestra columnas propias en vez del aviso «Información no disponible». En Moodle 4.5 esa página no existe.
- Profesorado (con «Ver todas las entregas»): «Cierre» (fecha de cierre de la actividad o «-»), «Estudiantes que completaron» (alumnos matriculados con permiso de participar que tienen al menos un intento terminado, es decir, pendiente de evaluación, evaluándose o calificado, sobre el total de esos alumnos), «Pendientes de revisión» (intentos calificados que siguen «En revisión») y «Acciones», un botón a «Entregas» que dice «Calificar» si hay pendientes y el usuario puede calificar, y «Ver» si no.
- Con grupos separados, quien no tiene acceso a todos los grupos solo cuenta a los alumnos de sus grupos; si no está en ningún grupo, ve 0.
- Alumnado (con «Participar en una sesión»): «Cierre» (la fecha de la actividad, no la de su excepción), «Estado» de su último intento (un intento calificado aún no publicado aparece «En revisión») e «Intentos usados» sobre el máximo que le corresponde con sus excepciones (solo el número si es ilimitado).
- La columna de calificación la pone Moodle, no el plugin.
