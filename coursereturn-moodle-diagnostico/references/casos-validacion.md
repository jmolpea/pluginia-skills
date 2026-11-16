# Casos sintéticos de validación
No corresponden a clientes reales. Evaluar las respuestas en una conversación nueva que solo reciba la skill y el caso.

1. «Los alumnos se registran desde el curso, confirman y acaban en el Área personal.»
Esperado: pedir el diagnóstico de una cuenta; si no hay destino original guardado, el registro no empezó en el curso (curso con invitados o enlace externo); proponer el enlace de entrada al registro del curso.

2. «Un alumno dice que no le llega el email, pero si lo reenvío yo, sí.»
Esperado: el primero se envía al registrarse; la causa está en la entrega (greylisting, spam, SPF/DKIM); revisar eventos de email fallido sabiendo que cero no prueba la entrega.

3. «Abrí el enlace y me salió una página con un botón; no lo pulsé y al día siguiente el enlace seguía funcionando. ¿Es un fallo?»
Esperado: no; abrir el enlace no confirma, solo el botón; protege de los filtros de correo.

4. «Han pasado 10 días y el enlace dice que ha caducado. Le reenvié el email y sigue igual.»
Esperado: la vigencia (7 días de fábrica) se cuenta desde la creación; reenviar no la amplía; un administrador puede confirmar la cuenta a mano.

5. «El alumno llega al curso pero no queda matriculado.»
Esperado: revisar el ajuste de matriculación automática y el método de automatriculación (clave, claves de grupo, nuevas matrículas, fechas, plazas, cohorte, permiso); no forzar.

6. «Tenía una matrícula suspendida en ese curso, se registró de nuevo y no se reactivó.»
Esperado: el plugin nunca reactiva matrículas; lo hace el profesor o el administrador.

7. «Sale "Hay otra cuenta con sesión iniciada".»
Esperado: abrir el enlace en una ventana privada o cerrar la otra sesión; es una protección.

8. «El email de confirmación no dice el nombre del curso.»
Esperado: preguntar si fue un reenvío (texto estándar) o si el curso está oculto; el enlace lleva igualmente al curso.

9. «Con el MFA activado, ¿el alumno tendrá que meter un código por email además de confirmar?»
Esperado: con el factor de email, la confirmación cuenta como ese factor en esa sesión; otros factores sí se piden.

10. «Quiero que el enlace de confirmación sirva para entrar siempre sin contraseña.»
Esperado: no es posible ni conveniente; tras confirmar se entra con usuario y contraseña.

11. «Voy a desinstalar el plugin. ¿Qué pasa con las cuentas?»
Esperado: pasan al autorregistro por email estándar, se conservan contraseñas y matrículas; los enlaces enviados antes dejan de funcionar y hay que reenviarlos.

12. «¿Qué datos guarda el plugin?»
Esperado: solo el curso pendiente y su caducidad, como mucho 24 horas, declarado en la API de privacidad; nada sale del sitio.
