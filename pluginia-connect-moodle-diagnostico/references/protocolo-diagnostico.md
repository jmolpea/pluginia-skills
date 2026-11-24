# Protocolo de diagnóstico de Pluginia Connect

Los mensajes entre comillas son los textos exactos de la versión 0.2.0, en inglés, como salen en pantalla o como los recibe el asistente (que suele repetirlos o parafrasearlos). Pedir siempre el texto literal.

## Ficha mínima
Pedir solo lo que haga falta para la consulta. No pedir tokens, códigos, claves ni acceso de administrador.
- Versión de Moodle y de Pluginia Connect. ¿Sitio de pruebas o de producción? (la 0.2.0 es alfa).
- Modo de conexión que se intenta: directo o pasarela (la pasarela está en servicio desde el 24-11-2026, sin conexión real de un asistente comprobada todavía).
- Asistente (Claude, ChatGPT, Copilot Cowork u otro) y si es de escritorio, web o de línea de comandos.
- Resultado de «Diagnostics»: las filas que no estén en «OK».
- Estado de «Enable the connector», «Allow direct connections», «Read-only mode» y de los cuatro perfiles.
- La conexión afectada, tal como la muestra «My AI connections» o «Connections»: aplicación, «Profile», «Access», «Connected on», «Last used», «Valid until».
- El caso: rol de la persona en el curso (no su nombre), qué pidió al asistente, qué esperaba y qué ocurrió, fecha y hora.
- El mensaje literal y, si lo hay, el «Request ID».
- La fila de «Audit report» de esa llamada: «Action», «Profile», «Kind», «Outcome», «Reason».
- Para cambios: si la acción está encendida para ese perfil en «Actions by profile» y qué paso adicional tiene.
Los datos de personas deben llegar anonimizados.

## Dónde mirar cada evidencia
| Evidencia | Dónde |
|---|---|
| Requisitos del servidor | «Diagnostics» |
| Conector, modos, perfiles, alcance, caducidades, límites | «Settings» |
| Qué acciones tiene cada perfil y su paso adicional | «Actions by profile» |
| Conexiones activas de todos | «Connections» (filtros por usuario y aplicación) |
| Cada llamada, permitida o rechazada, y su motivo | «Audit report» (filtros; resumen «Refused calls and limits reached») |
| Lo que ve la persona | «My AI connections»: asistentes, cambios en espera y últimas 50 llamadas |
| Conexión nueva, revocación, credencial reutilizada, límite por hora | Registros de eventos de Moodle |
| Notificaciones | Preferencias de notificación del usuario; bandeja de notificaciones |

## Cómo leer «Audit report»
| «Outcome» | Significa |
|---|---|
| ok | La llamada se atendió (con «Reason» replayed: se devolvió la respuesta guardada de un cambio ya hecho) |
| confirmation_required | Primer paso de una confirmación en dos pasos: todavía no se ha cambiado nada |
| approval_pending | Cambio creado y en espera de aprobación en el sitio |
| denied | Rechazada; el motivo está en «Reason» |
| rate_limited | Límite alcanzado |
| error | Error inesperado; buscar por «Request ID» |

La columna «Reason» dice qué capa rechazó la llamada:

| «Reason» | Capa que rechazó |
|---|---|
| site_unavailable | Conector o modo apagados, o sitio en mantenimiento |
| tool_disabled | Acción apagada para ese perfil, «Read-only mode», asistente limitado, o función de Moodle apagada |
| profile_not_allowed | El perfil de la conexión no alcanza, o la persona ya no cumple ese perfil |
| scope_missing | La conexión no incluye ese grupo de permisos (típico: es de solo lectura) |
| out_of_scope | El curso o la categoría están fuera del alcance configurado |
| permission_denied | A la persona le falta un permiso de Moodle en ese lugar, o ya no puede usar el conector |
| not_found | No existe o no es visible para la persona (incluye cursos ocultos y actividades ocultas) |
| validation_error | Datos no válidos, o código de confirmación caducado o que no corresponde |
| limit_exceeded | Tope de tamaño o de cantidad (destinatarios, usuarios, cambios en espera) |
| user_action_required | La persona tiene algo pendiente en el sitio (contraseña, políticas, perfil) |
| conflict | El cambio choca con el estado actual o ya se está tramitando |
Si la llamada no aparece en el informe, no llegó a identificarse en el sitio: el problema está antes (servidor, dirección, credencial).

