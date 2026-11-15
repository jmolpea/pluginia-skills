# Funcionamiento verificado de Peer Review Studio 1.0.1

Base: revisión estática del código que declara la versión 1.0.1 (versión interna 2026111500, Moodle 4.5 a 5.3), el 15-11-2026. No se ejecutó Moodle ni se comparó con el ZIP instalado. Todo lo que sigue es hecho verificado en el código salvo donde se indica «hipótesis» o «estimación».

## Qué es
Actividad de Moodle de evaluación entre pares. Cada alumno entrega un trabajo, revisa con una rúbrica los trabajos de otros alumnos que el plugin le asigna y recibe comentarios anónimos y una nota. El tutor supervisa desde un panel. Opcionalmente, la IA del sitio da una segunda opinión.
No tiene licencia, clave ni ajustes propios a nivel de sitio: la página de administración solo informa de si la IA está disponible y enlaza a la prueba.

## Modos y fases
- Programado por fechas: fase Entrega hasta «Cierre de entregas» (si hay «Apertura de entregas», no se puede entregar antes); fase Revisión hasta «Fecha límite de revisión»; después, fase Feedback. No existen las fases Asignación ni Cerrada.
- Manual: la fase la elige el docente en «Fase manual» (Entrega, Asignación, Revisión, Feedback, Cerrada) abriendo la configuración y guardando. Las fechas se ignoran.
- Abierto / autoformativo: no hay fases; siempre se puede entregar, se empareja continuamente y se revisa en cuanto hay algo asignado. El autor ve su feedback cuando su entrega llega a «Revisiones completas».
Cuándo se emparejan revisores: Programado, solo en la fase Revisión (tras el cierre); Manual, en Asignación y Revisión; Abierto, siempre.
Cuándo se puede revisar: Programado y Manual, solo en la fase Revisión; Abierto, siempre.
Cuándo se ve el feedback: Programado, tras la fecha límite de revisión; Manual, en Feedback y Cerrada; Abierto, por entrega, al completarse sus revisiones.

## Entrega
Un alumno tiene una única entrega por actividad. Según «Tipo de entrega» lleva ficheros, texto en línea o cualquiera de los dos.
Se puede editar mientras la fase admita entregas y la entrega no tenga ningún revisor asignado ni revisión recibida. Con el primer revisor asignado queda congelada; en modo Abierto esto puede ocurrir segundos después de entregar.
Al entregar por primera vez se envía la confirmación al autor. Editar no reenvía la confirmación.
Los ficheros se sirven siempre como descarga y solo al autor, a los revisores asignados (con revisión abierta o completada) y a los tutores que pueden ver a ese alumno.

## Estados de una entrega (se calculan solos)
Entregada: sin cola ni revisores. Esperando revisores: en cola de emparejamiento. En revisión: tiene revisores asignados y ninguna revisión enviada. Revisada parcialmente: alguna revisión, menos que el objetivo. Revisiones completas: alcanzó el objetivo, o la calificó la IA de respaldo.
El estado describe solo lo que la entrega ha recibido; lo que su autor revisa a otros se muestra aparte.

## Emparejamiento de revisores
Solo son candidatos los alumnos que ya han entregado en esa misma actividad, siguen matriculados y activos, y tienen permiso para revisar. Quien no entrega no revisa.
Nunca se asigna la propia entrega ni una entrega que ese revisor ya tuvo asignada antes, aunque se le retirase.
Si «Evitar revisiones recíprocas» está marcado, no se asigna a A la entrega de B mientras B tenga asignada (o haya hecho) la de A.
«Modo del grupo de revisores»: cualquiera, solo quien comparte algún grupo con el autor, o solo quien no comparte ninguno. Se usan los grupos del curso, limitados al agrupamiento de la actividad si lo tiene. Con «mismo grupo», un autor sin grupo no tiene candidatos.
Siempre se elige a los candidatos con menos revisiones asignadas hasta cubrir el «Objetivo de revisiones recibidas por entrega». Desde 1.0.1 hay dos formas de recorrer la cola. Sin regla de grupos ni de recíprocas (la configuración de fábrica), toda la cola se reparte junta: un revisor por entrega en cada vuelta y, a igualdad de carga, primero quienes entregaron después del autor; así la carga queda igualada. Con «mismo grupo», «grupos distintos» o «Evitar revisiones recíprocas», el reparto sigue siendo secuencial, entrega a entrega por orden de llegada (a igualdad, menos retiradas y entrega más antigua).
En los dos casos cada entrega recibe el mismo número de revisores, y las asignaciones que ya existen nunca se cambian.
«Revisiones que cada alumno debe completar» no interviene en el reparto: no limita ni garantiza cuántas se asignan a cada alumno.
Con asignación automática desmarcada no se encola ni se reparte nada automáticamente; el tutor asigna desde la página de cada entrega.
El emparejamiento se ejecuta al entregar (si la fase lo permite), en la tarea programada, al guardar la configuración y con el botón «Emparejar revisores ahora». Solo una ejecución a la vez por actividad.
Al revisor se le avisa cuando ya puede empezar: al asignar si la fase es de revisión, o al abrirse esta.

