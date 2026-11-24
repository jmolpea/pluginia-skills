# Funcionamiento de Pluginia Connect: versión 0.2.0

Revisión estática del código de la versión 0.2.0, hecha el 24-11-2026 y revisada el 25-11-2026. Madurez declarada: alfa. Compatibilidad declarada: Moodle 4.5 a 5.3, PHP 8.1 o superior. Manual público: https://claude.ai/artifact/XSFJRPaBcavfAJyFBo7K2Y
Salvo que se indique «probable» o «según la documentación del proyecto», todo lo que sigue es un hecho verificado leyendo el código, no una prueba en un Moodle real.
El plugin solo trae la interfaz en inglés: los nombres entre comillas son los que salen en pantalla, con su traducción entre paréntesis.

## Qué es
Un plugin de tipo «local» que permite a una persona conectar un asistente de IA (Claude, ChatGPT o Microsoft 365 Copilot Cowork) a su propia cuenta del sitio. El asistente puede entonces pedir al sitio que ejecute acciones de una lista cerrada, en nombre de esa persona y dentro de sus permisos.
No añade actividades ni bloques. No usa los tokens de servicios web de Moodle ni necesita que los servicios web estén activados. No lleva comprobación de licencia dentro del plugin. Al registrar el sitio en la pasarela, la clave de licencia es opcional y hoy no hace falta.
El asistente nunca recibe la contraseña: la persona entra en el sitio como siempre y autoriza la conexión en una página del propio sitio.

## Estado de esta versión
- Alfa: no es para sitios en producción. Sitios de prueba y datos inventados.
- La pasarela Pluginia Connect (connect.pluginia.es) está en servicio desde el 24-11-2026 y es gratuita por ahora: el registro no exige clave de licencia (el campo existe y se deja vacío). Todavía no figura en los directorios de los asistentes, no admite Copilot Cowork y, según la documentación del proyecto, ningún asistente real se ha conectado aún a través de ella.
- Según la documentación del proyecto, solo consta una primera conexión real de prueba desde Claude (web) en modo directo, y ninguna desde ChatGPT ni Copilot Cowork; las reglas de servidor para la raíz del dominio no se han probado contra ellos.
- Las notas de la versión la marcan como no publicada todavía.

## Qué puede y qué no puede hacer un asistente conectado
Cuatro reglas explican casi todo:
1. Decide el sitio. Cada llamada se comprueba en el sitio, en ese momento, contra los permisos reales de la persona en el curso, la categoría o el sitio de que se trate.
2. Cada capa solo resta. Lo que puede hacer una conexión es la intersección de: permisos de la persona en Moodle, perfil elegido al conectar, permisos concedidos en la página de consentimiento (solo lectura, o lectura y cambios) y política del sitio (ajustes y «Actions by profile»).
3. Lista cerrada. Solo existen las 31 acciones del catálogo: 22 que leen y 9 que cambian algo. No hay ninguna acción genérica del tipo «ejecuta esta función» o «ejecuta esta consulta».
4. Apagado de fábrica. Al instalar, el conector y los dos modos de conexión están apagados. Las acciones de cambio siguen apagadas hasta que el administrador enciende cada una para cada perfil, y ninguna se aplica la primera vez que se pide.

Lo que no hace:
- No actúa sobre otros plugins, sobre actividades distintas de las que cubre el catálogo ni sobre contenidos fuera de él. De los foros solo lee y publica en el foro de avisos del curso. No lee cuestionarios, mensajes privados, bases de datos, wikis ni contenido de archivos (de un archivo adjunto devuelve nombre, tamaño y tipo, nunca el contenido ni un enlace de descarga).
- No borra nada: ni cursos, ni usuarios, ni matrículas, ni calificaciones, ni entregas. Ninguna acción del catálogo borra. No existe la baja de matrícula: una matrícula se suspende o se reactiva. Un aviso publicado o un mensaje enviado no se pueden retirar desde el asistente.
- Todo se ejecuta y se registra como la persona conectada. Ninguna acción actúa en nombre de otro usuario ni deja constancia a nombre de otro.
- No concede nada que la persona no pueda hacer ya en el sitio, y un perfil alto no da más permisos: es solo un tope.
- No deja crear una conexión a un invitado, a una cuenta suspendida, sin confirmar o sin acceso, ni a un administrador que ha entrado «como» otro usuario.

