# Configuración de Pluginia Connect (versión 0.2.0)

Nombres tal como aparecen en Moodle. El plugin solo trae la interfaz en inglés; la traducción entre paréntesis es orientativa y no aparece en pantalla. Revisado el 24-11-2026. Manual de configuración: https://claude.ai/artifact/XSFJRPaBcavfAJyFBo7K2Y

Dónde: Administración del sitio › Extensiones › Extensiones locales › Pluginia Connect. Seis páginas: «Settings», «Actions by profile», «Gateway registration», «Diagnostics», «Connections» y «Audit report». Las cuatro primeras, solo administradores. La página «Settings» empieza con el enlace «Configuration manual» («Open the configuration manual of Pluginia Connect (opens in a new tab)»), que lleva al manual.

Orden recomendado en un sitio de pruebas: 1) «Diagnostics» sin errores; 2) perfiles y alcance; 3) «Actions by profile»; 4) «Enable the connector» y «Allow direct connections»; 5) conectar con una cuenta de prueba; 6) revisar «Audit report».

## «Settings» › «General»
| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| «Enable the connector» (activar el conector) | Apagado | Interruptor principal. Apagado, todas las direcciones del conector responden que el servicio no está disponible y ningún asistente lee ni cambia nada. | Encenderlo al final, con todo lo demás decidido. Es también la parada general. |
| «Read-only mode» (modo de solo lectura) | Apagado | Bloquea todas las acciones que cambian algo, para todos. Tampoco se ofrece «Read and changes» al conectar. | Encenderlo si solo se quiere consulta, o para parar los cambios sin cortar las lecturas. |
| «Allow direct connections» (permitir conexiones directas) | Apagado | Los asistentes conectan directamente con el sitio. | Es el único modo utilizable hoy. |
| «Allow the Pluginia Connect gateway» (permitir la pasarela) | Apagado | Admite conexiones a través de la pasarela. Se enciende solo al registrar el sitio. Apagarlo corta la pasarela en el acto sin dar de baja el sitio. | No tocar: la pasarela no está en servicio. |
| «Notice shown before connecting» (aviso antes de conectar) | Vacío | Texto de la institución en la página de consentimiento. | Indicar qué cuentas de asistente se permiten (personales o de la organización). |
| «Privacy policy of the institution» (política de privacidad) | Vacío | Enlace en la página de consentimiento. | Rellenarlo. |

## «Settings» › «Profiles» (perfiles)
| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| «Allow the student profile» | Apagado | Cualquier usuario con el permiso puede conectar para ver sus cursos, entregas, notas y progreso. Encenderlo equivale a declarar que el sitio no se dirige a menores de 13 años y que la institución tiene base jurídica para ofrecerlo. | Decisión de la institución, no técnica. Combinarlo con «Excluded cohorts». |
| «Allow the teacher profile» | Encendido | Quien imparte un curso puede ver participantes, entregas y notas de sus cursos. | Mantener si se quiere uso docente. |
| «Allow the manager profile» | Encendido | Quien gestiona una categoría puede listar categorías, ver resúmenes de matrícula y buscar usuarios. | Apagarlo si no se necesita. |
| «Allow the administrator profile» | Apagado | Los administradores del sitio pueden leer estado del sitio, tareas programadas y plugins instalados. | Encender solo si se va a usar. |
| «Administrators allowed to use the administrator profile» | Vacío | Identificadores de usuario, uno por línea. Vacío = todos los administradores del sitio. | Limitarlo a personas concretas. |
| «Excluded cohorts» (cohortes excluidas) | Vacío | Identificadores de cohorte, uno por línea. Sus miembros no pueden conectar, tengan los roles que tengan, y pierden las conexiones que tuvieran. | Usarlo, por ejemplo, para una cohorte de menores. |