## Revisión
El revisor ve el trabajo sin nombre del autor en pantalla (los ficheros pueden contener datos que lo identifiquen), elige un nivel por cada criterio, puede comentar cada criterio y debe escribir un comentario general.
Una revisión enviada es definitiva: no hay borrador ni edición posterior.
La revisión propone una nota: suma de (puntos del nivel elegido × peso) dividida por la suma de (puntos máximos del criterio × peso), aplicada a «Calificación máxima de la entrega». El nivel más bajo no vale cero salvo que tenga 0 puntos.
El autor ve las revisiones como «Comentarios del revisor N», sin identidad. El tutor ve quién escribió cada una.

## Seguimiento automático (tarea programada cada 10 minutos)
En cada pasada, por cada actividad con cola pendiente, revisiones abiertas o plazo de revisión vencido sin publicar: empareja, avisa a revisores pendientes de aviso, envía recordatorios, retira y reasigna, escala y, en Programado, publica el feedback.
Recordatorio: uno solo por revisión asignada, pasados los días configurados.
Reasignación: pasados los días configurados se retira la revisión (el revisor recibe aviso) y la entrega vuelve a la cola mientras no acumule más de 3 revisiones retiradas y siga necesitando revisores.
Reloj de inactividad: en Programado cuenta desde el cierre de entregas (o desde la asignación si es posterior); en Manual, desde que se avisó al revisor de que ya podía revisar, es decir, al abrirse la fase Revisión o al asignarle la revisión si es posterior (corregido en 1.0.1; antes contaba desde la asignación); en Abierto, desde la asignación. Solo corre mientras se puede revisar.
En Programado, al vencer la fecha límite de revisión se cancelan sin aviso las revisiones abiertas.

## Escalado y respaldo
Solo se escalan entregas con cero revisiones recibidas, sin revisiones abiertas, sin nota fijada por el docente y no escaladas antes, cuando ocurre una de estas cosas: terminó el plazo de revisión (Programado), se alcanzaron 3 revisiones retiradas, o la entrega lleva en cola más días que el umbral de reasignación.
Escalar significa: si el respaldo por IA está activo y disponible, encargar a la IA la nota de la entrega; si no, enviar a los tutores un resumen con los alumnos afectados. La entrega aparece en «Requiere atención».
En Manual, el escalado solo ocurre en las fases Asignación y Revisión. Una vez en Feedback o Cerrada, las entregas sin revisar ya no se escalan solas.
Una entrega con alguna revisión pero sin llegar al objetivo nunca se escala: ni aviso a tutores ni respaldo por IA. Desde 1.0.1, si además no le queda ningún revisor asignado mientras el emparejamiento está permitido, aparece en «Requiere atención» como «Revisada parcialmente; sin revisores pendientes».
Si un tutor asigna a mano o vuelve a emparejar, la entrega sale del estado escalado y el ciclo puede repetirse.

## Nota
Nota de la entrega: media de las notas propuestas por las revisiones recibidas. Con IA activa y nota de IA disponible: media de pares × (100 − peso) % + nota de IA × peso %. Sin ninguna revisión: sin nota, salvo respaldo por IA con nota de IA, que entonces vale al 100 %.
Nota de revisión: (revisiones hechas ÷ requeridas, con tope 1) × «Calificación máxima de revisión». Con IA activa y valoraciones disponibles, se multiplica por la calidad media (0–100 %) de sus revisiones.
Nota final: entrega + revisión. Si la entrega no tiene nota, no hay nota final aunque el alumno haya revisado. Si el docente fija una nota, esa es la final.
Al cambiar máximos, pesos, puntuaciones, número de revisiones o ajustes de IA y guardar, todo se recalcula.

## Publicación
La nota llega al libro de calificaciones solo cuando el feedback está publicado para ese alumno; antes, el libro muestra vacío. La nota fijada por el docente se publica siempre al momento.
El autor recibe un único aviso de «Feedback y nota disponibles».
En Programado la publicación la hace la tarea programada tras la fecha límite; sin cron, no se publica.

