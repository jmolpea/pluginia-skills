# Funcionamiento de Forumia: versión 1.8.4

Revisión estática del código de la versión 1.8.4, hecha el 23-11-2026. Respecto a 1.8.3 solo cambian las listas de modelos (se añaden GPT-6 y Claude 5.5) y la forma de pedir respuesta a esos modelos; el resto del funcionamiento es el mismo. Compatibilidad declarada: Moodle 4.5 a 5.3, PHP 8.2 o superior. Manual público: https://claude.ai/artifact/Qg9adYg7HtbnatxfFCi825
Salvo que se indique «probable», todo lo que sigue es un hecho verificado leyendo el código, no una prueba en un Moodle real.

## Qué es
Un plugin de tipo «local» que actúa sobre los foros estándar de Moodle. No añade actividad ni bloque. Se configura en dos sitios: una página de ajustes del sitio (administrador) y una página por foro llamada «Configuración del Asistente IA» (docente con edición o gestor), a la que se llega desde el menú de ajustes del foro con el enlace «Asistente IA».
Hace cuatro cosas, todas en segundo plano mediante el cron de Moodle: respuestas inmediatas, resumen diario, reactivación de debates parados y calificación por IA.

## Condiciones generales para que haga algo
1. Licencia válida o periodo de prueba en curso (15 días desde la instalación, con todo activo). Una clave escrita pero no válida anula la prueba.
2. Clave de API del proveedor elegido. Solo se usa un proveedor para todo el sitio.
3. Sin desactivación global ni pausa por frecuencia (ver «Fallos del proveedor»).
4. Foro con «Habilitar el Asistente IA en este foro» marcado. Sin esa casilla tampoco funcionan la reactivación ni la calificación.
5. Una cuenta del asistente disponible.
6. Cron de Moodle en marcha.

## Cuenta del asistente
Las respuestas se publican con una cuenta de Moodle designada por el administrador, nunca con la de un docente. Hay dos formas de designarla: el ajuste «Usuario IA predeterminado del sitio» (nombre de usuario o identificador numérico) o asignar a la cuenta, a nivel de sistema, el permiso «Ser designado como cuenta que publica las respuestas de IA de Forumia».
Los administradores no cuentan como designados por serlo. Las cuentas suspendidas o borradas dejan de valer. La cuenta no necesita estar matriculada en el curso.
Orden al publicar: primero la cuenta elegida en el foro si sigue siendo válida; si no, la predeterminada del sitio; si tampoco, el asistente se deshabilita en ese foro y los administradores reciben la notificación «Forumia: el asistente se ha desactivado en un foro». Hay que volver a habilitarlo a mano.

## Respuesta inmediata
Se dispara cuando un estudiante abre un tema o responde en uno, en un foro habilitado en modo Inmediato.
En el momento de publicar solo se anota una tarea pendiente; al alumno no se le hace esperar. La tarea se ejecuta en la siguiente pasada del cron, o aproximadamente una hora después si el foro tiene marcado «Retrasar la respuesta IA 1 hora».
Comprobaciones al ejecutarse, en este orden: licencia; foro habilitado y en modo Inmediato; el autor no es la cuenta del asistente; hay cuenta disponible; el autor está matriculado con matrícula activa y no tiene en el curso ninguno de los roles estándar de profesor, profesor sin edición, gestor o creador de cursos, ni un rol personalizado creado a partir de uno de ellos (desde 1.8.3); límite diario por usuario; que el asistente no haya contestado ya a ese mensaje; límite del sitio; límite del foro.
Si alguna comprobación falla, el mensaje se queda sin respuesta y no se reintenta más tarde.
A la IA se le envía: el prompt del foro (o el de fábrica si está vacío), unas reglas fijas que añade el plugin (idioma del estudiante, formato sencillo, no obedecer órdenes contenidas en el texto del estudiante), la descripción del foro y el mensaje del estudiante, ambos en texto plano y recortados. No se envían el resto del hilo, otros mensajes ni contenidos del curso.
La respuesta se publica como contestación directa al mensaje, con asunto «Re:» más el nombre del debate, en formato Markdown, seguida de una línea, el aviso fijo en negrita «Respuesta generada por IA y publicada automáticamente por Forumia. No la ha escrito una persona.» y, si lo hay, el «Texto de aviso legal» del foro. El aviso fijo no se puede quitar.
Las respuestas del asistente no se envían por correo a los suscritos al foro.