## «Settings» › «Scope» (alcance)
| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| «Allowed categories» | Vacío (todas) | Identificadores de categoría. Si hay alguno, el conector solo alcanza esas categorías y las que contienen. | En pruebas, limitar a una categoría de pruebas. |
| «Excluded categories» | Vacío | Esas categorías y todo su contenido quedan fuera, aunque estén en la lista de permitidas. | Para áreas sensibles. |
| «Excluded courses» | Vacío | Identificadores de curso fuera de alcance. | Para cursos concretos. |
| «Include hidden courses» | Apagado | Apagado, los cursos ocultos no se devuelven nunca, ni a quien puede verlos en el sitio. | Encender si los docentes preparan cursos ocultos y quieren usar el asistente en ellos. |
| «Custom profile fields that may be returned» | Vacío (ninguno) | Nombres cortos de campos personalizados de perfil que se pueden devolver. | Dejar vacío salvo necesidad clara. |
| «Who may receive email addresses of other users» | «Teacher profile and above» | Perfil más bajo que puede recibir correos de otros: «Nobody», «Teacher profile and above», «Manager profile and above», «Administrator profile only». Además la persona necesita el permiso del sitio para ver campos de identidad. | «Nobody» si no hace falta. |

## «Settings» › «Sign-in and tokens» (inicio de sesión y credenciales)
Se aplican a las conexiones directas.
| Ajuste | De fábrica | Qué hace | Recomendación |
|---|---|---|---|
| «Allowed return addresses» | Las de Claude y ChatGPT | Direcciones exactas a las que un asistente puede devolver al usuario tras autorizar. Sin comodines. Quitar una detiene las conexiones de esa aplicación. | No añadir direcciones que no se hayan verificado con la documentación del proveedor. |
| «Allow return addresses on the own computer» | Apagado | Acepta direcciones de retorno en el propio ordenador, que usan asistentes de escritorio, de línea de comandos y herramientas de desarrollo. | Dejar apagado salvo necesidad: cualquier programa del ordenador podría recibir el inicio de sesión. |
| «Allow assistants to register on their own» | Encendido | El asistente se registra antes de que el usuario entre. Solo si todas sus direcciones de retorno están en la lista. | Mantener. |
| «Accept assistants identified by a metadata document» | Encendido | El asistente se identifica con la dirección de un documento que publica. Solo de los dominios de confianza. | Apagarlo si el servidor solo sale a internet por un proxy. |
| «Trusted domains for metadata documents» | claude.ai, chatgpt.com, connect.pluginia.es | Dominios aceptados. Vacío = cualquiera con HTTPS. | No dejar vacío. |
| «Permissions an assistant asks for when it connects» (permisos que pide un asistente al conectarse) | «Everything switched on in this site (recommended)» | Qué grupos de permisos anuncia el sitio a un asistente que conecta. Con el valor de fábrica, todos los que tienen al menos una acción encendida en «Actions by profile» para un perfil permitido, sin ninguno de cambio si «Read-only mode» está encendido. Con «Basic reading only: profile, courses and grades», solo esos tres. Claude pide exactamente lo anunciado y no vuelve a pedir más. Anunciar no concede: la página de consentimiento sigue recortando por perfil y nivel de acceso. | Mantener el valor de fábrica. Tras cambiarlo, o tras encender acciones nuevas, cada persona desconecta el asistente y lo conecta de nuevo. |
| «Access token lifetime» | 3600 | Segundos de validez de la credencial de acceso (300 a 3600). El asistente la renueva solo. | Mantener. |
| «Connection idle time» | 2592000 | Segundos sin uso tras los que hay que volver a conectar (30 días de fábrica). | Bajar en entornos sensibles. |
| «Connection lifetime» | 15552000 | Segundos tras los que hay que autorizar de nuevo (180 días de fábrica). | Bajar a 30 o 90 días si la política lo pide. |
| «Revoke connections when the password changes» | Encendido | Termina todas las conexiones de un usuario cuando cambia su contraseña. | Mantener. |

