# Protocolo de casos

## Ficha mínima
Pedir según la consulta, no todo siempre:
- Versión de Moodle y del plugin.
- Si «Registro por email con retorno al curso» está habilitado y elegido como autorregistro en Gestionar autenticación.
- Por dónde entró el visitante: la página del curso, el enlace de entrada al registro, una web externa o el formulario de registro directamente.
- Qué vio en cada paso: aviso del curso en el formulario, página tras el registro, email recibido (asunto y si nombra el curso), página del enlace, mensaje literal si lo hubo y página final.
- Si se pulsó el botón de la página de confirmación.
- Captura de la página de diagnóstico del plugin con la cuenta afectada (sin nombre ni email visibles).
- Del curso: método de automatriculación (habilitado, nuevas matrículas, clave, claves de grupo, fechas, plazas, cohorte).
- Si hay MFA, políticas del sitio o campos de perfil obligatorios.
No pedir contraseñas, el enlace de confirmación completo, acceso administrativo ni el ZIP del plugin.

## Síntoma: el email no llega
1. En la página de diagnóstico, parte del sitio: «Todo el correo desactivado» en Sí o «Desvío de correo configurado» en Sí explican que no llegue al destinatario.
2. Para la cuenta: «Eventos de email fallido» mayor que cero indica que el servidor de correo rechazó el envío; revisar la configuración del correo saliente.
3. Cero fallos no demuestra la entrega: revisar los registros del servidor o proveedor de correo a la hora del registro, la carpeta de spam o cuarentena y el greylisting (el primer mensaje a una dirección nueva suele retrasarse unos minutos; un reenvío posterior llega enseguida).
4. Revisar SPF, DKIM y DMARC de la dirección remitente que usa Moodle.
5. Si un reenvío manual sí llega y el primero no, la causa está en la entrega, no en el plugin: el primero se envía en el mismo momento del registro.

## Síntoma: el enlace da error
1. «Ha caducado»: pasó la vigencia desde la creación de la cuenta; reenviar no la amplía. Opciones: que un administrador confirme la cuenta a mano, o ampliar la vigencia si es razonable.
2. «Su cuenta ya está confirmada»: el enlace ya se usó (o un administrador confirmó la cuenta). Debe iniciar sesión con usuario y contraseña; si han pasado menos de 24 horas desde la confirmación, llegará al curso.
3. «Hay otra cuenta con sesión iniciada»: abrir el enlace en una ventana privada o cerrar la otra sesión.
4. Datos de confirmación no válidos: enlace cortado por el programa de correo (copiarlo entero), enlace de una cuenta eliminada (por ejemplo, por el borrado automático de cuentas sin confirmar de Moodle), cuenta suspendida, o método desinstalado y vuelto a instalar.
5. Confirmación no habilitada: el método está deshabilitado en Gestionar autenticación.

## Síntoma: confirma pero termina en el Área personal
1. Diagnóstico de la cuenta: «Destino original guardado» en No y «Curso de la URL original» vacío significan que el registro no empezó en un curso (formulario abierto directamente, enlace de una web que no pasa por el curso, o curso de acceso libre para invitados que no pidió iniciar sesión). Solución: usar el enlace de entrada al registro del curso.
2. Si había curso pero «Curso pendiente» está vacío tras completar el retorno, es normal: se borra al llegar al curso.
3. Si el usuario cerró el navegador y volvió después de 24 horas, el curso pendiente ya caducó.
4. Comprobar que el curso existe y no es la portada.

## Síntoma: llega al curso pero no se matricula
1. «Matricular automáticamente cuando esté permitido» activado.
2. En el diagnóstico: «Plugin de automatriculación habilitado» en Sí y «Capacidad enrol/self:enrolself» en Sí.
3. Cada «Instancia de automatriculación»: habilitada, nuevas matrículas, sin clave, sin clave de grupo, dentro de fechas, plazas disponibles, cohorte.
4. «Matrícula activa» en No pero el usuario tenía antes una matrícula suspendida o caducada en ese curso: el plugin no la reactiva nunca; debe hacerlo el profesor o el administrador.
5. «Curso visible para el usuario» en No: curso oculto o en una categoría que no puede ver.
6. Más de 24 horas entre la confirmación y la llegada al curso.

## Síntoma: el MFA o las políticas interrumpen
Es el comportamiento esperado: Moodle pide MFA, políticas y campos obligatorios antes del curso. Al terminarlos, el usuario sigue al curso. Con el factor de email del MFA, la confirmación ya cuenta como ese factor en esa sesión. Si se queda en otra página, pedir que inicie sesión de nuevo dentro de las 24 horas.

## Síntoma: el email no nombra el curso
1. ¿Es un reenvío? Los reenvíos usan siempre el texto estándar de Moodle; su enlace lleva igualmente a la página con botón y al curso.
2. ¿Puede ver el curso una cuenta recién creada? El email y la página del enlace se comprueban con la cuenta ya creada: si el curso está oculto o en una categoría que esa cuenta no puede ver, no se nombra.
3. ¿Empezó el registro en el curso? Ver el síntoma «termina en el Área personal».
4. ¿Hay una personalización de idioma que cambie el texto?

## Síntoma: un alumno dice que no pidió la cuenta o que entró en una cuenta ajena
La página de confirmación muestra el email de la cuenta medio oculto para que cada persona reconozca la suya; no confirma hasta pulsar el botón. Si alguien confirmó una cuenta que no es suya, el administrador puede suspenderla o eliminarla.