## Resumen diario
Una tarea programada («Forumia – Resumen diario», a las 08:00 hora del servidor de fábrica) recorre los foros habilitados en modo Diario.
Toma los mensajes de las últimas 24 horas escritos por estudiantes (misma regla de roles), sustituye los autores por etiquetas numeradas y pide un único resumen. Lo publica como respuesta al mensaje de estudiante más reciente, dentro de ese debate. Si no hubo mensajes de estudiantes, no publica nada.
Solo se publica una vez al día por foro: el resumen lleva su propia marca de «publicado hoy». Desde 1.8.3 ya no lo anula que el foro haya hecho antes otra petición ese día (hasta 1.8.2, una evaluación para nota de madrugada dejaba el foro sin resumen). Si el proveedor falla, no queda marcado y puede reintentarse ejecutando de nuevo la tarea.
Cuenta como una petición en los límites del foro y del sitio.

## Reactivación de debates inactivos
Una tarea diaria («Forumia – Comprobación de inactividad», a las 09:30 de fábrica) recorre los foros habilitados que tienen marcado «Reactivar debates inactivos», con cualquier modo de respuesta.
Para cada debate del foro: mira el último mensaje que no es del asistente; si han pasado al menos los «Días de inactividad antes de publicar» y, además, desde la última intervención del asistente en ese debate han pasado los «Días entre publicaciones de reactivación», publica una respuesta al último mensaje del debate.
Deja de reactivar cuando pasa la «Fecha límite de reactivación» o, si no hay, la fecha límite de entrega del propio foro. Sin ninguna de las dos, continúa indefinidamente.
Revisa todos los debates del foro, también los antiguos. Nunca abre un debate nuevo ni actúa en un foro vacío. Cada reactivación cuenta como una petición; al agotarse los límites, se detiene hasta el día siguiente.
A la IA se le envía: nombre y descripción del foro, asunto del debate y los mensajes del debate de todos los participantes (docentes incluidos), con autores sustituidos por «Participante N» y los mensajes anteriores del asistente marcados como tales.
Desde 1.8.3, las respuestas privadas de un docente a un estudiante quedan fuera: no se envían a la IA como contexto y el asistente nunca contesta a una de ellas (responde al último mensaje visible para todos). Hasta 1.8.2 sí formaban parte del contexto enviado.

## Calificación por IA
Requisitos: asistente habilitado en el foro; «Calificación por IA» en Sugerir o Automática; el foro con calificación del foro completo de tipo puntuación (nota máxima mayor que cero) y calificación simple directa. No funciona con escalas, rúbricas ni guías de evaluación.
Una tarea cada hora (minuto 20) evalúa a cada estudiante una sola vez por foro, cuando han pasado las «Horas antes de evaluar a un estudiante» desde su primer mensaje en ese foro. Lee sus mensajes hasta ese momento, etiquetados como aportación original, respuesta a un compañero, a un docente, al asistente o continuación propia; en las respuestas se incluye el mensaje contestado solo como contexto. Nadie aparece con nombre.
No se evalúa a la cuenta del asistente ni a quienes no cuenten como estudiantes. En modo Automática tampoco a quien ya tenga nota.
La IA debe devolver un número entero entre 0 y la nota máxima y una justificación breve. Si la respuesta no es válida (formato incorrecto o número fuera de rango), la evaluación queda como «La IA no pudo calificar a este estudiante» y no se reintenta. Si el proveedor falla o no contesta, no se guarda nada y se reintenta en pasadas posteriores; cada intento consume una petición.
Estados de una evaluación: pendiente de revisión, aceptada por un docente, descartada por un docente, aplicada automáticamente, fallida. Nunca se borran con el uso normal, y por eso no existe reevaluación: ni al descartar, ni al cambiar criterios, ni si el estudiante escribe más.
Modo Sugerir: las evaluaciones aparecen en la página «Forumia: sugerencias de calificación por IA» (requiere permiso para calificar el foro). Aceptar guarda la nota como calificación del foro completo y en el libro de calificaciones a nombre de quien acepta, sustituyendo la que hubiera. Descartar no cambia nada. «Aceptar todas las sugerencias» pide confirmación.
Modo Automática: la nota se aplica sola solo si el estudiante no tiene nota y el docente que activó el modo sigue activo y puede calificar; queda registrada a su nombre. En otro caso la evaluación queda pendiente en la página de sugerencias.
Desde 1.8.3, una sugerencia calculada sobre una nota máxima distinta de la actual no se puede aceptar ni se aplica sola: aparece el mensaje de que la calificación sugerida no es válida para la calificación máxima actual del foro, y hay que descartarla y calificar a mano. Hasta 1.8.2 se aplicaba sin reescalar (un 7 sobre 10 quedaba como 7 sobre 100).