## Modo directo y modo pasarela
- Modo directo («Allow direct connections», permitir conexiones directas): el asistente habla con el sitio. No interviene ningún servidor de Pluginia; el único tercero es el proveedor del asistente. Solo pueden conectar las aplicaciones cuyas direcciones de retorno están en «Allowed return addresses» (de fábrica, las de Claude y ChatGPT). Microsoft 365 Copilot Cowork no puede conectar en modo directo: su dirección de retorno es común a todos los complementos de Microsoft 365 y el plugin la rechaza siempre, diga lo que diga la lista.
- Modo pasarela («Allow the Pluginia Connect gateway», permitir la pasarela): una única dirección de conexión para todos los sitios registrados, pensada para los directorios de los asistentes. Exige registrar el sitio en «Gateway registration»; por ahora es gratuita y el campo de clave de licencia se deja vacío. La pasarela transporta peticiones y respuestas, no guarda su contenido y no puede conceder lo que el sitio no concede. Es la única vía prevista para Copilot Cowork, que todavía no está disponible. En servicio y gratuita por ahora; sin conexión real de un asistente comprobada todavía.
- El conector necesita «Enable the connector» encendido y al menos un modo. Cada conexión pertenece al modo con el que se creó: si ese modo se apaga, sus conexiones dejan de funcionar aunque el otro siga encendido.
- La dirección que hay que dar al asistente en modo directo no aparece en ninguna pantalla del plugin: consultarla en el manual.

## Requisitos del servidor
- HTTPS con certificado de una autoridad reconocida. Sin HTTPS el conector rechaza las peticiones («HTTPS is required.»).
- El servidor web debe pasar a PHP la cabecera Authorization. Sin ella los asistentes no pueden autenticarse.
- El servidor web debe pasar a PHP los argumentos de ruta (la misma configuración que Moodle necesita para los «slash arguments»). Sin ellos los asistentes no encuentran los metadatos de inicio de sesión del sitio.
- Cron cada minuto. Las tareas programadas del plugin borran códigos, tokens y cambios pendientes caducados y los registros antiguos.
- Extensión sodium de PHP.
- Reloj del servidor en hora: de él dependen las caducidades.
- Con varios servidores web: un almacén de caché compartido (por ejemplo Redis) para los contadores de límites; si no, cada servidor cuenta por su lado.
- Sin dependencias externas ni cambios en el núcleo de Moodle.
La página «Diagnostics» (diagnóstico) comprueba todo lo anterior; ver references/configuracion.md.

