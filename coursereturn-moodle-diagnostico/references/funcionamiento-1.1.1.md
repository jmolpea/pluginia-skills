# Funcionamiento verificado: versión 1.1.1

Revisión estática del código que declara 1.1.1 (versión interna 2026111601), para Moodle 4.5 a 5.3. Revisado el 18-11-2026.
Manual público: https://claude.ai/artifact/S9nVg3PK3GW412ms6GScy9
Todo lo que sigue son hechos leídos en el código, salvo lo marcado como «No verificado».

## Cambios de 1.1.0 a 1.1.1
- El email de confirmación que nombra el curso se envía ahora en dos versiones dentro del mismo mensaje: una con formato (logo o nombre del sitio, botón «Abrir la página de confirmación» y el enlace completo debajo) y la de solo texto, que no cambia respecto a 1.1.0.
- Sin cambios en los ajustes, sus valores de fábrica, los permisos, la tarea programada, los plazos, la página de confirmación ni los datos guardados. No hay ningún ajuste nuevo para el aspecto del email: sale de la configuración que el sitio ya tiene.
- El email estándar de Moodle (registro sin curso, curso que la cuenta no puede ver y reenvíos) no cambia.

## Cambios de 1.0.0 a 1.1.0
- Confirmación explícita: en 1.0.0 la página que abre el enlace se enviaba sola con JavaScript; desde 1.1.0 muestra el curso, qué supone confirmar y el email medio oculto, y solo confirma al pulsar el botón «Confirmar e ir al curso» (o «Confirmar mi cuenta» si no hay curso). Abrir el enlace ya no confirma nada, ni siquiera con un navegador que ejecute JavaScript.
- Email de confirmación: en 1.0.0 era siempre el estándar de Moodle; desde 1.1.0, si el registro empezó en un curso que la cuenta recién creada puede ver, el email nombra el curso, explica el botón y dice hasta cuándo vale el enlace. Con la matriculación automática activada, avisa de que confirmar es solicitar la matrícula.
- La página que aparece tras enviar el formulario de registro nombra el curso.
- Enlace caducado: en 1.0.0 daba el error genérico de datos de confirmación no válidos; desde 1.1.0 tiene su propio mensaje.
- Enlace ya usado: en 1.0.0 llevaba al inicio de sesión con el aviso estándar de Moodle de registro ya confirmado; desde 1.1.0 dice «Su cuenta ya está confirmada. Inicie sesión para continuar a su curso.»
- Nuevo idioma: portugués de Brasil (ya había inglés y español).
- Enlace «Manual de configuración» en la parte superior de los ajustes del plugin.
- Versiones de Moodle: 1.0.0 declaraba solo 4.5; desde 1.1.0 se declara de 4.5 a 5.3.
- Sin cambios en los ajustes, sus valores de fábrica ni los datos guardados.

## Qué es
Un método de autenticación de Moodle: el autorregistro por email de siempre, con una diferencia. Recuerda el curso desde el que empezó el visitante y, al confirmar el email, le inicia la sesión y le lleva a ese curso. Opcionalmente le matricula, si el propio curso lo permite. No usa inteligencia artificial ni servicios externos. Necesita los plugins estándar de autorregistro por email y de automatriculación, que vienen con Moodle.

## Flujo completo
1. Un visitante sin sesión abre la página de un curso (o el enlace de entrada al registro de ese curso) y Moodle le pide iniciar sesión.
2. Elige «Crear una cuenta nueva». El formulario es el estándar de Moodle, con sus comprobaciones, CAPTCHA, campos de perfil y políticas. Si el curso es visible para el visitante, encima aparece un aviso con su nombre:
   - sin matriculación automática: «Tras confirmar su email y completar los controles de acceso requeridos, volverá a [curso].»;
   - con ella: «Al crear esta cuenta para acceder a [curso], solicita matricularse en este curso…».
3. Al enviar el formulario se crea la cuenta sin confirmar y se envía el email en ese momento, sin esperar al cron. La página siguiente dice a qué dirección se envió y a qué curso llevará.
4. El email (con curso visible) se titula «[sitio]: confirme su cuenta para el curso [curso]», explica que el enlace abre una página con el botón «Confirmar e ir al curso», da la fecha y hora hasta la que vale y dice que, si no se pidió la cuenta, basta con ignorarlo. Se escribe en el idioma en que se rellenó el formulario (inglés, español o portugués de Brasil; otros idiomas, en inglés salvo traducción del sitio). Lleva una versión con formato y otra de solo texto (ver «El email con formato»).
5. El botón del email y el enlace abren la misma página sencilla, sin el tema del sitio, que muestra el nombre del sitio, «Confirme su cuenta», qué pasará al confirmar, «Cuenta: » con el email medio oculto (primera letra, puntos y el dominio) y el botón. Abrirla no cambia nada.
6. Al pulsar el botón de esa página, el plugin confirma la cuenta, inicia la sesión y pasa a la página final del plugin.
7. Antes de llegar al curso, Moodle aplica sus controles normales: autenticación multifactor (MFA), aceptación de políticas del sitio y campos obligatorios del perfil.
8. La página final matricula al usuario si la matriculación automática está activada y el curso lo permite, borra el curso pendiente y le lleva al curso. Si no se matricula, Moodle muestra la página normal de acceso o matriculación del curso.