## Árbol: el asistente no encuentra el sitio o no puede conectar
1. Se intenta por el directorio del asistente → Pluginia Connect todavía no figura en los directorios. Por la pasarela (dirección https://connect.pluginia.es/mcp) el sitio tiene que estar registrado en «Gateway registration»; está en servicio, pero no consta ninguna conexión real de un asistente a través de ella. Solo consta una conexión real de prueba con Claude en modo directo; ninguna con ChatGPT o Copilot Cowork. Copilot Cowork no puede conectar en modo directo y la pasarela todavía no lo admite.
2. Conector apagado → «Diagnostics»: «The connector is switched off. Its endpoints answer that the service is unavailable.» El asistente recibe «The connector is switched off on this site.»
3. Ningún modo activado → «The connector is on but no connection mode is enabled, so no assistant can connect.»
4. Sin HTTPS → «HTTPS is required.»; en «Diagnostics», error en «HTTPS».
5. Argumentos de ruta → error en «Path arguments». El asistente no encuentra los metadatos de inicio de sesión.
6. Cabecera Authorization → error en «Authorization header». Síntoma típico: la persona autoriza bien y, acto seguido, el asistente vuelve a pedir conexión o dice que no está autorizado («Authorization is required.»).
7. El asistente busca los metadatos solo en la raíz del dominio → fila «Metadata at the domain root» en «Optional». Añadir la regla de reescritura del manual y repetir el diagnóstico. Probable, no confirmado: esas reglas no se han probado contra los asistentes.
8. Sitio en mantenimiento → «The site is in maintenance mode.»
9. El sitio no es accesible desde internet, o un cortafuegos o un filtro de aplicaciones bloquea las peticiones del asistente → no comprobable desde el plugin; lo revisa quien administra el servidor.
10. El servidor sale por proxy y el asistente se identifica con un documento de metadatos → aviso en «Outgoing proxy».
11. Dirección de conexión mal escrita en el asistente → comprobarla con el manual.
12. Demasiadas peticiones desde una misma dirección → «Too many requests from this address. Try again in a minute.»

## Árbol: error en la página de autorización
| Mensaje en pantalla | Causa | Qué revisar |
|---|---|---|
| «Connections with AI assistants are switched off on this site.» | Conector apagado | «Enable the connector» |
| «This application, or the address it wants to return to, is not accepted by this site. Nothing was shared.» | La aplicación o su dirección de retorno no se aceptan | «Allowed return addresses» (exacta, sin comodines), «Allow assistants to register on their own», «Accept assistants identified by a metadata document», «Trusted domains for metadata documents»; en asistentes de escritorio, «Allow return addresses on the own computer»; modo directo apagado; Copilot Cowork en directo |
| «Guests cannot connect an AI assistant. Log in with your own account and try again from the assistant.» | Sesión de invitado | Entrar con cuenta propia |
| «You are logged in as another user. A connection can only be created by the owner of the account.» | Administrador dentro de la cuenta de otro | Salir y entrar con la propia |
| «Your account cannot be used to connect an AI assistant.» | Cuenta suspendida, sin confirmar o sin acceso | Estado de la cuenta |
| «You do not have permission to connect an AI assistant on this site.» | Falta «Connect an AI assistant to the own account» | Roles de la persona |
| «Your account belongs to a group that cannot connect AI assistants on this site.» | Cohorte excluida | «Excluded cohorts» |
| «None of the connection profiles enabled on this site applies to your account. Contact your site administrator.» | Ningún perfil permitido encaja con sus roles | Perfiles encendidos; permiso de perfil en algún curso o categoría dentro del alcance; con alumnos, que el perfil de alumno está apagado de fábrica |
| «This site does not accept connections from this assistant.» | Copilot Cowork bloqueado | «Microsoft 365 Copilot Cowork» en «Assistants» |
| «Choose one of the profiles listed.» | Perfil no válido | Elegir uno de la lista |
| «Your session expired before the form was sent. Check the details and try again.» | La sesión del sitio caducó con la página abierta | Repetir |
Otros casos:
- El asistente solo ofrece «Read only», con cualquier perfil aparece la misma lista de acciones, o no aparecen las acciones de gestor o de administrador → el asistente pidió solo la lectura básica al conectarse. Revisar «Permissions an assistant asks for when it connects» en «Settings» › «Sign-in and tokens» (debe estar en «Everything switched on in this site (recommended)») y que las acciones esperadas estén encendidas para ese perfil en «Actions by profile». Después, desconectar el asistente (en el asistente y en «My AI connections») y conectarlo de nuevo: el asistente solo pide permisos al conectarse. Si persiste con el ajuste correcto, recoger la lista de acciones que muestra la página de consentimiento para cada perfil y escalar.
- No aparece «Read and changes» («no me deja elegir lectura y cambios») → no hay ninguna acción de cambio encendida en «Actions by profile» para los perfiles de esa persona (lo más frecuente: de fábrica están todas apagadas); «Read-only mode» encendido; el asistente pidió solo la lectura básica (caso anterior); la persona no tiene «Allow AI assistant connections to request changes» en ningún curso dentro del alcance (de fábrica, el profesor sin edición no lo tiene); o Copilot Cowork limitado a «Read only».
- Falta un perfil en la lista tras cambiar un rol o sus permisos → el cambio tiene efecto inmediato; si sigue faltando, la causa es otra: perfil apagado, o permiso de perfil no concedido en ningún curso o categoría dentro del alcance.
- La persona pulsa «Allow» y el asistente dice que la conexión falló → el código entregado vale 60 segundos y un solo uso: comprobar reloj del servidor («Server clock»), cabecera Authorization y que el asistente no tardó o repitió la operación. Probable, no comprobable sin más datos.
- La página no llega a mostrarse y el asistente recibe un error → la petición del asistente no era válida (por ejemplo, pedía acceso para otra dirección). Recoger el texto que muestre el asistente y escalar.

## Árbol: conecta pero no ve acciones, o faltan algunas
1. El modo con el que se creó la conexión se apagó después → la lista llega vacía.
2. El perfil elegido es más bajo que el que necesita la acción → desconectar y conectar con el perfil adecuado, si los roles lo permiten.
3. La acción está apagada para ese perfil en «Actions by profile».
4. Es una acción de cambio: apagada de fábrica; la conexión es «Read only»; «Read-only mode» encendido; o Copilot Cowork en «Read only».
5. La acción se encendió después de conectar → la conexión no incluye su grupo de permisos. Al llamarla: «This connection is read-only. Reconnect and choose 'Read and changes' to allow it.» o «This connection does not include the access this action needs. Reconnect to grant it.» Desconectar y volver a conectar.
6. El asistente pidió solo la lectura básica al conectarse («Permissions an assistant asks for when it connects» en «Basic reading only», o conexión creada antes de encender las acciones) → ver «Otros casos» del árbol anterior.
7. El asistente conserva la lista anterior → el sitio le permite reutilizarla cinco minutos; esperar o reiniciar la conversación. Probable.
8. El asistente decide no usar una acción aunque la tenga → no es cosa del plugin; comprobar en la página de consentimiento, que lista las acciones de cada perfil, y pedir la acción por su nombre.

## Árbol: una acción dice que no tiene permiso
| Mensaje que recibe el asistente | Qué revisar |
|---|---|
| «Your site administrator has disabled this action.» | «Actions by profile» para el perfil de la conexión; política de Copilot Cowork |
| «Changes through the connector are disabled on this site.» | «Read-only mode» |
| «This action needs the … profile. Reconnect and choose it if it applies to you.» | Perfil de la conexión |
| «This connection is read-only. Reconnect and choose 'Read and changes' to allow it.» | Nivel de acceso de la conexión. El sitio responde como falta de permiso, indicando el grupo de permisos que falta, no como credencial inválida: el asistente puede pedir a la persona que lo conceda |
| «You do not have permission to do this here.» | Permisos reales de la persona en ese curso: su perfil efectivo allí o un permiso de Moodle de la operación (línea de detalle de la acción) |
| «You do not have permission to make changes here.» | «Allow AI assistant connections to request changes» en ese curso |
| «Your account no longer qualifies for the … profile. Reconnect and choose another profile.» | La persona perdió el rol, o el perfil se apagó |
| «Your account may no longer use the connector on this site.» | Perdió el permiso de conectar o entró en una cohorte excluida; la conexión queda revocada |
| «This site no longer accepts the application you connected.» | Se quitó su dirección de retorno, su dominio o su forma de registro |
| «This course is not available through the connector.» | «Allowed categories», «Excluded categories», «Excluded courses», «Include hidden courses» |
| «Course N was not found or is not visible to you.» / «The requested item was not found or is not visible to you.» | La persona no puede entrar a ese curso o no ve ese elemento; el mensaje es el mismo si no existe |
| «Sign in to the site and change your password.» / «Your password has expired. Sign in to the site and change it.» / «Sign in to the site and accept the updated policies.» / «Sign in to the site and complete your profile.» | Algo pendiente de la persona en el sitio |
| «The connector is switched off on this site.» / «The site is in maintenance mode.» | Interruptores y mantenimiento |
| «Unexpected error. Quote request ID … to your administrator.» | Buscar ese «Request ID» en «Audit report»; si se repite, escalar con los pasos |
No recomendar ampliar roles sin más: primero identificar la capa (fila de «Audit report», columna «Reason»).

## Árbol: el cambio no se aplica o queda pendiente
1. Es lo previsto: ningún cambio se aplica a la primera. Mirar «Outcome» en la auditoría.
2. confirmation_required y nada más → el asistente no dio el segundo paso en 5 minutos. Pedirle que confirme. Mensaje si el código caducó o no corresponde: «The confirmation token does not match this change or has expired. Call the tool again without 'confirm_token' to get a new summary and token.»
3. El asistente confirma y recibe otra descripción → la situación cambió entre los dos pasos (otra nota, otros destinatarios); hay que confirmar la nueva.
4. approval_pending → espera a la persona: «My AI connections» › «Changes waiting for your approval» › «Review», o el enlace de la notificación. Caduca a los 15 minutos.
5. Estados de la página de aprobación: «The change was applied.»; «The change was rejected. Nothing was changed.»; «This request expired without being approved. Nothing was changed.»; «The change was approved but could not be applied. Nothing was changed.» (seguido del motivo); «The situation on the site changed since you opened this page. Review the change again before approving it.»; «This change can no longer be made.» (permisos o conexión ya no válidos); «This request does not exist or does not belong to you.»; «You are signed in as another user. A change can only be approved by the person it belongs to, signed in as themselves.»
6. Se pidió aprobación donde se esperaba confirmación → es suspensión o reactivación de una matrícula o de una cuenta (siempre aprobación), el administrador eligió «Approval on this site» para esa acción, o la conexión es de un asistente que trabaja sin supervisión.
7. «This connection already has 5 changes waiting. Complete or let them expire before requesting more.» → cuentan también las confirmaciones sin terminar; esperar a que caduquen.
8. «This change is already being processed. Try again in a moment.» → dos peticiones a la vez.
9. «This 'idempotency_key' was already used with different arguments. Use a new key for a different change.» → el asistente reutilizó una clave de repetición.
10. El asistente dice «hecho» y no se ve el cambio → comprobar en el sitio y en la auditoría; una repetición devuelve la respuesta guardada de la primera vez (motivo replayed).
11. Rechazos propios de cada acción:
| Acción | Mensajes |
|---|---|
| «Save assignment grade» | «This assignment is graded with a rubric or marking guide. Grade it on the site.»; «This grade is locked or overridden in the gradebook, or its marking workflow state or the marking by several markers does not let you change it. Change it on the site.»; «This assignment is marked anonymously: name the submission with 'submission_id' instead of 'user_id'.»; «This assignment is not graded.»; «Feedback comments are switched off in this assignment.»; con flujo de calificación activo la nota se guarda pero no se publica |
| «Post course announcement» | «'subject' must be plain text: remove any HTML tags or markup from it and try again.» (se rechaza al pedir el cambio, antes de confirmar); «This course has no announcements forum you can post in.»; «You do not have permission to post announcements in this course.» |
| «Send message to participants» | «Messaging is switched off on this site.»; «One or more recipients are not participants of this course that you can message.»; «A maximum of N recipients can be messaged per call.»; «This connection has reached its daily number of message recipients.» |
| «Update assignment dates» | «The due date must be after the opening date.»; «The cut-off date cannot be before the due date.»; aviso de que las fechas no pueden superar la de «Remind me to grade by» de la tarea |
| «Enrol users in course» | «Manual enrolment is not available in this course.»; «'role' is not a role you can give in this course through the connector.»; rechazo de usuarios con matrícula manual suspendida o con fechas; «A maximum of N users can be enrolled per call.» |
| «Set enrolment status» | «One or more of the users have no manual enrolment in this course. Nothing was requested.»; «You cannot change your own enrolment through the connector.»; «Manual enrolment is not available on this site.»; «The enrolment of a maximum of N users can be changed per call.». Nunca se aplica sin aprobación en el sitio |
| «Create course» | «'short_name' is already in use by another course.»; categoría no encontrada o no gestionada |
| «Set user suspension» | «This account cannot be suspended or reactivated through the connector.»; «You cannot suspend or reactivate your own account.» |

## Árbol: «quiero dar de baja a un alumno» o «quiero borrar algo»
1. No existe ninguna acción que dé de baja una matrícula ni que borre nada. No es un fallo ni tiene ajuste.
2. Lo equivalente es «Set enrolment status»: suspende la matrícula del alumno en ese curso sin borrar la matrícula ni sus notas, entregas, roles o grupos; se reactiva con la misma acción.
3. Requisitos: perfil de gestor, acción encendida en «Actions by profile», conexión con «Read and changes», matrícula manual y aprobación en el sitio (15 minutos). Nadie puede suspender su propia matrícula.
4. Matrículas de otros métodos (automatrícula, cohorte, pago) → la acción no las toca; se gestionan en el sitio.
5. Si lo que se quiere es impedir que la persona entre al sitio entero → «Set user suspension», perfil de administrador. No confundirlas.
6. Para borrar de verdad una matrícula → en el sitio, a mano.
7. El asistente dice haber actuado «como» otro usuario o en su nombre → no es posible: todo se ejecuta y se registra como la persona conectada; comprobarlo en «Audit report».

## Árbol: no llega la notificación de aprobación
1. El cambio era de confirmación en dos pasos → no hay notificación; solo la genera la aprobación en el sitio.
2. La persona desactivó «A change requested by an AI assistant needs my approval» en sus preferencias de notificación (web o correo).
3. La salida de notificaciones por web o por correo está desactivada en el sitio, o el correo del sitio no funciona → probar con otra notificación de Moodle. Probable.
4. Llegó tarde: el cambio caduca a los 15 minutos.
5. La notificación no es necesaria para aprobar: «My AI connections» › «Changes waiting for your approval» › «Review». Si el envío falla, el cambio queda igualmente en espera.
6. La notificación nombra la acción por su identificador (en minúsculas y con guiones bajos), no por su título: puede haberse pasado por alto.
Lo mismo vale para «An AI assistant was connected to my account».

## Árbol: la conexión caduca o se corta
1. Se cumplió «Valid until» → duración máxima («Connection lifetime», 180 días de fábrica). Volver a conectar.
2. Más de 30 días sin uso («Connection idle time») → se corta antes de «Valid until», que no refleja este plazo.
3. Se cambió la contraseña de la persona («Revoke connections when the password changes»).
4. Cuenta suspendida, borrada o sin acceso; pérdida del permiso de conectar; cohorte excluida.
5. Un administrador la desconectó en «Connections», o se usó la orden de emergencia.
6. Se apagó el modo, el conector, o se quitó la dirección o el dominio de la aplicación.
7. Evento «Credential reuse detected»: una credencial de renovación ya usada se presentó otra vez. Puede indicar copia, o un asistente que repite una renovación más de 30 segundos después. Se revoca la conexión entera. Si se repite con el mismo asistente, escalar.
8. Se corta cada hora o cada pocos minutos → el asistente no renueva la credencial de acceso («Access token lifetime»), o el reloj del servidor está mal. Mensaje: «The access token is invalid, expired or revoked.» Probable; revisar «Server clock».
9. Se retiró el sitio de la pasarela (solo conexiones de pasarela).
Una conexión revocada desaparece de las listas de activas; su causa queda en los eventos de Moodle.

## Árbol: el asistente no ve un curso, una entrega o un dato que la persona sí ve
1. Curso oculto → no se devuelve nunca con «Include hidden courses» apagado (de fábrica).
2. Curso o categoría fuera de «Allowed categories» o dentro de «Excluded categories» o «Excluded courses».
3. La conexión tiene perfil de alumno: solo ve lo propio. Con perfil de docente, solo ve como docente los cursos donde tiene el permiso de ese perfil; en los demás, como mucho lo que vería un alumno, y solo si el perfil de alumno está permitido en el sitio.
4. «List my courses» solo lista cursos con matrícula; para los demás, «Search courses».
5. Grupos separados: solo se listan miembros y entregas de los grupos propios (en las tareas manda el modo de grupos de la actividad). Con asignación de correctores, solo las entregas asignadas.
6. Calificación anónima: los alumnos salen como participantes numerados, sin nombre.
7. Paginación: 20 elementos si el asistente no pide más, 50 como máximo por llamada; hay que pedir la continuación. En cursos muy grandes, «List submissions to grade» avisa de que el examen fue parcial.
8. «Get course grade summary» incluye 60 elementos de calificación como máximo.
9. Actividad oculta o no mostrada en la página del curso; calificación oculta para la persona.
10. Texto retenido: el asistente recibe una nota de que el texto no se muestra porque trae su propia hoja de estilo o coloca una parte encima de otra, y que hay que leerlo en el sitio. Es deliberado; también se retiene si otro texto de la misma página trae hoja de estilo. Además se retira el texto invisible por tamaño o transparencia acumulados, sobre fondos con imagen, sacado de la vista con márgenes o con clases de ocultación; un texto simplemente pequeño se conserva.
11. Texto cortado: 4.000 caracteres por texto y el tamaño de respuesta configurado.
12. Correos de otras personas: «Who may receive email addresses of other users» y el permiso del sitio para ver campos de identidad.
13. «Find users»: mínimo 3 caracteres, 20 resultados, sin cuentas borradas.
14. «List inactive participants»: «This site does not show you when participants last accessed.»
15. Contenido que el catálogo no cubre: archivos, otros foros, cuestionarios, otros plugins.
16. Límite por hora de registros de otras personas alcanzado.
17. En «List course participants» faltan roles o grupos de un participante → solo se nombran los roles y grupos que la persona conectada puede ver en Moodle. Es deliberado.

## Árbol: límites
- «Too many requests. Try again in N seconds.» → lecturas o cambios por minuto o por día de esa conexión. Cuentan también las llamadas rechazadas. Mirar el resumen de «Audit report».
- «Another request of this connection is still reading records about other people. Try again in 5 seconds.» → las llamadas de una conexión que devuelven datos de otras personas se atienden de una en una; una esperó más de 10 segundos a la anterior. Reintentar; pedir al asistente que no lance esas consultas en paralelo.
- Los contadores son exactos aunque el asistente lance llamadas simultáneas.
- Canje de credenciales bloqueado («Too many requests. Try again in a minute.») → 120 por minuto por dirección, o 20 identificaciones fallidas de la aplicación en un minuto; los códigos o renovaciones rechazados no cuentan para ese bloqueo.
- Un asistente que encadena muchas llamadas agota el minuto con facilidad: esperar. No se puede subir por encima del máximo.
- Con varios servidores web y contadores locales, los límites no se aplican bien: fila «Rate limit store».

## Árbol: registro en la pasarela
El servicio está en marcha y es gratuito por ahora: la clave de licencia se deja vacía. Mensajes de la página: «The connector is switched off. Switch it on in the settings first: the gateway reads the connection details of the site while registering.»; «The site is not served over HTTPS.»; «The Sodium extension of PHP is not available.»; «The gateway could not be reached. Nothing was changed on this site.»; «The gateway could not verify this site. Check that the site is reachable from the internet over HTTPS and that the connector is switched on, then try again.»; «The licence key is not valid.»; «This licence key is already registered for another site.»; «The gateway does not accept the address of this site. It must be a public HTTPS address.»; «The student profile is on. To register, you must declare that the site is not directed to children under 13, or switch the student profile off.»; «You must accept the terms and the data processing agreement.»; «Too many registration attempts. Try again later.»; «The gateway gave an unexpected answer. Nothing was changed on this site.»
Con la clave vacía no deben salir los mensajes de licencia; si salen, comprobar que el campo está realmente vacío. «The gateway could not verify this site…» → el sitio no es accesible desde internet por HTTPS con su dirección pública o el conector está apagado. «The gateway could not be reached…» o una respuesta inesperada → reintentar más tarde; no se ha cambiado nada en el sitio.

## Árbol: seguridad y dudas de la persona
- Notificación de una conexión que la persona no hizo → «My AI connections» › «Disconnect» de inmediato; cambiar la contraseña; avisar al administrador.
- El asistente propone un cambio que nadie pidió tras leer una entrega o un aviso → puede ser texto de otra persona dirigido al asistente. No aprobar; revisar en el sitio.
- Sospecha de fallo de seguridad del plugin → security@pluginia.es, sin datos reales ni credenciales.

## Cierre
Clasificar cada causa como confirmada, probable o no comprobable. Proponer el ajuste según references/ajustes-y-pruebas.md. Si hay que escalar, redactar la solicitud al mantenedor con pasos reproducibles, el mensaje literal, el «Request ID» y sin datos personales.
