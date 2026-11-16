# Límites y valores por defecto: versión 1.1.0

Verificados leyendo el código de 1.1.0 el 16-11-2026. Los valores de fábrica son los mismos que en 1.0.0. Un límite documentado es un hecho; que haya causado un incidente concreto es una conclusión aparte.

## Valores de fábrica del plugin
| Ajuste | Valor de fábrica |
|---|---|
| Matricular automáticamente cuando esté permitido | No |
| Vigencia del enlace de confirmación | 7 días |
| CAPTCHA del formulario de registro (ajuste reCAPTCHA del plugin) | No |
| Bloqueo de campos de perfil | Los valores estándar de Moodle (sin bloquear) |

Tras instalar, el método no está activo: hay que habilitarlo y elegirlo como método de autorregistro en Gestionar autenticación (ver configuracion.md).

## Plazos
| Qué | Plazo | Detalle |
|---|---|---|
| Vigencia del enlace | 7 días de fábrica | Se cuenta desde la creación de la cuenta, no desde el último email. Reenviar no la amplía. Un valor de 0 equivale a 7 días. |
| Borrado de cuentas sin confirmar | Lo decide Moodle | El ajuste estándar de Moodle que elimina cuentas sin completar puede borrarlas antes de que caduque el enlace. |
| Curso pendiente tras confirmar | 24 horas | Dentro de ese plazo, un inicio de sesión normal lleva al curso. Después se olvida y el usuario va donde Moodle le lleve normalmente. |
| Limpieza de cursos pendientes caducados | Cada hora | Tarea programada «Eliminar destinos de curso caducados». |
| Espera ante dos confirmaciones simultáneas | 10 segundos | Después muestra «Se está procesando otra solicitud…». |
| Envío del email | Inmediato | Se envía al crear la cuenta, sin esperar al cron. |

## Qué direcciones sirven para recordar el curso
- La página normal de un curso del sitio y la página de matriculación de un curso del sitio, con el número de curso.
- El enlace de entrada al registro del curso (la página de diagnóstico lo muestra como «Enlace de entrada al registro para este curso»). Es la opción más fiable para catálogos externos, temas personalizados y cursos con acceso de invitados, donde la página del curso podría no pedir iniciar sesión.
- No sirven: la portada, el Área personal, direcciones de otros dominios, ni un curso que no exista. En esos casos no hay curso y el usuario termina en el Área personal.
- El enlace de entrada da el mismo error para un curso inexistente que para uno oculto.

## Cuándo el email nombra el curso
- Solo si el registro empezó en un curso que existe y que la cuenta recién creada puede ver.
- Un curso oculto nunca se nombra en el email ni en la página de confirmación: se envía el email estándar. Aun así el curso se recuerda y, al confirmar, el usuario va a él; si no puede verlo, Moodle se lo dirá.
- El aviso del formulario de registro se comprueba con el visitante sin sesión. Si el sitio tiene activado «Forzar a los usuarios a identificarse», ese aviso puede no aparecer; el email y la página del enlace sí nombran el curso, porque se comprueban con la cuenta ya creada.
- Los reenvíos de Moodle siempre usan el texto estándar.

## Condiciones de la matriculación automática
Ver el apartado «Matriculación automática» de la referencia de funcionamiento. En resumen, nunca matricula si:
- el ajuste está desactivado o la automatriculación está deshabilitada en el sitio;
- el curso solo tiene automatriculación con clave de matriculación o con claves de grupo;
- el método está deshabilitado, no admite nuevas matrículas, está fuera de fechas, sin plazas o restringido a una cohorte a la que el usuario no pertenece;
- el rol del usuario no tiene el permiso de automatricularse;
- el usuario ya tiene cualquier matrícula en el curso, aunque esté suspendida o caducada;
- el curso no es visible para el usuario o ya no existe;
- han pasado más de 24 horas desde la confirmación.

## Mensajes que puede ver el usuario
| Situación | Mensaje |
|---|---|
| Enlace incompleto, inventado, de otra cuenta o de una cuenta suspendida o eliminada | Error estándar de Moodle de datos de confirmación no válidos |
| Enlace caducado | «Este enlace de confirmación ha caducado y ya no se puede usar. Contacte con el soporte del sitio para activar su cuenta.» |
| Enlace ya usado | «Su cuenta ya está confirmada. Inicie sesión para continuar a su curso.» |
| Otra cuenta con la sesión iniciada | «Hay otra cuenta con sesión iniciada. Abra este enlace de confirmación en una ventana privada o cierre primero la sesión.» |
| Dos confirmaciones a la vez | «Se está procesando otra solicitud. Inténtelo de nuevo en unos instantes.» |
| Método deshabilitado | Error estándar de Moodle de confirmación no habilitada |

## Lo que el plugin no hace
- No crea cuentas por otra vía: solo el formulario de registro estándar de Moodle.
- No limita el número de registros: Moodle no trae ese límite; se recomienda CAPTCHA y limitar en el servidor web.
- No permite elegir el curso con un parámetro de redirección ni enviar a páginas que no sean el curso.
- No convierte el enlace de confirmación en un enlace de acceso: tras confirmar, se entra con usuario y contraseña.
- No envía el texto con el curso en los reenvíos.
- No matricula en cursos con clave ni reactiva matrículas.
- No muestra la página de confirmación con el aspecto del tema del sitio.

## Idiomas incluidos
Inglés, español y portugués de Brasil.