## Cómo se crea una conexión
1. La persona inicia la conexión desde su asistente.
2. El sitio le pide que entre como siempre (incluida la autenticación en varios pasos si el sitio la usa).
3. El sitio muestra «Connect an AI assistant» (conectar un asistente de IA) con: «Asking for access» (quién pide acceso), «You will be sent back to» (a dónde se la devolverá), «Profile for this connection» (perfil), «Access level» (nivel de acceso: «Read only», solo lectura, marcado de fábrica; «Read and changes», lectura y cambios, solo si se le puede ofrecer), la lista de acciones que podrá usar el asistente con cada perfil, el aviso de la institución y el enlace a su política de privacidad si están configurados.
4. Al pulsar «Allow» (permitir) se crea la conexión. Nunca hay aprobación silenciosa: la página se muestra siempre, también a quien ya conectó antes.
5. La persona recibe la notificación «An AI assistant was connected to your account» con un enlace para desconectar si no ha sido ella.
«Read and changes» solo se ofrece si no está activo «Read-only mode», si la persona tiene el permiso «Allow AI assistant connections to request changes» en al menos un curso dentro del alcance del sitio, si hay alguna acción de cambio encendida en «Actions by profile» para alguno de los perfiles que esa persona puede elegir (sin ninguna, la opción no añadiría nada y no se muestra) y, con Copilot Cowork, si el sitio no lo ha limitado a solo lectura.
Lo concedido queda fijado en ese momento: solo entran los grupos de permisos que tienen alguna acción encendida para ese perfil. Si el administrador enciende después una acción de un grupo que la conexión no tiene, hay que desconectar y volver a conectar.
Qué pide el asistente al conectarse lo decide el ajuste «Permissions an assistant asks for when it connects». El sitio anuncia una lista de grupos de permisos y asistentes como Claude piden exactamente esa lista, una sola vez, sin ampliarla después. La página de consentimiento solo puede conceder lo que el asistente pidió, recortado por el perfil y el nivel de acceso que elige la persona.
- Con el valor de fábrica, «Everything switched on in this site (recommended)», el sitio anuncia la lectura básica más todos los grupos que tienen alguna acción encendida en «Actions by profile» para algún perfil permitido en el sitio. Si «Read-only mode» está encendido o el conector apagado, no anuncia ningún grupo de cambio. La lista se calcula en cada petición: encender o apagar una acción, un perfil o el modo de solo lectura cambia lo que se anuncia al momento.
- Con «Basic reading only: profile, courses and grades», solo anuncia leer el perfil, los cursos y las calificaciones de la persona. Con un asistente que no pide más por su cuenta, la página de consentimiento solo ofrece «Read only» y todos los perfiles muestran la misma lista de acciones, sin las de docente, gestor ni administrador.
- Cambiar el ajuste no modifica las conexiones existentes: cada persona desconecta el asistente y lo conecta de nuevo.
Este ajuste se añadió en la versión 0.2.0 tras la primera conexión real con Claude, en la que el sitio solo anunciaba la lectura básica y desde Claude no se podía alcanzar ninguna acción de cambio ni de gestor o administrador. Que la corrección funcione con Claude no consta todavía como probado con el asistente real; consta probado en un sitio de desarrollo simulando su forma de pedir permisos.

## Perfiles
Un perfil es lo máximo que puede hacer una conexión. Son acumulativos.
| Perfil | De fábrica | Quién puede elegirlo | Añade |
|---|---|---|---|
| «Student» (alumno) | Apagado | Quien tiene «Use the student profile in AI assistant connections» (de fábrica, cualquier usuario autenticado) | Sus cursos, entregas, calificaciones y progreso |
| «Teacher» (docente) | Encendido | Quien tiene «Use the teacher profile in AI assistant connections» en algún curso dentro del alcance (de fábrica: profesor, profesor sin edición y gestor) | Participantes, entregas y calificaciones de los cursos que imparte |
| «Manager» (gestor) | Encendido | Quien tiene «Use the manager profile in AI assistant connections» en el sitio o en una categoría dentro del alcance (de fábrica: gestor) | Categorías, matrículas y búsqueda de usuarios en lo que gestiona |
| «Administrator» (administrador) | Apagado | Administradores del sitio, o solo los que se indiquen | Estado del sitio, tareas programadas y plugins instalados |
En cada llamada se vuelve a comprobar el perfil que la persona tiene de verdad en ese curso: una conexión de docente no da datos de docente en un curso donde la persona es solo alumna.
La lista de perfiles disponibles para una persona se recuerda diez minutos como máximo, pero se recalcula en el acto cuando se le asigna o quita un rol, cambia de cohorte, se cambian los permisos de un rol o se cambian los ajustes del plugin.

