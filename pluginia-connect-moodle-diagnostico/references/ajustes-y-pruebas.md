# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero la solución en lo que el cliente puede cambiar. Cambiar una sola cosa cada vez y anotar el resultado real.
La versión 0.2.0 es alfa: todas las pruebas se hacen en un sitio de pruebas con datos inventados, nunca con alumnos reales.
No ampliar roles, encender perfiles ni activar acciones de cambio para «hacer desaparecer» un rechazo sin saber antes qué capa lo produjo (columna «Reason» de «Audit report»).
Avisar de que lo que el asistente lee sale del sitio hacia el proveedor del asistente, que lo trata con sus propias condiciones, y de que cada prueba cuenta en los límites de la conexión.
Tras cualquier cambio en el servidor web, volver a ejecutar «Diagnostics».

## Qué puede ajustar el cliente
| Ámbito | Ajuste | Efecto esperado |
|---|---|---|
| Servidor | HTTPS, cabecera Authorization, argumentos de ruta, cron, sodium, reloj, almacén compartido de contadores | Que los asistentes puedan encontrar el sitio, identificarse y que los límites y caducidades funcionen |
| Servidor | Regla de reescritura en la raíz del dominio (manual) | Que un asistente que solo mira la raíz encuentre los metadatos en modo directo |
| Sitio | «Enable the connector», «Allow direct connections» | Encender, o parar todo |
| Sitio | «Read-only mode» | Parar todos los cambios sin cortar las lecturas |
| Sitio | Perfiles permitidos, administradores autorizados, «Excluded cohorts» | Quién puede conectar y con qué tope |
| Sitio | «Allowed categories», «Excluded categories», «Excluded courses», «Include hidden courses» | Qué cursos alcanza el conector |
| Sitio | «Who may receive email addresses of other users», campos de perfil | Qué datos personales se devuelven |
| Sitio | «Allowed return addresses», registro propio, documentos de metadatos y dominios de confianza, direcciones en el propio ordenador | Qué aplicaciones pueden conectar en modo directo |
| Sitio | Caducidades de credencial, de inactividad y de duración; revocar al cambiar la contraseña | Cuánto dura una conexión |
| Sitio | Límites de llamadas, registros por hora, tamaños | Solo a la baja |
| Sitio | «Keep the record of calls for», «Keep network addresses» | Conservación de la auditoría |
| Sitio | «Actions by profile»: casillas y paso adicional | Qué acciones existen para cada perfil y con qué garantía se aplican los cambios |
| Sitio | «Connections»: desconectar una conexión, un usuario o una aplicación | Cortar accesos concretos |
| Roles | Los siete permisos del plugin y los permisos propios de Moodle de cada operación | Quién conecta, con qué perfil, quién puede pedir cambios y dónde |
| Curso | Visibilidad, grupos, foro de avisos, matrícula manual, ajustes de las tareas | Lo que cada acción puede leer o cambiar |
| Usuario | Perfil y nivel de acceso al conectar; desconectar y volver a conectar | El tope de esa conexión |
| Usuario | Preferencias de notificación | Recibir o no los avisos de conexión y de aprobación |
| Sitio | Mensajería y salidas de notificación de Moodle | Que funcionen el envío de mensajes y las notificaciones |

## Lo que ningún ajuste cambia en la versión 0.2.0
- El catálogo es de 31 acciones. No se pueden añadir acciones, ni hacer que el asistente actúe sobre otros plugins, otros foros, cuestionarios o archivos.
- No se puede borrar nada desde el asistente, ni dar de baja una matrícula (solo suspenderla o reactivarla), ni retirar un aviso o un mensaje ya enviados.
- Todo se ejecuta y se registra como la persona conectada; ninguna acción actúa en nombre de otro usuario.
- Ningún cambio se aplica a la primera. El paso adicional se puede endurecer, no suavizar; la suspensión o reactivación de una matrícula y la de una cuenta exigen siempre aprobación en el sitio.
- Los máximos de los límites no se pueden superar. Los 200 destinatarios de mensajes por día y conexión, los 5 cambios en espera, los 5 minutos del código de confirmación y los 15 minutos de la aprobación son fijos.
- Copilot Cowork no conecta en modo directo y todos sus cambios exigen aprobación.
- La pasarela no está en servicio: no se puede registrar el sitio ni conectar desde el directorio de un asistente.
- La interfaz está solo en inglés.
- Los textos con hoja de estilo propia o con partes superpuestas se retienen enteros.
- Los cursos nuevos nacen vacíos y ocultos; las fechas de una tarea se mueven, no se quitan; las tareas con rúbrica o guía de evaluación no se califican desde el asistente.
- Para cambiar el perfil o el nivel de acceso de una conexión hay que desconectar y volver a conectar.
- No hay pantalla con el consumo de límites en curso; se deduce del informe de auditoría.
Explicarlo con claridad y, si es un requisito del cliente, prepararlo como petición de mejora al mantenedor.

