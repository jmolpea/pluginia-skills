# Configuración: ajustes y recomendaciones

Nombres tal como se ven en Moodle en español, versión 1.1.1. Los ajustes son los mismos que en 1.1.0 y 1.0.0. Explicación ampliada y ejemplos en el manual: https://claude.ai/artifact/S9nVg3PK3GW412ms6GScy9

## Puesta en marcha (ajustes de Moodle, no del plugin)
Dónde: Administración del sitio › Extensiones › Autenticación › Gestionar autenticación. Solo administradores.
1. Habilitar «Registro por email con retorno al curso» en la lista de métodos (icono del ojo).
2. En el desplegable de autorregistro de la misma página, elegir «Registro por email con retorno al curso».
Son dos ajustes distintos: habilitado sin elegirlo como autorregistro, nadie se registra con él. Mantener habilitado cualquier método que usen cuentas existentes, incluido «Autorregistro por email», para que sus cuentas pendientes puedan confirmar.
3. Comprobar que el correo saliente del sitio funciona (Administración del sitio › Servidor › Email) y que el cron se ejecuta.
4. Recomendado: activar el CAPTCHA (ver abajo) y revisar los dominios de email permitidos y denegados de Moodle.

## Ajustes del plugin
Dónde: Administración del sitio › Extensiones › Autenticación › Registro por email con retorno al curso. Una sola página. Arriba, por este orden: el enlace «Manual de configuración» (se abre en una pestaña nueva), un texto de ayuda y el enlace «Diagnóstico de registro y retorno al curso».

| Ajuste | Valor de fábrica | Qué hace | Recomendación |
|---|---|---|---|
| Matricular automáticamente cuando esté permitido | No | Tras confirmar el email y superar MFA, políticas y perfil, matricula al usuario solo si el curso tiene una automatriculación abierta sin clave ni clave de grupo. Nunca reactiva matrículas. Con él activado, el formulario de registro, el email y la página de confirmación avisan de que confirmar es solicitar la matrícula. | Activarlo si los cursos de destino son de acceso libre. Dejarlo apagado si la matrícula la gestiona otra persona o un pago. |
| Vigencia del enlace de confirmación | 7 días | Antigüedad máxima de la cuenta cuando se pulsa el botón. Se indica con un número y una unidad (semanas, días, horas…). Reenviar no la amplía. | Dejar 7 días. Acortarla solo con una razón de seguridad, porque los alumnos que tardan quedan bloqueados y deben pedir ayuda. |
| Habilitar reCAPTCHA (ajuste estándar del autorregistro, con el texto de Moodle) | No | Muestra un CAPTCHA en el formulario de registro. Si el CAPTCHA estaba activado en «Autorregistro por email», se sigue mostrando aunque aquí esté apagado. Necesita las claves de reCAPTCHA del sitio. | Activarlo en sitios públicos. |
| Bloquear valor (campos de perfil) | Sin bloquear | Los ajustes estándar de Moodle para bloquear campos del perfil de estas cuentas. | Igual que en el autorregistro estándar. |

El nombre exacto en español del ajuste de CAPTCHA y de los de bloqueo es el que trae el paquete de idioma de Moodle (No verificado en pantalla).

El texto de ayuda de arriba pide no excluir del MFA la página final del plugin que nombra: si se excluyera, el plugin repite igualmente la comprobación de MFA.

## Aspecto del email de confirmación (desde 1.1.1)
El plugin no tiene ajustes para el aspecto del email. La versión con formato usa lo que el sitio ya tiene:

| Qué | De dónde sale | Si falta |
|---|---|---|
| Logo | Administración del sitio › Apariencia › Logos, campo «Logo» | Aparece el nombre del sitio como texto |
| Color del botón | El color de marca del tema activo (en Boost, «Color de marca») | El color de marca general del sitio si existe; si no, el azul por defecto de Moodle |
| Firma | La firma estándar de los emails del sitio (quien figura como soporte) | Se omite |
| Frases y texto del botón | Los textos del plugin, en el idioma del registro | Se cambian con la personalización de idioma |

Recomendación: subir el logo del sitio y fijar el color de marca en el tema; con eso el email queda con la imagen de la institución sin tocar el plugin. Al personalizar las frases, dejar el enlace solo en su párrafo, entre líneas en blanco, para conservar el botón. El nombre exacto en español de los ajustes de logo y color es el del paquete de idioma de Moodle y del tema (No verificado en pantalla).

## Configuración en cada curso
No hay ajustes del plugin dentro del curso. Para la matriculación automática, en el curso: Participantes › Métodos de matriculación › Automatriculación:
- habilitado;
- «Permitir nuevas matrículas»: Sí;
- sin clave de matriculación y sin claves de grupo;
- fechas, plazas y cohorte según se quiera: el plugin las respeta.
El rol, la duración y el mensaje de bienvenida son los de ese método.

## Enlaces para los visitantes
- La dirección normal del curso: funciona cuando el curso pide iniciar sesión a quien no la tiene.
- El enlace de entrada al registro del curso: guarda el curso y abre directamente el inicio de sesión. Recomendado para webs y catálogos externos, temas personalizados y cursos con acceso de invitados. La página de diagnóstico lo muestra al consultar una cuenta que tenga ese curso; el manual explica cómo formarlo.
- Quien abre directamente el formulario de registro sin pasar por un curso termina en el Área personal.

## Idiomas
Los textos del plugin, el email incluido, están en inglés, español y portugués de Brasil. El texto puede ajustarse con la personalización de idioma estándar de Moodle (Administración del sitio › Idioma › Personalización del idioma), buscando las cadenas del plugin. El cambio se aplica a la versión de solo texto y a la versión con formato del email, porque las dos salen del mismo texto.