Sin curso (registro abierto directamente, curso inexistente o que la cuenta recién creada no puede ver, como un curso oculto): email estándar de Moodle; la página del enlace dice «Confirme para activar su cuenta. A continuación iniciará sesión.» con el botón «Confirmar mi cuenta»; al confirmar, sesión iniciada y Área personal. El plugin nunca adivina un curso.

## El email con formato (desde 1.1.1)
Solo el email del plugin que nombra el curso. De arriba abajo:
- Una franja fina con el color de marca y, debajo, el logo del sitio, que enlaza con la página principal. El logo es el principal del sitio (Administración del sitio › Apariencia › Logos, campo «Logo»). Si ese campo está vacío, aparece el nombre del sitio como texto. No se usa el logo compacto ni un logo guardado en los ajustes propios de un tema.
- Los mismos párrafos del texto, en el mismo orden.
- En el lugar del enlace, un botón con el texto «Abrir la página de confirmación» (en inglés «Open the confirmation page»; en portugués de Brasil «Abrir a página de confirmação») y, justo debajo, el enlace completo en pequeño, para copiarlo si el botón no se abre.
- Al final, separada por una línea, la firma estándar de los emails del sitio.

Color del botón: el color de marca del tema activo del sitio (en el tema Boost, el ajuste «Color de marca»); si el tema no lo tiene, el color de marca general del sitio si existe; y si no, el azul por defecto de Moodle. El texto del botón sale en blanco o en oscuro, lo que más contraste tenga con ese color.

Cómo se construye: a partir del mismo texto que la versión de solo texto. Por eso las frases cambiadas con la personalización de idioma de Moodle salen en las dos versiones. El párrafo que contiene únicamente el enlace es el que se convierte en botón; si una personalización mete el enlace dentro de una frase, no hay botón y el enlace queda como texto. Un tema a medida puede sustituir la plantilla de este email.

El botón del email no confirma la cuenta: solo abre la página de confirmación. La confirmación sigue exigiendo pulsar el botón de esa página.

Qué versión ve cada persona: su programa de correo muestra la versión con formato si la admite y, si no, la de solo texto. Si bloquea las imágenes, en lugar del logo se ve el nombre del sitio. No verificado: Moodle decide si adjunta la versión con formato según el formato de email de la cuenta, que en una instalación estándar es HTML para las cuentas nuevas; en un sitio que haya cambiado ese valor por defecto a texto, podría enviarse solo el texto.

## Cómo se decide el curso
- Solo se acepta la dirección de un curso del propio sitio (la página del curso o su página de matriculación) que exista y no sea la portada. Cualquier otra dirección de vuelta se descarta: el plugin no guarda ni sigue direcciones arbitrarias.
- El curso se guarda en la cuenta al registrarse. Al confirmar, pasa a ser «curso pendiente» durante 24 horas.
- Si el usuario cierra el navegador antes de llegar al curso, dentro de esas 24 horas basta con iniciar sesión normalmente: Moodle le lleva de nuevo a la página final y de ahí al curso.
- Una tarea programada, que se ejecuta cada hora, borra los cursos pendientes caducados.

## Matriculación automática
Solo si se cumplen todas:
- «Matricular automáticamente cuando esté permitido» activado (de fábrica, no).
- El plugin de automatriculación está habilitado en el sitio.
- El curso existe, el usuario puede verlo y es su curso pendiente.
- El usuario no tiene ninguna matrícula previa en ese curso, por ningún método ni en ningún estado (activa, suspendida o caducada).
- El curso tiene un método de automatriculación habilitado, sin clave de matriculación y sin claves de grupo, que en ese momento permite inscribirse: «Permitir nuevas matrículas» activado, dentro de sus fechas, con plazas libres, sin restricción de cohorte que excluya al usuario, y el rol del usuario tiene el permiso de automatricularse.
Se usa el propio mecanismo de automatriculación de Moodle: rol, duración y mensaje de bienvenida son los del método del curso. Nunca se reactivan matrículas existentes.

