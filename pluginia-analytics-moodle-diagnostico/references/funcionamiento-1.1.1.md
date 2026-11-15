# Funcionamiento verificado: Pluginia Analytics 1.1.1

Revisión estática del 15-11-2026. Todo lo que sigue es un hecho leído en esa versión, salvo donde se indica «hipótesis» o «no verificado en ejecución».

## Qué es y dónde aparece
Plugin de tipo «local» para Moodle 4.5 a 5.3. No es una actividad ni un bloque: no se añade a los cursos.
- Ajustes del sitio: Administración del sitio › Extensiones › Extensiones locales › Pluginia Analytics (solo administradores con configuración del sitio).
- Informes del sitio: Administración del sitio › Informes: «Pluginia Analytics» (panel del sitio), «Analíticas por categoría», «Seguimiento de alumnos» y «Auditoría de preparación».
- En cada curso: menú Informes › «Pluginia Analytics» (página «Analíticas del curso»). Solo lo ven quienes tienen el permiso de ver las estadísticas del curso; el alumnado no.
- Configuración por curso: página «Mensajes automáticos», con el botón «Configurar mensajes automáticos» al final de la pestaña Resumen (bajo el panel de alumnos en riesgo cuando ese panel se ve). Desde 1.1.1 lo ve toda persona que puede configurar los mensajes, vea o no el panel.
- Enlace «Manual de configuración» (desde 1.1.1): al principio de los ajustes del sitio, en la página de mensajes del curso y junto a los botones del panel del curso.

## Cálculo de datos
- Una tarea programada horaria («Agregar datos analíticos») recalcula cada curso visible y el conjunto del sitio y guarda el resultado en la caché de Moodle. Los paneles leen esa copia.
- Si la copia de un curso no existe, el panel del curso la calcula al abrirse (más lento). El panel del sitio nunca calcula en pantalla: si no hay copia, muestra «Las analíticas del sitio se están preparando en segundo plano…» y encarga el cálculo a una tarea puntual.
- La copia caduca a las 3 horas. Si tiene más de 2 horas, el panel avisa «Los datos pueden estar desactualizados».
- «Actualizar datos» en un curso encarga el recálculo a una tarea puntual; no es inmediato.
- Cambiar ciertos ajustes (campos demográficos, umbral de supresión, umbrales de riesgo, alertas de comportamiento, ajustes de satisfacción, campo de horas) vacía la caché.
- Los cursos ocultos no se calculan en la tarea horaria ni aparecen en el panel del sitio.

## Embudo de participación (seis etapas)
Cuenta a toda persona con matrícula activa en el curso (método de matrícula activo y matrícula no suspendida), sin distinguir rol.
1. Matriculados: matrícula activa.
2. Iniciado: ha entrado al curso alguna vez (último acceso al curso o cualquier evento en el registro estándar).
3. Activos: dos o más actividades completadas.
4. 50% completado: al menos la mitad de las actividades con seguimiento.
5. Completado: todas las actividades con seguimiento.
6. Calificación emitida: completó el curso y su nota final alcanza la nota de aprobado (la del criterio de calificación de la finalización del curso o, si no hay, la «calificación para aprobar» del total del curso). Sin nota de aprobado vale 0.
«Actividad con seguimiento» = actividad visible, con seguimiento de finalización activado y que no se está borrando.
Porcentajes: Iniciado sobre Matriculados; Activos sobre Iniciado; las tres últimas sobre Activos.
Las cifras del sitio cuentan personas distintas; las de categoría suman cursos (una persona en dos cursos cuenta dos veces).

## Alumnos en riesgo y alertas de comportamiento
Se excluye siempre a quien ya completó el curso, a usuarios suspendidos o eliminados y a matrículas inactivas.
- Nunca accedió: matriculado desde hace más días que el umbral de inactividad y sin ningún acceso al curso.
- Inactivo: matriculado desde hace más días que el umbral, entró alguna vez, lleva más días que el umbral sin entrar y ha completado menos del porcentaje de progreso. Requiere que el curso tenga actividades con seguimiento; si no, nadie entra en este nivel.
- Vista, sin completar: abrió (evento de vista en el registro estándar) una actividad con seguimiento hace al menos N días, dentro de los últimos 90, y no la ha completado.
- Caída de actividad: en los 14 días anteriores a la última semana tuvo al menos 20 eventos, y en los últimos 7 días su actividad es al menos un X % menor que su media semanal de esos 14 días.
Las dos últimas dependen del ajuste del sitio «Alertas de comportamiento» y del registro estándar de Moodle.
Los umbrales de inactividad y progreso salen del sitio y cada curso puede sustituirlos; los de las alertas se fijan en cada automatización (curso), con valor de partida en la plantilla del sitio.
El panel lista los primeros 50 alumnos de cada grupo (los matriculados más antiguos primero, o la mayor caída primero) y añade «… y N más (no listados)». La cola de intervención y el mensaje manual en lote usan esa misma lista de hasta 50 por grupo. La exportación de alumnos en riesgo, desde 1.1.1, se calcula al descargarla e incluye a todos (en 1.1.0 solo los 50 listados).
El panel con nombres, su exportación y la cola exigen el permiso «Ver demografía, satisfacción y los nombres de los alumnos en riesgo» en el curso. El panel no distingue grupos separados.

