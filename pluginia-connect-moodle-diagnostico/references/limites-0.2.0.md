# Límites y valores de fábrica de Pluginia Connect: versión 0.2.0

Verificados leyendo el código de la versión 0.2.0 el 24-11-2026. Los nombres entre comillas son los de la pantalla (en inglés). Manual: https://claude.ai/artifact/XSFJRPaBcavfAJyFBo7K2Y

## Cómo interpretar los valores
Distinguir tres clases:
- Límites ajustables en «Settings»: se pueden bajar, nunca subir por encima del máximo indicado. Si se escribe un valor fuera del intervalo, la página responde «Enter a whole number between … and ….» y no lo guarda.
- Límites fijos del plugin: no tienen ajuste.
- Límites de la pasarela: los fija el servicio, que todavía no está en producción; se citan según la documentación del proyecto y pueden cambiar.
«Por conexión» significa por cada asistente conectado por cada persona: dos personas, o dos asistentes de la misma persona, no comparten contador.
Los contadores van por ventanas de reloj (el minuto, la hora o el día en curso del servidor), no por los últimos 60 segundos. Cuentan todas las llamadas autenticadas, también las rechazadas.

## Estado de fábrica al instalar
| Elemento | De fábrica |
|---|---|
| «Enable the connector» | Apagado |
| «Read-only mode» | Apagado |
| «Allow direct connections» | Apagado |
| «Allow the Pluginia Connect gateway» | Apagado (se enciende al registrar el sitio) |
| Perfil «Student» | Apagado |
| Perfil «Teacher» | Encendido |
| Perfil «Manager» | Encendido |
| Perfil «Administrator» | Apagado |
| Las 22 acciones que leen | Encendidas para sus perfiles |
| Las 9 acciones que cambian algo | Apagadas para todos los perfiles |
| Nivel de acceso propuesto al conectar | «Read only» |
| «Include hidden courses» | Apagado |
| «Who may receive email addresses of other users» | «Teacher profile and above» |
| «Allow return addresses on the own computer» | Apagado |
| «Allow assistants to register on their own» | Encendido |
| «Accept assistants identified by a metadata document» | Encendido |
| «Revoke connections when the password changes» | Encendido |
| «Keep network addresses» | Encendido |
| «Microsoft 365 Copilot Cowork» | «Read, and changes approved on this site» |

## Caducidades de la conexión
Los tres primeros ajustes se escriben en segundos.
| Concepto | Ajuste | De fábrica | Mínimo y máximo |
|---|---|---|---|
| Vida de la credencial de acceso | «Access token lifetime» | 3.600 s (1 hora) | 300 s (5 minutos) a 3.600 s (1 hora) |
| Tiempo sin uso tras el que hay que volver a conectar | «Connection idle time» | 2.592.000 s (30 días) | 3.600 s (1 hora) a 7.776.000 s (90 días) |
| Duración máxima de la conexión | «Connection lifetime» | 15.552.000 s (180 días) | 86.400 s (1 día) a 31.536.000 s (365 días) |
| Código que se entrega al pulsar «Allow» | Fijo | 60 segundos, un solo uso | — |
| Margen para repetir una renovación por fallo de red | Fijo | 30 segundos | — |
| Conexiones revocadas guardadas como constancia | Fijo | 30 días | — |
| Aplicaciones registradas que nadie usa | Fijo | Se eliminan a los 30 días | — |
| Recuerdo de los perfiles disponibles de una persona | Fijo | 10 minutos como máximo; se recalcula en el acto al cambiar roles, permisos de un rol, cohortes o ajustes | — |
El asistente renueva la credencial de acceso por su cuenta; la persona no nota nada. Ninguna credencial dura más allá de la duración máxima de la conexión.
Los valores nuevos se aplican a las conexiones y renovaciones posteriores al cambio.

## Límites de uso por conexión
| Límite | Ajuste | De fábrica | Mínimo y máximo |
|---|---|---|---|
| Lecturas por minuto | «Read calls per minute» | 60 | 1 a 60 |
| Lecturas por día | «Read calls per day» | 2.000 | 1 a 2.000 |
| Cambios por minuto | «Changes per minute» | 10 | 1 a 10 |
| Cambios por día | «Changes per day» | 200 | 1 a 200 |
| Registros de otras personas por hora | «Records of other people per hour» | 1.000 | 1 a 1.000 |
| Destinatarios de mensajes por día | Fijo | 200 | — |
De fábrica todos están ya en su máximo, salvo el tamaño de la respuesta.
Mensajes que recibe el asistente: «Too many requests. Try again in N seconds.»; «This connection has reached its hourly limit of records about other people. Try again in N seconds.»; «This connection can message 200 recipients per day and has N left today.»
El límite por hora de registros de otras personas afecta a participantes, entregas, libro de calificaciones, informe de finalización, participantes inactivos y búsqueda de usuarios, y a los cambios cuya descripción nombra a personas. Al alcanzarlo se lanza un evento.
Los límites de lectura y de cambios son exactos también con llamadas simultáneas: cada llamada se cuenta de una en una.
Las llamadas de una misma conexión que devuelven datos de otras personas se atienden de una en una. Si una espera más de 10 segundos a la anterior, responde límite alcanzado con reintento a los 5 segundos: «Another request of this connection is still reading records about other people. Try again in 5 seconds.»
Si los contadores no están disponibles, las llamadas se rechazan.