## «Settings» › «Limits», «Retention» y «Assistants»
Los límites se pueden bajar y no subir; valores e intervalos en references/limites-0.2.0.md.
| Ajuste | De fábrica | Qué hace |
|---|---|---|
| «Read calls per minute» / «Read calls per day» | 60 / 2000 | Lecturas por conexión. |
| «Changes per minute» / «Changes per day» | 10 / 200 | Cambios por conexión. |
| «Records of other people per hour» | 1000 | Registros sobre otras personas que una conexión puede recibir en una hora. Frena la extracción masiva. |
| «Items per page» | 50 | Elementos por llamada. |
| «Answer size» | 48000 | Caracteres por respuesta; lo que excede se corta y se marca. |
| «Users per bulk action» | 50 | Usuarios por matrícula, o por suspensión o reactivación de matrículas. |
| «Recipients per message» | 50 | Destinatarios por mensaje. |
| «Keep the record of calls for» | 180 | Días de conservación de la auditoría (30 a 730). |
| «Keep network addresses» | Encendido | Guarda la dirección de red de cada petición en la auditoría y con las credenciales. |
| «Assistants that can work unattended» | copilot-cowork | Identificadores de asistentes que pueden trabajar sin nadie delante. Para ellos todo cambio exige aprobación en el sitio. Se pueden añadir; el de fábrica se conserva siempre. |
| «Microsoft 365 Copilot Cowork» | «Read, and changes approved on this site» | Otras opciones: «Read only» (solo lectura) y «Blocked: connections from this assistant are refused» (bloqueado). Solo tiene efecto por la pasarela. |
Validaciones visibles: «Enter a whole number between … and ….» en los números; «This entry is not valid: …» en las listas.

## «Actions by profile» (acciones por perfil)
Una fila por acción con una casilla por cada perfil que puede usarla; botón de guardar cambios; mensaje «Changes saved: N.».
- «Actions that read» (acciones que leen): 22, encendidas de fábrica.
- «Actions that change something» (acciones que cambian algo): 9, apagadas de fábrica y tras cada actualización que añada alguna. Encender una a una y por perfil.
- Debajo de cada acción, una línea indica su identificador, si lee o cambia, su grupo de permisos y los permisos de Moodle que se comprueban en cada llamada.
- En las acciones de cambio, el desplegable «Extra step before "…"» elige el paso adicional: «Confirmation in two steps» o «Approval on this site». Solo se ofrecen el mínimo de la acción y los más estrictos.
- Apagar una casilla retira la acción en el acto para todas las conexiones de ese perfil.
- Mientras no haya ninguna acción de cambio encendida para los perfiles de una persona, la página de consentimiento no le ofrece «Read and changes».
- Encender una acción no la da a las conexiones que ya existían si no tenían su grupo de permisos: esas personas deben desconectar y volver a conectar.
- Con «Permissions an assistant asks for when it connects» en su valor de fábrica, lo que se enciende aquí decide también qué grupos de permisos pide el asistente al conectarse. Con «Basic reading only», un asistente como Claude no pide más que la lectura básica, aunque haya acciones encendidas.
Recomendación: donde un error salga caro (calificaciones, matrículas), elegir «Approval on this site».

## «Diagnostics» (diagnóstico)
Tabla con «Check», «Status» («OK», «Optional», «Warning», «Error») y «Result», con el remedio debajo. Botón «Run the checks again». Ejecutarla tras instalar y tras cualquier cambio en el servidor web.
| Comprobación | Si falla | Remedio que indica la página |
|---|---|---|
| «Connector state» | Aviso: conector apagado, o encendido sin ningún modo | Encenderlo; activar conexiones directas o registrar el sitio |
| «HTTPS» | Error: «This site is not served over HTTPS. The connector refuses requests that do not use HTTPS.» | Servir el sitio por HTTPS con certificado reconocido y dirección del sitio en https |
| «Sodium extension» | Error: «The sodium PHP extension is not available.» | Instalar o activar la extensión |
| «Authorization header» | Error: «The web server does not pass the Authorization header to PHP. Assistants will not be able to authenticate.» | Con Apache y PHP-FPM o CGI, la directiva «CGIPassAuth On» o la regla equivalente que muestra la página; con nginx, que ninguna regla quite la cabecera |
| «Path arguments» | Error: «The web server does not pass the path after a script name to PHP. Assistants will not find the sign-in metadata of this site.» | Activar la información de ruta para PHP; la página muestra las dos líneas de nginx |
| «Metadata at the domain root» | «Optional»: la raíz del dominio no sirve los metadatos | Solo si un asistente no logra conectar en modo directo: regla de reescritura del manual. No hace falta para la pasarela |
| «Rate limit store» | Aviso: contadores en un almacén local a un servidor | Con un solo servidor web está bien; con varios, asignar la caché de límites del plugin a un almacén compartido |
| «Cron» | Error: «Cron has never run on this site.» o «Cron last started … ago.» | Cron cada minuto |
| «Server clock» | Muestra la hora del servidor; error si es claramente incorrecta | Sincronizar el reloj |
| «Outgoing proxy» | Aviso: el sitio usa proxy de salida y se aceptan documentos de metadatos | Apagar «Accept assistants identified by a metadata document» si el servidor solo sale por el proxy |
| «Pluginia Connect gateway» | «Optional» si el sitio no está registrado; aviso o error si lo está y algo falla | Los de la página de registro |
Cuando el sitio no puede llamarse a sí mismo, las comprobaciones de cabecera y de ruta salen como aviso: «The site could not call itself to run this check.» Hay que probarlas desde fuera, como indica el mensaje.