## Mensajes automáticos
- Se activan por curso («Activar los mensajes automáticos»). Cada curso tiene cuatro automatizaciones, una por situación; de fábrica están encendidas «Nunca accedió» e «Inactivo» y apagadas las otras dos. Las plantillas del sitio no encienden nada.
- Una tarea diaria recorre los cursos visibles con los mensajes activados. El botón «Enviar mensajes ahora» hace lo mismo para un curso en el momento (también si está oculto) y anota el origen «Manual».
- Para cada alumno candidato se toma la primera automatización activada que le corresponde, en este orden: Nunca accedió, Inactivo, Vista sin completar, Caída de actividad. Recibe un solo mensaje.
- Plazo mínimo: no se envía si ese alumno recibió cualquier mensaje automático de ese curso dentro de los «Días mínimos entre mensajes». No existe un tope total: mientras siga cumpliendo la condición, recibe otro mensaje al vencer el plazo. Tampoco se tienen en cuenta las fechas de inicio o fin del curso.
- Antes de enviar se comprueba que el destinatario existe, no está suspendido y sigue matriculado.
- Desde 1.1.1 no se envía al personal del curso: quien tiene en ese curso el permiso de ver las estadísticas del curso (profesorado, gestores) se omite, aunque siga contando en el embudo y apareciendo en el panel. Un administrador del sitio matriculado como estudiante sí lo recibe. En 1.1.0 no existía este filtro.
- El envío se anota en el historial aunque algún canal de entrega de Moodle (por ejemplo, el correo) falle: el historial indica que el plugin lo entregó a Moodle, no que llegó al buzón.
- Texto: tres capas, gana la primera que exista: texto propio del curso, plantilla del sitio, texto incorporado. El incorporado se envía en el idioma del perfil de cada alumno (español, inglés, portugués de Brasil). Un texto propio se envía igual a todos, salvo bloques multiidioma. Si se guarda un texto idéntico al heredado, no se considera propio.
- La plantilla es texto plano; se respetan los saltos de párrafo y las direcciones web se convierten en enlaces. El aspecto (color, logotipo o nombre del sitio, botón «Ir al curso», firma, pie con el motivo y el enlace a preferencias) lo añade el plugin según los ajustes del sitio.
- Entrega: notificación de Moodle del tipo «Recordatorios del curso (alumnos inactivos o atascados)», activada de fábrica en web y correo. Cada alumno puede desactivarla en sus preferencias. El remitente es el usuario «no responder» del sitio.
- Cada envío se anota (curso, alumno, automatización, origen, fecha). El historial muestra los 20 últimos.
- «Qué pasó después de los mensajes»: cada alumno cuenta una vez, desde su primer mensaje, en el nivel más alto alcanzado después: Completó el curso, Avanzó, Volvió o Aún sin volver. Es descriptivo, no causal.
- «Redactar con IA» (si hay IA configurada): envía al proveedor el nombre del curso, el tipo de destinatario, la lista de marcadores, el idioma y el texto actual de la plantilla. No envía datos de alumnos. No guarda nada hasta que se guarda el formulario.
- Mensaje manual desde el panel («Enviar mensaje» con alumnos seleccionados): es un mensaje personal de Moodle del propio docente; no se anota en el historial ni cuenta para el plazo mínimo; usa cinco marcadores propios.

## Resumen semanal a tutores
Opción del curso «Enviar un resumen semanal de este curso a sus tutores» (en 1.1.0 se llamaba «Enviarme un resumen semanal de este curso»; el comportamiento es el mismo). La tarea semanal lo envía a todas las personas con el permiso de configurar los mensajes en ese curso (también gestores con ese permiso heredado), no solo a quien lo activó. Contiene: nuevas matrículas, finalizaciones, mensajes enviados, alumnos que volvieron tras un mensaje (7 días) y alumnos en riesgo. Si todas las cifras son cero, no se envía. Con IA configurada añade un «Apunte de la IA», desde 1.1.1 en el idioma de cada destinatario (una llamada por curso, semana e idioma distinto entre los destinatarios, fuera del límite por usuario). Solo cursos visibles.