## Catálogo: 22 acciones que leen
| Perfil mínimo | Acción (título en pantalla) | Qué devuelve |
|---|---|---|
| Alumno | «Get connection info» | Sitio, usuario, perfil, nivel de acceso y límites de la conexión |
| Alumno | «List my courses» | Cursos en los que la persona está matriculada |
| Alumno | «Search courses» | Cursos visibles para la persona que coinciden con un texto |
| Alumno | «Get course outline» | Secciones, actividades y recursos visibles de un curso |
| Alumno | «List upcoming deadlines» | Próximas fechas de entrega propias |
| Alumno | «Get assignment details» | Enunciado y fechas de una tarea y estado de la entrega propia |
| Alumno | «List course announcements» | Avisos recientes del foro de avisos del curso |
| Alumno | «Get my grades» | Calificaciones propias |
| Alumno | «Get my course progress» | Finalización propia de un curso |
| Alumno | «Get pending action status» | Estado de un cambio pedido antes por esa misma conexión |
| Docente | «List course participants» | Participantes de un curso que imparte. Solo nombra los roles y grupos que la persona puede ver en Moodle |
| Docente | «List submissions to grade» | Entregas de tareas pendientes de calificar |
| Docente | «Get submission» | Una entrega: estado, texto en línea, datos de los adjuntos y nota |
| Docente | «Get course grade summary» | Libro de calificaciones del curso |
| Docente | «Get course completion report» | Quién ha completado el curso |
| Docente | «List inactive participants» | Participantes que llevan días sin entrar al curso |
| Gestor | «List course categories» | Categorías que gestiona |
| Gestor | «Get course enrolment summary» | Métodos de matrícula y recuento por rol, sin listar personas |
| Gestor | «Find users» | Cuentas cuyo nombre coincide con un texto |
| Administrador | «Get site status» | Resumen de salud del sitio |
| Administrador | «List scheduled tasks» | Tareas programadas y cuáles fallan |
| Administrador | «List installed plugins» | Plugins instalados |
Todas están encendidas de fábrica en «Actions by profile», pero no sirven de nada hasta que se enciende el conector, un modo y el perfil correspondiente.

## Catálogo: 9 acciones que cambian algo
| Perfil mínimo | Acción (título en pantalla) | Paso adicional mínimo | A qué se limita |
|---|---|---|---|
| Docente | «Save assignment grade» (guardar calificación) | Confirmación en dos pasos | Un alumno por llamada. Rechaza tareas con rúbrica o guía de evaluación, tareas sin calificación y notas bloqueadas o anuladas. No toca el estado del flujo de calificación |
| Docente | «Post course announcement» (publicar aviso) | Confirmación en dos pasos | Un aviso en texto plano en el foro de avisos existente. Un asunto con etiquetas o marcado se rechaza al pedir el cambio |
| Docente | «Send message to participants» (enviar mensaje) | Confirmación en dos pasos | Participantes concretos de un curso, por la mensajería del sitio |
| Docente | «Set activity visibility» (mostrar u ocultar actividad) | Confirmación en dos pasos | Una actividad o recurso |
| Docente | «Update assignment dates» (cambiar fechas de una tarea) | Confirmación en dos pasos | Apertura, entrega y fecha límite; se pueden mover, no quitar |
| Gestor | «Enrol users in course» (matricular) | Confirmación en dos pasos | Usuarios concretos, solo matrícula manual. Rechaza a quien tiene la matrícula manual suspendida o con fechas |
| Gestor | «Create course» (crear curso) | Confirmación en dos pasos | Un curso vacío, siempre oculto para los alumnos |
| Gestor | «Set enrolment status» (suspender o reactivar matrícula) | Aprobación en el sitio | Suspende o reactiva la matrícula de usuarios concretos en un curso. No borra la matrícula ni las notas, entregas, roles o grupos. Solo matrícula manual; nunca la propia |
| Administrador | «Set user suspension» (suspender o reactivar cuenta) | Aprobación en el sitio | Una cuenta entera del sitio (no puede entrar en ningún curso); nunca un administrador del sitio, el invitado ni la propia |
No confundir «Set enrolment status» (la matrícula en un curso; la persona sigue pudiendo entrar al sitio y a sus otros cursos) con «Set user suspension» (la cuenta entera). En esta versión no existe ninguna acción para dar de baja o borrar una matrícula: eso se hace en el sitio.
Todas están apagadas tras instalar o actualizar. Además de encender la acción hace falta: conexión con «Read and changes», el permiso «Allow AI assistant connections to request changes» en el curso o lugar donde se hace el cambio (de fábrica: profesor con edición y gestor; el profesor sin edición no) y los permisos propios de Moodle para esa operación.