## Revisión por IA (opcional)
Usa el subsistema de IA de Moodle con la acción «Generar texto». El plugin no tiene clave, modelo ni conexión propia: proveedor, modelo, límites y registros son los del sitio.
Condiciones para que actúe: proveedor disponible, herramientas de IA permitidas en el curso (Moodle 5.1 o posterior), casilla activada en la actividad y política de IA aceptada por quien escribió el contenido.
Cuándo: tras cada revisión enviada, en segundo plano. Hace dos evaluaciones: la entrega revisada (una sola vez por entrega, a nombre del autor) y la calidad de esa revisión (a nombre del revisor). Ambas devuelven una nota de 0 a 100 y un comentario.
Qué se envía: instrucciones del docente (o las de fábrica), nombre y descripción de la actividad, rúbrica con pesos y niveles, texto de la entrega y de sus ficheros legibles, y, para valorar la revisión, los niveles elegidos y los comentarios del revisor. El contenido de alumnos va marcado como no fiable, con orden de no obedecerlo.
Qué no se envía: nombres, correos ni identificadores de usuarios. Si el alumno escribe datos personales en su trabajo, viajan con él.
Entregas no legibles (algún fichero que no es texto, .docx u .odt, texto vacío o demasiado largo): la IA no califica la entrega y no se reintenta. La revisión sí se valora, sin mostrar el trabajo a la IA.
Si el autor no ha aceptado la política, la evaluación queda en espera y se lanza cuando la acepta y abre la actividad.
Qué ve cada uno: el autor, la nota y el comentario de la IA sobre su entrega junto al feedback, con aviso de que es automática; el tutor, además, la valoración de cada revisión. El revisor no ve la valoración de sus revisiones.
Qué se guarda: nota y comentario de la IA por entrega y por revisión, y la fecha del intento. No se guarda la petición enviada ni la respuesta íntegra; el registro de uso de IA es el de Moodle.
Respaldo: si la IA no puede (política no aceptada, trabajo ilegible, fallos repetidos), se avisa a los tutores. Si el autor acepta la política después, el respaldo no se relanza solo.

## Avisos
Seis tipos, por notificación de Moodle y correo de fábrica: confirmación de entrega, revisión asignada, recordatorio, retirada de revisión, feedback y nota disponibles, y escalado a tutores. No se envían a usuarios suspendidos o borrados ni a quien no puede abrir la actividad.

## Permisos y roles
Estudiante: ver, entregar, revisar y ver su estado. Profesor sin edición, profesor y gestor: ver, panel del tutor, gestionar asignaciones, fijar notas y gestionar modo y fase. Añadir la actividad: profesor con edición y gestor.
La zona del alumno solo aparece a quien tiene asignados los permisos de alumno: un administrador o profesor no puede entregar ni revisar.
Con grupos separados, un tutor sin acceso a todos los grupos solo ve y recibe avisos de los alumnos de sus grupos.

## Privacidad, copia y reinicio
Exporta la entrega, el feedback recibido (sin identidad de revisores) y las revisiones escritas. Borrar a un autor elimina trabajo y ficheros; borrar a un revisor quita identidad y comentarios y conserva la nota propuesta.
La copia de seguridad incluye ajustes y rúbrica siempre, y entregas, revisiones y notas solo con datos de usuario. El reinicio de curso puede vaciar la actividad y desplaza las fechas.

## Corregido en 1.0.1 respecto a 1.0.0
- Modo Manual: recordatorios y retiradas ya no se adelantan por los días pasados en la fase Asignación.
- Reparto: con la configuración de fábrica la carga de revisiones queda igualada cuando se reparte una cola entera (por ejemplo, al cerrar las entregas en Programado).
- Entregas «Revisada parcialmente» sin nadie asignado: ahora se ven en «Requiere atención».
- Rúbrica: un peso menor que 0,1 o un criterio con etiqueta y sin niveles dan error en el formulario en lugar de cambiarse en silencio.
- Ayudas de recordatorio y reasignación: indican que en Manual el contador empieza al abrir la fase Revisión.
- Enlace al manual de configuración en los ajustes del sitio y en el formulario de la actividad.
Si el cliente tiene 1.0.0, estos comportamientos siguen presentes en su sitio: recomendar actualizar.

## Comportamientos conocidos de 1.0.1 que conviene tener presentes
Verificados leyendo el código; no reproducidos en Moodle para esta revisión.
- Con regla de grupos o de recíprocas, el reparto sigue siendo secuencial y puede dejar a algún alumno con menos revisiones asignadas que las requeridas y a otro con más. Rodeo: «Asignar manualmente».
- Modo Abierto: una entrega «Revisada parcialmente» que agota las reasignaciones sigue sin publicarse hasta completar el objetivo; no hay aviso por mensaje ni respaldo por IA, solo la fila en «Requiere atención». Rodeo: asignar a mano, bajar el objetivo o fijar la nota.
- El contador de revisiones retiradas de una entrega no se reinicia cuando un tutor vuelve a emparejar: tras 3 retiradas acumuladas, la siguiente revisión que caduque ya no se reasigna sola.