## Asistente de IA («Pregunta a Pluginia»)
- Aparece en la pestaña Resumen del curso y en el panel del sitio solo si hay proveedor y clave.
- En cada pregunta se envía al proveedor elegido: la pregunta, los turnos anteriores de la conversación y un resumen de cifras agregadas (recuentos, porcentajes, medias, nombres de cursos y actividades, países y ciudades).
- Nunca se envían nombres, correos ni identificadores de alumnos. Discapacidad y grupo étnico no se envían nunca. Demografía y satisfacción solo se incluyen si quien pregunta puede ver esas pestañas. Los grupos pequeños se omiten.
- La conversación no se guarda en Moodle; vive en la página abierta.
- Proveedores: Anthropic Claude, OpenAI, Google Gemini, DeepSeek. Una sola clave de API para el proveedor elegido.
- Errores visibles: «El asistente de IA no está configurado…», «Ha alcanzado el límite de preguntas a la IA por hora…», «Servicio de IA no disponible temporalmente…» (cualquier fallo del proveedor: clave, saldo, modelo, red, respuesta vacía o rechazada).

## Otras funciones
- Demografía: desgloses por los campos de perfil asignados; país y departamento pueden usar los campos propios de Moodle.
- Geografía: país y ciudad por usuario, obtenidos por este orden: base GeoIP configurada en Moodle (con la última dirección de conexión, que no se guarda), país y ciudad del perfil, campo de perfil asignado. El mapa carga su fondo desde OpenStreetMap en el navegador de quien lo mira.
- Satisfacción: NPS de una encuesta del plugin adicional Questionnaire y ganancia de conocimiento entre prueba inicial y final, detectadas por palabras clave en el nombre; hay valores manuales en los ajustes.
- Horas de formación impartidas: horas del curso (campo personalizado numérico) × personas que lo completaron.
- Panel del sitio: filtros, evolución de 12 meses, cohortes, clasificación de cursos, comparación de 2 a 5 cursos, exportaciones.
- Exportación semanal programada por correo a destinatarios configurados (desde 1.1.1 la dirección se reconoce sin distinguir mayúsculas).
- Seguimiento de alumnos: estado, último acceso, progreso y nota de una persona en todos sus cursos visibles.
- Auditoría de preparación: comprobaciones con estado Correcto, Aviso o Error y enlace para corregir.

## Licencia
- 15 días de evaluación completa desde la instalación, sin clave.
- La clave se valida sin conexión y está ligada a la dirección exacta del sitio (cuenta http frente a https; se ignora la barra final).
- Clave con caducidad: es válida durante todo el día de la fecha indicada (desde 1.1.1); después sigue funcionando 30 días con aviso. Clave no válida: funciona mientras quede evaluación.
- Sin licencia en vigor: los paneles muestran un aviso en lugar de cifras y las tareas de cálculo, mensajes, resumen y exportación no hacen nada. No se borra ningún dato ni ajuste.

## Qué guarda el plugin
- Último país y ciudad conocidos por usuario matriculado, con su origen y fecha.
- Ajustes de mensajes de cada curso y quién los guardó.
- Automatizaciones propias de cada curso y plantillas del sitio, y quién las guardó.
- Registro de mensajes automáticos enviados.
- Ajustes del sitio, incluida la clave de API, en la configuración de Moodle.
Todo ello está declarado para las solicitudes de exportación y borrado de datos de Moodle. Al eliminar un usuario o un curso se borran sus datos del plugin.

## Permisos de fábrica
| Permiso (nombre en pantalla) | Roles |
|---|---|
| Ver el panel de analíticas del sitio | Gestor, creador de cursos |
| Ver las estadísticas del curso | Gestor, profesor, profesor sin edición |
| Ver demografía, satisfacción y los nombres de los alumnos en riesgo | Gestor |
| Configurar y lanzar los mensajes automáticos a alumnos | Gestor, profesor con edición |
| Ver el progreso de un alumno en todos sus cursos | Gestor |
| Configurar Pluginia Analytics | Gestor |
Consecuencia: de fábrica un profesor con edición puede configurar mensajes y ve el botón que lleva a esa configuración, pero no ve el panel de alumnos en riesgo con nombres ni la cola de intervención. En 1.1.0 tampoco veía el botón.
Los enlaces a la página de ajustes del plugin solo se ofrecen a quien puede abrirla (administradores con configuración del sitio).