## Cómo se aplican los cambios
Ningún cambio se aplica en la primera llamada. Hay dos pasos adicionales posibles:
- «Confirmation in two steps» (confirmación en dos pasos). La primera llamada no cambia nada: devuelve una descripción del cambio exacto, redactada por el sitio con sus propios datos, y un código de un solo uso. El cambio se aplica cuando el asistente llama otra vez con los mismos datos y ese código. Si entre tanto la situación cambió, no se aplica nada y se devuelve una descripción y un código nuevos. El asistente puede dar el segundo paso solo: deja constancia y permite mostrar el cambio, no equivale a una revisión humana.
- «Approval on this site» (aprobación en el sitio). La llamada crea un cambio pendiente y devuelve un enlace a la página «Approve a change requested by an AI assistant». Solo se aplica cuando la persona dueña de la conexión abre esa página con su propia sesión, lee «What will change» (qué va a cambiar) y pulsa «Approve» (aprobar); «Reject» (rechazar) lo descarta. Al aprobar se vuelven a comprobar los permisos, y si la descripción ya no coincide con la mostrada la página lo avisa y pide revisar de nuevo.
Reglas:
- El administrador puede exigir en «Actions by profile» un paso más estricto para cada acción, nunca más débil que el mínimo de la tabla.
- Los asistentes que pueden trabajar sin nadie delante (Copilot Cowork, y los que el administrador añada) necesitan siempre aprobación en el sitio, sea cual sea la acción.
- La persona recibe la notificación «A change requested by an AI assistant needs your approval» con el enlace; los cambios en espera aparecen también en «My AI connections», apartado «Changes waiting for your approval», con el enlace «Review» (revisar).
- No se puede aprobar un cambio estando dentro de la cuenta de otro usuario.
- Un cambio repetido con la misma clave de repetición devuelve la respuesta guardada y no se aplica dos veces.
- «Get pending action status» permite al asistente saber si un cambio pendiente se aplicó, se rechazó, caducó o falló.

## Qué se devuelve y qué se retiene
- Solo campos de una lista fija por acción; nunca contraseñas ni tokens.
- Se respetan actividades ocultas, calificaciones ocultas, grupos separados, asignación de correctores y calificación anónima (los alumnos salen como participantes numerados).
- Los cursos ocultos no se devuelven nunca salvo que se active «Include hidden courses», ni siquiera a quien puede verlos en el sitio.
- Las direcciones de correo de otras personas solo llegan al perfil que indique «Who may receive email addresses of other users» y si además la persona tiene el permiso del sitio para ver campos de identidad.
- El texto escrito por personas (enunciados, avisos, entregas, comentarios) se devuelve como dato y se le quita el texto oculto para un lector humano. El filtro retira, entre otros, texto invisible por tamaño o transparencia (también cuando se acumulan entre elementos anidados), texto sobre fondos con imagen, texto sacado de la vista con márgenes y las clases de ocultación del tema; un texto simplemente pequeño se conserva. Si un texto trae su propia hoja de estilo, o coloca una parte encima de otra, se retiene entero y el asistente recibe una nota que dice que hay que leerlo en el sitio. Es deliberado.
- Un curso al que la persona no puede entrar, una actividad oculta y un identificador inexistente dan la misma respuesta de «no encontrado», para no revelar que existen.
- Las respuestas largas se cortan y se marcan como cortadas; las listas se entregan por páginas.