## «Gateway registration» (registro en la pasarela)
Servicio todavía no disponible: el formulario existe, pero el registro no se puede completar.
- Muestra «State» («This site is not registered.», «This site is registered.» o «This site was removed here, but the gateway has not confirmed it.») y la tabla «Data sent to Pluginia when you register»: dirección del sitio, versión del software y del plugin, si se ofrece el perfil de alumno, la declaración sobre menores de 13 años, un valor de verificación de un solo uso, un secreto creado en ese momento y la clave de licencia, que no se guarda en el sitio. No se envía ningún dato de usuarios.
- Requisitos previos que la página exige («The site cannot be registered yet:»): conector encendido, sitio en HTTPS y extensión sodium.
- Campos: «Licence key», la casilla de condiciones y contrato de encargo de tratamiento y, con el perfil de alumno encendido, la declaración sobre menores de 13 años. Botón «Register this site».
- Para salir: «Remove this site from the gateway». Desconecta en el acto todas las conexiones hechas por la pasarela y apaga ese modo; las directas no se ven afectadas. Si no se pudo avisar a la pasarela, botón «Tell the gateway again».

## Permisos
| Permiso (nombre en pantalla) | Quién lo tiene de fábrica | Para qué |
|---|---|---|
| «Connect an AI assistant to the own account» | Usuario autenticado | Poder conectar. Prohibirlo a un rol lo deja fuera. |
| «Use the student profile in AI assistant connections» | Usuario autenticado | Elegir el perfil de alumno, si está permitido en el sitio. |
| «Use the teacher profile in AI assistant connections» | Profesor, profesor sin edición, gestor (en el curso) | Elegir el perfil de docente y usarlo en ese curso. |
| «Use the manager profile in AI assistant connections» | Gestor (en la categoría o el sitio) | Elegir el perfil de gestor. |
| «Allow AI assistant connections to request changes» | Profesor con edición, gestor (en el curso) | Que se ofrezca «Read and changes» y que un cambio se admita en ese curso. |
| «View the audit report of AI assistant connections» | Gestor | Página «Audit report». |
| «Revoke AI assistant connections of other users» | Nadie (los administradores del sitio siempre) | Página «Connections». |
Además se aplican los permisos propios de Moodle de cada operación (calificar, matricular, publicar en avisos, etc.), que la línea de detalle de «Actions by profile» enumera.

## Lo que configura cada usuario
- En la página de consentimiento: perfil y nivel de acceso. Para cambiarlos, desconectar y volver a conectar.
- En sus preferencias, «My AI connections»: «Disconnect» junto a cada asistente; «Review» en los cambios en espera.
- En sus preferencias de notificaciones: «An AI assistant was connected to my account» y «A change requested by an AI assistant needs my approval», por web y por correo, activadas de fábrica.

## Ajustes de Moodle que influyen
- Roles y permisos del curso: deciden qué perfil vale en cada curso y qué puede hacer cada acción. Cambiar los permisos de un rol tiene efecto inmediato.
- Visibilidad del curso y de las actividades; modo de grupos; calificación anónima y asignación de correctores en las tareas.
- Mensajería del sitio: si está apagada, «Send message to participants» responde «Messaging is switched off on this site.»
- Foro de avisos del curso: debe existir para leer o publicar avisos; el conector no lo crea.
- Políticas del sitio, cambio de contraseña forzado y campos de perfil obligatorios: si la persona tiene algo pendiente, las llamadas se rechazan hasta que lo resuelva en el sitio.
- Modo de mantenimiento: el conector deja de atender.
- Salidas de notificación del sitio (web y correo) y su configuración de correo.
