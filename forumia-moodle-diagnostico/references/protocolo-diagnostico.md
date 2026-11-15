# Protocolo de diagnóstico de Forumia

## Ficha mínima
Pedir solo lo que haga falta para la consulta. No pedir claves ni acceso de administrador.
- Versión de Moodle y de Forumia; proveedor de IA y modelo elegidos.
- Estado de la licencia tal como lo muestra la página de ajustes.
- ¿Se ejecuta el cron? (aviso en Administración del sitio › Servidor › Tareas, o última ejecución de las tareas de Forumia).
- Configuración del foro: habilitado, cuenta elegida, modo, retraso, límites por foro y por usuario, calificación (modo y horas), reactivación (días, repetición, fecha límite).
- Ajustes del sitio: límite global activado y su valor; «Usuario IA predeterminado del sitio» relleno o no.
- El caso: quién publicó (rol en el curso, no el nombre), fecha y hora, si abrió tema o respondió, qué se esperaba y qué ocurrió.
- Notificaciones recibidas por los administradores con el prefijo «Forumia:».
- Para calificación: tipo de calificación del foro, nota máxima, método de calificación, y lo que muestra la página de sugerencias.
- Si el curso fue restaurado, duplicado o importado recientemente.
Los mensajes de estudiantes deben llegar anonimizados.

## Dónde mirar cada evidencia
| Evidencia | Dónde |
|---|---|
| Estado de licencia | Página de ajustes de Forumia; aviso en la configuración del foro |
| Tareas y sus errores | Tareas programadas («Ejecutar ahora» y registros de la tarea); las respuestas inmediatas aparecen como tarea puntual «Forumia – Respuesta de IA» |
| Desactivación global o de un foro | Notificaciones de los administradores |
| Peticiones gastadas hoy | No hay pantalla; se deduce contando las respuestas del asistente del día en el foro |
| Rol del autor | Participantes del curso |
| Nota actual y sugerida | Página de sugerencias; calificador del foro |

## Árbol: el asistente no responde a nadie
1. Cron parado o muy espaciado → comprobar el aviso de cron y la hora de la última ejecución. Sin cron no hay ninguna función.
2. Licencia: prueba agotada, clave no válida para esta dirección o caducada → estado en ajustes y aviso en el foro.
3. Parada general tras clave rechazada → buscar la notificación «el proveedor de IA ha rechazado la clave de API» y mirar si la casilla «Deshabilitado en todo el sitio» está marcada en los ajustes. Se reanuda al guardar una clave distinta o al desmarcar la casilla; si vuelve a marcarse sola, la clave sigue siendo rechazada. En 1.8.2 y anteriores no existe la casilla: recomendar actualizar.
4. Pausa de una hora por exceso de frecuencia → ¿volvió a funcionar solo pasado un rato? Revisar el plan del proveedor.
5. Falta la clave del proveedor seleccionado (se cambió de proveedor sin poner su clave).
6. Endpoint cambiado a una dirección no permitida (solo OpenAI).
7. Modelo que no devuelve texto → en 1.8.2 y anteriores era probable con los modelos que razonan de Gemini o DeepSeek; en 1.8.3 se amplió su presupuesto. Si persiste, probar el modelo económico cambiando solo el modelo.
8. Foro no habilitado, o en modo Diario cuando se espera respuesta inmediata.
9. Foro deshabilitado automáticamente por falta de cuenta → notificación «el asistente se ha desactivado en un foro».
10. Límite del foro o del sitio agotado ese día.