## Cuándo termina una conexión
- La persona pulsa «Disconnect» (desconectar) en «My AI connections», o un administrador lo hace en «Connections».
- Tiempo sin uso («Connection idle time») o duración máxima («Connection lifetime»). La columna «Valid until» (válida hasta) muestra solo la fecha de la duración máxima.
- Cambio de contraseña de la persona, si «Revoke connections when the password changes» está encendido (de fábrica lo está).
- La cuenta se suspende, se borra o se queda sin acceso.
- La persona pierde el permiso de conectar o entra en una cohorte excluida: pierde la conexión en su siguiente uso.
- Se detecta que una credencial de renovación ya usada se usa otra vez (posible copia): se revoca la conexión entera y se lanza el evento «Credential reuse detected».
- Se retira el sitio de la pasarela: se desconectan todas las conexiones hechas por ella.
Sin revocar, una conexión deja de funcionar mientras: el conector o su modo estén apagados, el sitio esté en mantenimiento, o el sitio ya no acepte la aplicación (se quitó su dirección de retorno, su dominio de confianza o su forma de registro).

## Páginas
Para el administrador, en Administración del sitio › Extensiones › Extensiones locales › Pluginia Connect:
- «Settings» empieza con el enlace «Configuration manual» (manual de configuración), que abre el manual en otra pestaña.
- «Settings» (ajustes), «Actions by profile» (acciones por perfil), «Gateway registration» (registro en la pasarela) y «Diagnostics» (diagnóstico): solo administradores.
- «Connections» (conexiones): requiere «Revoke AI assistant connections of other users». Lista las conexiones activas y permite desconectar una, todas las de un usuario o todas las de una aplicación.
- «Audit report» (informe de auditoría): requiere «View the audit report of AI assistant connections» (de fábrica, gestor). Cada llamada, permitida o rechazada: fecha, usuario, aplicación, acción, perfil, tipo, curso, resultado, motivo, elementos devueltos, duración, dirección IP e identificador de la petición. Filtros y descarga en CSV. Nunca contiene lo que se pidió ni lo que se devolvió.
Para cada usuario, en sus preferencias: «My AI connections» (mis conexiones de IA), con «Connected assistants», «Changes waiting for your approval» y las últimas llamadas hechas en su nombre. El enlace aparece cuando el conector está encendido o la persona tiene alguna conexión activa.

## Tareas programadas y notificaciones
- «Remove expired codes, tokens and pending changes»: cada hora.
- «Remove old records of calls»: una vez al día.
- Notificaciones al usuario, activadas de fábrica por web y por correo y desactivables en sus preferencias: «An AI assistant was connected to my account» y «A change requested by an AI assistant needs my approval».
- Eventos estándar de Moodle para reglas de monitorización: asistente conectado, conexión revocada, herramienta llamada, llamada denegada, cambio en espera, cambio aprobado, cambio rechazado, reutilización de credenciales, límite por hora de registros de otras personas, interruptor del conector cambiado, sitio registrado y sitio retirado de la pasarela.

## Qué se guarda y a dónde van los datos
- En el sitio: conexiones (usuario, aplicación, perfil, permisos, fechas), resúmenes irreversibles de los tokens (nunca el token), el registro de llamadas, los cambios en espera (sus detalles pueden incluir texto, como un mensaje o un comentario de nota, y se borran al resolverse o caducar) y las respuestas guardadas de cambios durante un día.
- Si una llamada no se puede registrar en la auditoría, se rechaza y no devuelve datos.
- El plugin declara todo esto en la API de privacidad de Moodle y permite exportarlo y borrarlo por usuario.
- Destinos externos: el proveedor del asistente elegido por la persona (Anthropic, OpenAI o Microsoft), que recibe lo que la persona pide y lo trata según sus propias condiciones; y, solo si el sitio se registra, la pasarela, que recibe un identificador seudónimo y no el nombre, el correo ni el identificador de usuario.
- El asistente recibe un identificador seudónimo de la persona, distinto para cada aplicación.

## Qué ve cada rol
- Administrador: las seis páginas, los eventos y la orden de emergencia de línea de comandos que revoca todas las conexiones y apaga el conector (descrita en el manual).
- Gestor: «Audit report» de fábrica; «Connections» solo si se le da el permiso.
- Docente, gestor o alumno con permiso de conectar: la página de consentimiento, «My AI connections», la página de aprobación y sus notificaciones.
- Nadie ve las conexiones o llamadas de otra persona sin los permisos anteriores.