## Entorno de prueba recomendado
1. Un sitio de pruebas con HTTPS público y «Diagnostics» sin errores.
2. Una categoría de pruebas indicada en «Allowed categories», con un curso visible que tenga foro de avisos, una tarea con calificación en puntos y al menos una entrega.
3. Tres cuentas inventadas: un profesor con edición, un profesor sin edición y un alumno, matriculados en ese curso. Una cuenta de gestor en la categoría si se van a probar matrículas.
4. Conector y modo directo encendidos; acciones de cambio apagadas al empezar.
5. Tener abiertas «Audit report» y, con la cuenta de prueba, «My AI connections».
La forma de añadir el conector en cada asistente no consta en esta documentación: seguir la ayuda del proveedor y el manual.

## Pruebas controladas
| Prueba | Cambio único | Resultado esperado |
|---|---|---|
| Servidor | Ejecutar «Diagnostics» | Ninguna fila en «Error»; «Connector state» en «OK» |
| Conexión básica | El profesor con edición conecta con perfil «Teacher» y «Read only» | Página de consentimiento con sus acciones; notificación de conexión nueva; fila en «Connected assistants» |
| Lectura | Pedir «List my courses» | Fila con resultado ok en la auditoría; solo cursos dentro del alcance |
| Perfil | Conectar con la cuenta de alumno con el perfil de alumno apagado | «None of the connection profiles enabled on this site applies to your account…» |
| Alcance | Excluir el curso en «Excluded courses» y repetir una lectura | «This course is not available through the connector.» o curso no encontrado |
| Curso oculto | Ocultar el curso con «Include hidden courses» apagado | El curso deja de aparecer; encendiendo el ajuste, vuelve |
| Acción apagada | Apagar una acción de lectura para «Teacher» | Desaparece para esa conexión; si se llama: «Your site administrator has disabled this action.» |
| Solo lectura | Encender «Set activity visibility» para «Teacher» y pedir ocultar una actividad con la conexión «Read only» | La acción no figura entre las del asistente; si aun así la llama: «This connection is read-only. Reconnect and choose 'Read and changes' to allow it.» |
| Confirmación en dos pasos | Reconectar con «Read and changes» y repetir | Primero una descripción del cambio sin aplicar nada (confirmation_required); al confirmar, cambio aplicado y resultado ok |
| Aprobación en el sitio | Poner «Approval on this site» en esa acción y repetir | approval_pending; notificación; el cambio aparece en «Changes waiting for your approval»; al pulsar «Approve», «The change was applied.» |
| Rechazo | Repetir y pulsar «Reject» | «The change was rejected. Nothing was changed.» |
| Caducidad de la aprobación | Repetir y esperar más de 15 minutos | «This request expired without being approved. Nothing was changed.» |
| Permiso de cambios | Conectar con el profesor sin edición | No se ofrece «Read and changes» |
| Sin acciones de cambio | Con todas las acciones de cambio apagadas, conectar con el profesor con edición | No se ofrece «Read and changes»; al encender una para «Teacher» y volver a conectar, sí |
| Modo de solo lectura | Encender «Read-only mode» | Los cambios responden «Changes through the connector are disabled on this site.» |
| Desconexión | «Disconnect» en «My AI connections» | El asistente pierde el acceso en el acto |
| Contraseña | Cambiar la contraseña de la cuenta de prueba | La conexión desaparece de «Connected assistants» |
| Parada general | Apagar «Enable the connector» | «The connector is switched off on this site.»; al encender de nuevo, las conexiones no revocadas vuelven a servir |

## Registro de prueba
| Ensayo | Cambio único | Configuración (modo, asistente, perfil, nivel de acceso, acción) | Estado | Resultado observado («Outcome», «Reason», mensaje) | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñado; pendiente de ejecutar; ejecutado en Moodle; no resuelto; resuelto en las condiciones probadas.

## Cómo parar, de lo más estrecho a lo más amplio
| Qué se quiere parar | Cómo |
|---|---|
| Una conexión, un usuario o una aplicación | «Connections» › «Disconnect», «All of this user» o «All of this application» |
| Una acción | «Actions by profile» › apagar su casilla |
| Todos los cambios | «Read-only mode» |
| Un asistente que trabaja sin supervisión | «Assistants» › «Read only» o «Blocked» |
| La pasarela | Apagar «Allow the Pluginia Connect gateway» o retirar el sitio |
| Todo | Apagar «Enable the connector» |
| Todo, y revocar todas las conexiones | Orden de emergencia de línea de comandos descrita en el manual |

## Cuándo escalar al mantenedor
Cuando un comportamiento contradiga esta documentación tras una prueba limpia, cuando aparezca «Unexpected error. Quote request ID …» de forma repetida, cuando un asistente concreto no logre conectar con «Diagnostics» sin errores, o cuando el requisito del cliente choque con algo que ningún ajuste cambia. Incluir: versiones de Moodle y del plugin, servidor web, modo, asistente, perfil y nivel de acceso, pasos, mensaje literal, «Request ID», filas de «Diagnostics» que no estén en «OK», registro de pruebas, síntoma residual y criterio de aceptación. Contacto: julio@rsmax.es. Fallos de seguridad: security@pluginia.es.