## Tamaños
| Límite | Ajuste | De fábrica | Mínimo y máximo |
|---|---|---|---|
| Elementos por llamada | «Items per page» | 50 | 1 a 50 |
| Caracteres por respuesta | «Answer size» | 48.000 | 2.000 a 60.000 |
| Usuarios por acción en lote (matricular, suspender o reactivar matrículas) | «Users per bulk action» | 50 | 1 a 50 |
| Destinatarios por mensaje | «Recipients per message» | 50 | 1 a 50 |
Valores fijos:
| Concepto | Valor |
|---|---|
| Elementos devueltos si el asistente no pide un número | 20 (10 en avisos; 50 en progreso del curso) |
| Cada texto escrito por personas dentro de una respuesta | 4.000 caracteres; el resto se corta y se marca |
| «Search courses» | Considera 200 coincidencias como máximo |
| «Find users» | Texto de al menos 3 caracteres; 20 resultados como máximo, sin forma de listar a todos |
| «Get course grade summary» | 60 elementos de calificación como máximo |
| «List submissions to grade» | Examina hasta 2.000 entregas; si el curso es mayor avisa de que el examen fue parcial |
| «List upcoming deadlines» | 14 días de fábrica; máximo 180 |
| «List inactive participants» | 14 días de fábrica; máximo 365 |
| Asunto y texto de un aviso | 255 y 4.000 caracteres |
| Comentario de una calificación | 4.000 caracteres |
| Nombre completo y nombre corto de un curso nuevo | 254 y 100 caracteres |
| Tamaño de una petición al conector | 256 KB |

## Cambios pendientes
| Concepto | Valor |
|---|---|
| Código de la confirmación en dos pasos | 5 minutos, un solo uso |
| Cambio en espera de aprobación en el sitio | 15 minutos |
| Cambios en espera por conexión (confirmaciones sin terminar y aprobaciones juntas) | 5 |
| Resultado guardado de un cambio resuelto | 1 día |
| Recuerdo de una clave de repetición | 1 día |
Ninguno es ajustable. Mensaje al llegar al tope: «This connection already has 5 changes waiting. Complete or let them expire before requesting more.»

## Auditoría y páginas
| Concepto | Ajuste | De fábrica | Mínimo y máximo |
|---|---|---|---|
| Conservación del registro de llamadas | «Keep the record of calls for» | 180 días | 30 a 730 días |
| Llamadas propias visibles en «My AI connections» | Fijo | Las últimas 50 | — |
| Filas por página en «Audit report» | Fijo | 100 | — |
| Filas por página en «Connections» | Fijo | 50 | — |

## Protección de las direcciones del conector
Fijos, por dirección de red de origen salvo que se indique:
| Punto | Límite |
|---|---|
| Llamadas al conector, antes de identificarse | 600 por minuto |
| Canje y renovación de credenciales | 120 por minuto; además 20 identificaciones fallidas de la aplicación por minuto, por aplicación y dirección (un código o una credencial de renovación rechazados no cuentan) |
| Registro de aplicaciones por sí mismas | 10 por hora; entre 1 y 10 direcciones de retorno por aplicación |
| Descarga de documentos de metadatos de aplicaciones | 10 por minuto; documento de 64 KB como máximo; 5 segundos; un fallo se recuerda 5 minutos |
| Verificación del sitio durante el registro en la pasarela | 10 por minuto; solo responde durante 10 minutos mientras hay un registro en curso |
Mensajes: «Too many requests from this address. Try again in a minute.»; «Too many requests. Try again in a minute.»; «Too many registrations from this address.»

## Diagnóstico y tareas
| Concepto | Valor |
|---|---|
| «Cron» en «Diagnostics» | Error si cron no ha arrancado en los últimos 10 minutos o nunca |
| Comprobaciones en que el sitio se llama a sí mismo | 5 segundos de espera |
| Llamadas del sitio a la pasarela | 5 segundos para conectar, 30 en total |
| «Remove expired codes, tokens and pending changes» | Cada hora |
| «Remove old records of calls» | Una vez al día |

## Pasarela (servicio todavía no disponible)
Según la documentación del proyecto, no verificable en el plugin: 120 llamadas por minuto y 10 conexiones por persona y sitio; la undécima conexión cierra la más antigua.

## Direcciones y listas de fábrica
- «Allowed return addresses»: https://claude.ai/api/mcp/auth_callback y https://chatgpt.com/connector_platform_oauth_redirect. Coincidencia exacta, carácter a carácter, sin comodines.
- «Trusted domains for metadata documents»: claude.ai, chatgpt.com y connect.pluginia.es. Si la lista se deja vacía se acepta cualquier dominio con HTTPS, lo que no se recomienda.
- «Assistants that can work unattended»: copilot-cowork, que no se puede quitar.
- Pasarela: https://connect.pluginia.es
