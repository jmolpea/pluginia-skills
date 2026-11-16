# Ajustes y pruebas antes de escalar

## Regla de intervención
Resolver primero con lo que el cliente puede cambiar: el correo del sitio, Gestionar autenticación, los ajustes del plugin, el método de automatriculación del curso y el enlace que se da a los visitantes. Cambiar una sola cosa cada vez y anotar el resultado.
No proponer desactivar el MFA, las políticas ni la confirmación por email para «que funcione». No proponer quitar la clave de un curso que la necesita.

## Lo que el cliente puede ajustar
| Capa | Quién | Ajustes disponibles |
|---|---|---|
| Correo | Administrador | Servidor de correo saliente, dirección remitente, SPF/DKIM/DMARC, desvío y desactivación del correo |
| Autenticación | Administrador | Habilitar el método, elegirlo como autorregistro, CAPTCHA, dominios permitidos y denegados, borrado de cuentas sin confirmar |
| Plugin | Administrador | Matriculación automática, vigencia del enlace, CAPTCHA, bloqueo de campos |
| Curso | Profesor o gestor | Método de automatriculación: habilitado, nuevas matrículas, clave, claves de grupo, fechas, plazas, cohorte, rol |
| Enlace | Quien publica el curso | Dirección del curso o enlace de entrada al registro |
| Cuenta | Administrador | Confirmar a mano, reenviar el email, suspender o eliminar |

## Prueba controlada de referencia
1. Usar una ventana privada y una dirección de email de prueba que no exista en el sitio.
2. Abrir el enlace de entrada al registro del curso (o la página del curso) y comprobar el aviso con el nombre del curso en el formulario.
3. Registrarse. Comprobar la página siguiente y el email: asunto con el curso y fecha de vigencia.
4. Abrir el enlace: debe salir «Confirme su cuenta», el curso, la cuenta medio oculta y el botón. Comprobar que, sin pulsarlo, la cuenta sigue sin confirmar en la página de diagnóstico.
5. Pulsar «Confirmar e ir al curso». Completar MFA, políticas y perfil si se piden.
6. Resultado esperado: dentro del curso; con matriculación automática y método abierto, matriculado.
7. Volver a abrir el enlace en otra ventana privada: debe pedir iniciar sesión con «Su cuenta ya está confirmada…».

## Lo que no se resuelve con ajustes (versión 1.1.0)
- Que los reenvíos de Moodle lleven el texto con el nombre del curso.
- Matricular en cursos con clave o por otros métodos (manual, pago, cohorte).
- Reactivar matrículas suspendidas o caducadas.
- Ampliar la vigencia de un enlace ya enviado sin cambiar el ajuste para todos.
- Dar a la página de confirmación el aspecto del tema.
- Volver al curso después de 24 horas desde la confirmación.
- Elegir el curso de destino con un parámetro de la dirección.