## Confirmación y seguridad
- El enlace lleva un código secreto de Moodle de 15 caracteres. El plugin comprueba usuario y código a la vez, de modo que un enlace inventado y uno con un usuario inexistente dan el mismo error.
- Solo confirma el botón de la página, que exige la clave de sesión del propio navegador. Los filtros de correo y las vistas previas que abren el enlace (o que «pulsan» el botón del email) no consumen la confirmación.
- La página de confirmación no carga el tema ni JavaScript a propósito, para que nada interfiera con el cambio de sesión al iniciar sesión; por eso tiene un aspecto sencillo.
- Si en ese navegador ya hay otra cuenta con la sesión iniciada, no la sustituye: muestra «Hay otra cuenta con sesión iniciada. Abra este enlace de confirmación en una ventana privada o cierre primero la sesión.»
- Un enlace ya usado no vuelve a iniciar sesión: lleva al inicio de sesión con «Su cuenta ya está confirmada. Inicie sesión para continuar a su curso.» Si quien lo abre es el mismo usuario con la sesión ya iniciada, continúa directamente.
- Las cuentas suspendidas o eliminadas no se pueden confirmar.
- Si dos peticiones llegan a la vez para la misma cuenta, la segunda espera hasta 10 segundos; si no puede, muestra «Se está procesando otra solicitud. Inténtelo de nuevo en unos instantes.»

## MFA y políticas
- Si el MFA está activado con el factor de email, la confirmación cuenta como prueba de ese factor solo para esa sesión, así que no se envía un segundo código. Los demás factores y los inicios de sesión posteriores siguen la configuración del sitio.
- La página final repite la comprobación de MFA aunque un administrador la excluyera del MFA.
- Las políticas aceptadas en el formulario de registro se conservan aunque se confirme en otro navegador; las pendientes o nuevas las pide Moodle.

## Reenvíos y cuentas existentes
- Los reenvíos de Moodle (desde el inicio de sesión de una cuenta sin confirmar o desde la administración de usuarios) usan el texto estándar de Moodle y el enlace estándar de confirmación, sin el logo ni el botón del plugin. El plugin reconoce esos enlaces de sus cuentas y los lleva a la misma página con botón y al mismo curso.
- Reenviar no amplía la vigencia: se cuenta desde la creación de la cuenta.
- Las cuentas pendientes del autorregistro por email estándar siguen pudiendo confirmar.

## Página de diagnóstico
Solo administradores (permiso de configurar el sitio). Está enlazada en los ajustes del plugin: «Diagnóstico de registro y retorno al curso». No cambia nada, no confirma enlaces y no muestra contraseñas, cuerpos de email ni códigos.
- Sitio: versión de Moodle, URL del sitio, versión del plugin (como número interno: 2026111601 es la 1.1.1; 2026111600, la 1.1.0), método habilitado, método de autorregistro elegido, matriculación automática, MFA, vigencia del enlace en segundos (604800 son 7 días), SMTP configurado, todo el correo desactivado, desvío de correo y gestor de políticas.
- Cuenta (botón «Consultar sin modificar» con un nombre de usuario): método de autenticación, confirmada, suspendida / eliminada, creación, último acceso y acceso actual, si guardó un destino original, curso de la URL original, curso pendiente y su caducidad, política aceptada, eventos de email fallido y el último, y aceptación de cada versión de política.
- Curso de esa cuenta: «Enlace de entrada al registro para este curso», si el curso es visible para el usuario, si tiene el permiso de automatricularse, si ya tiene matrícula activa, si la automatriculación está habilitada en el sitio y, por cada método de automatriculación del curso, si está habilitado, admite nuevas matrículas, tiene clave o clave de grupo, fechas, cohorte, plazas y matriculados.
- Lectura (texto de la propia página): sin confirmar y sin curso original, el destino se perdió antes de enviar el email; confirmada, el enlace ya se usó o la confirmó un administrador; la falta de curso pendiente después de completar el retorno es normal; cero emails fallidos no demuestra la entrega.
- La página no dice nada del aspecto del email (logo, color o versión enviada).

## Desinstalación
Se hace desde la administración de extensiones antes de borrar la carpeta. Las cuentas del método pasan al autorregistro por email estándar, que queda habilitado; si este método era el de autorregistro, se cambia al estándar. Se borran los cursos pendientes. Se conservan contraseñas y matrículas. Los enlaces de emails enviados antes dejan de funcionar: hay que reenviarlos desde la administración de usuarios.

## Privacidad
Guarda una preferencia temporal de usuario con el identificador del curso pendiente y su caducidad, desde la confirmación hasta llegar al curso, como mucho 24 horas. Está declarada y se exporta con la API de privacidad de Moodle, y se borra con el resto de preferencias del usuario. También usa la preferencia estándar de Moodle que guarda la página de origen del autorregistro por email. Ningún dato sale del sitio. El email con formato carga el logo desde el propio sitio; no usa servicios de terceros.