## Árbol: responde a unos y a otros no
1. Quien no recibe respuesta es docente, gestor o administrador, o no está matriculado → comportamiento previsto. Probar con una cuenta de estudiante.
2. Tiene un rol de profesorado en el curso además del de estudiante → no se le responde.
3. Rol personalizado: se excluyen los roles estándar de profesorado y gestión asignados en el curso y, desde 1.8.3, los roles creados a partir de ellos. Un rol docente asignado solo en la categoría o en el sistema no excluye por sí mismo, pero quien no está matriculado tampoco recibe respuesta.
4. Ya recibió hoy su cupo → «Límite diario de peticiones por usuario» (1 de fábrica).
5. El límite del foro o del sitio se agotó a partir de cierta hora → los posteriores se quedan sin respuesta, sin recuperación.
6. El mensaje se publicó durante una pausa o desactivación.
7. Retraso de una hora activado: aún no ha pasado la hora.
8. Versión anterior a 1.8.2: no se respondía a quien abría un tema nuevo, solo a las respuestas dentro de un tema.

## Árbol: no llega el resumen diario
1. Modo del foro distinto de Diario, o foro no habilitado.
2. No hubo mensajes de estudiantes en las 24 horas anteriores a la ejecución.
3. La tarea no se ejecutó, o su horario se cambió.
4. Solo en 1.8.2 y anteriores: si ese día ya había una petición anotada en el foro antes del resumen (por ejemplo, una evaluación para nota de madrugada), el resumen se omitía. Corregido en 1.8.3; en versiones anteriores, mover la hora del resumen o de la calificación.
5. Límites agotados, pausa o desactivación.
6. El resumen se publicó, pero dentro del debate del último mensaje de estudiante, no en un tema nuevo: buscarlo ahí.

## Árbol: calificación por IA
1. No aparece el enlace de sugerencias → la función está desactivada en el foro y no hay evaluaciones guardadas, o el usuario no puede calificar.
2. No hay sugerencias → asistente no habilitado en el foro; no han pasado las horas desde el primer mensaje; la tarea horaria no corre; límite del foro o del sitio agotado; el foro dejó de cumplir los requisitos de calificación; el estudiante no cuenta como estudiante.
3. Modo Automática y no se aplica → el estudiante ya tenía nota; el docente que activó el modo ya no puede calificar o fue suspendido; mirar la página de sugerencias.
4. «La IA no pudo calificar a este estudiante» → respuesta no válida del modelo; no se reintenta; calificar a mano.
5. Nota que parece baja porque el estudiante escribió después → la evaluación se hizo antes; no hay reevaluación.
6. No deja aceptar una sugerencia («no es válida para la calificación máxima actual») → la nota máxima del foro cambió tras la evaluación; descartar y calificar a mano. En 1.8.2 y anteriores se aplicaba sin reescalar: revisar las notas ya aceptadas.
7. No deja guardar el modo → mensajes de requisitos del foro o de permiso para calificar.

## Árbol: reactivación
1. No reactiva → función o asistente no habilitados; fecha límite (propia o del foro) ya pasada; aún no se cumplen los días; el asistente intervino hace menos de los días de repetición; límites agotados; la tarea diaria no corre.
2. Reactiva demasiado o en debates antiguos → revisa todos los debates; poner fecha límite, subir días de repetición o desactivar.
3. Foro con respuestas privadas de docentes → desde 1.8.3 no se envían a la IA ni se contestan. En 1.8.2 y anteriores sí formaban parte del contexto: recomendar actualizar antes de activar la reactivación.

## Árbol: cuenta del asistente
1. La lista del foro está vacía → no hay cuenta predeterminada ni cuentas con el permiso a nivel de sistema.
2. La cuenta no aparece → suspendida, borrada, permiso asignado en un curso o categoría en lugar de en el sistema, o nombre de usuario mal escrito en el ajuste.
3. Tras restaurar o duplicar un curso → en el mismo sitio y con la cuenta aún designada, el asistente sigue habilitado (desde 1.8.3). En otro sitio, con una cuenta que ya no está designada, o en 1.8.2 y anteriores: asistente deshabilitado y sin cuenta en los foros; volver a elegir y habilitar.

## Cierre
Clasificar cada causa como confirmada, probable o no comprobable. Proponer el ajuste según references/ajustes-y-pruebas.md. Si hay que escalar, redactar la solicitud al mantenedor con pasos reproducibles y sin datos personales.