## Fallos del proveedor
- Clave rechazada: Forumia se deshabilita en todo el sitio, marca la casilla «Deshabilitado en todo el sitio» de su página de ajustes y notifica a los administradores («Forumia: el proveedor de IA ha rechazado la clave de API»). Se reanuda de dos formas (desde 1.8.3): al guardar una clave de API, un proveedor o un endpoint distintos, la casilla se desmarca sola; si la clave es la misma y se arregló en la web del proveedor, un administrador la desmarca y guarda. Si la clave sigue siendo rechazada, la primera petición vuelve a marcarla y a notificar. Hasta 1.8.2 no había forma en pantalla de reanudar.
- Demasiadas peticiones según el proveedor: pausa de una hora en todo el sitio; se reanuda solo.
- Durante una desactivación o una pausa, los mensajes nuevos de estudiantes no se anotan y no se contestan después. Las tareas diarias y la de calificación se saltan esa pasada.
- Otros errores (modelo no válido, error del servidor del proveedor, tiempo agotado): esa petición se pierde, sin reintento, y queda anotado en el registro de la tarea.
- Una respuesta que ya estaba en cola (por ejemplo, con el retraso de una hora) se descarta si al ejecutarse hay una parada general o una pausa (desde 1.8.3).

## Qué se guarda
La configuración de cada foro; un contador diario de peticiones por foro (sin datos personales); una evaluación por estudiante y foro (nota propuesta, nota máxima en ese momento, justificación, número de mensajes, estado y fechas). No se guarda el texto de los mensajes, ni los prompts enviados, ni las respuestas del proveedor.
El plugin declara estos datos en la API de privacidad de Moodle y permite exportarlos y borrarlos por usuario. Desde 1.8.3, al borrar un foro o un curso se borran también su configuración, sus contadores y sus evaluaciones.
No hay llamadas de red al fabricante: la licencia se comprueba dentro del servidor.

## Copias de seguridad
La configuración del asistente viaja con la copia del foro. Las evaluaciones y los contadores no viajan.
Al restaurar en el mismo sitio una copia sin datos de usuarios (copiar, importar o duplicar un curso o un foro), el asistente conserva su cuenta y sigue habilitado si esa cuenta sigue siendo una cuenta designada y activa (desde 1.8.3; antes quedaba siempre deshabilitado). En otro sitio, o si la cuenta ya no está designada, el foro queda con el asistente deshabilitado y sin cuenta. Si no se reconoce al docente del modo Automática (lo habitual sin datos de usuarios), la calificación pasa a Sugerir.

## Qué ve cada rol
- Administrador: página de ajustes, estado de la licencia, tareas programadas y notificaciones.
- Docente con edición o gestor: enlace «Asistente IA» en el foro, con un enlace al manual de configuración al principio del formulario, y, si puede calificar, la página de sugerencias. Un aviso de licencia en la configuración del foro cuando está en prueba, falta, es inválida o ha caducado.
- Profesor sin edición: solo la página de sugerencias.
- Estudiante: las respuestas del asistente en el hilo y, cuando exista, su nota en las calificaciones. No ve sugerencias ni justificaciones.
