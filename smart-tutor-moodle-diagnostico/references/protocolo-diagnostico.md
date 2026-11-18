# Protocolo de diagnóstico de Smart Tutor & Support AI

## Ficha mínima
Pedir solo lo que haga falta para la consulta. No pedir claves ni acceso de administrador.
- Versión de Moodle y del plugin; proveedor de IA y modelos que muestra la pestaña «General e IA».
- Estado de la licencia tal como lo muestra la página de ajustes.
- Dónde está el bloque: curso, página de una actividad, categoría, portada o Área personal.
- Qué ve exactamente la persona afectada (texto del aviso o del error) y con qué rol.
- Interruptores del sitio y del asistente de la función afectada.
- Para calidad de respuestas: la pregunta (anonimizada), qué respondió y qué muestra la página de la base de conocimiento para la actividad que debería contener la respuesta.
- Para voz y llamadas: navegador, proveedor de voz, motor de la llamada y cupos.
- Para soporte: si el escalado está activado en el sitio y en el curso, dirección de destino rellena o no, y lo que muestra el informe de escalados.
- Si el cron de Moodle se ejecuta y cuándo corrieron por última vez las tareas del plugin.
- Si el curso fue restaurado, duplicado o importado recientemente, o si el sitio cambió de dirección.

## Dónde mirar cada evidencia
| Evidencia | Dónde |
|---|---|
| Licencia, proveedor, modelos | Pestaña «General e IA» |
| Conexión con el proveedor y correo de soporte | Herramientas de prueba |
| Qué ha leído el tutor y con qué estado | Página «Base de conocimiento del aula» del asistente |
| Qué trozos encontraría una pregunta | «Probar una pregunta» en esa página, o la búsqueda de las herramientas de prueba |
| Gasto, mensajes, voz, llamadas, motivos de fin de llamada | Panel de uso |
| Consultas a soporte y su estado (borrador, en cola, enviada, fallida, cancelada, caducada) | Informe de escalados a soporte |
| Respuestas mal valoradas | Respuestas con pulgar abajo |
| Tareas y sus errores | Administración del sitio › Servidor › Tareas programadas y registros de tareas |

## Árbol: el chat no aparece o dice que no está disponible
1. Aviso de licencia (falta, no válida para este sitio, caducada, prueba de 15 días terminada) → estado en «General e IA». Tras cambiar la dirección del sitio, la clave deja de valer.
2. «El asistente no está configurado» → falta la clave del proveedor elegido o «Habilitar el plugin» está apagado.
3. «El asistente no está habilitado en este curso» o aviso de no disponible → «Habilitar el asistente en este curso» apagado en ese asistente.
4. «El asistente no está disponible en este curso» (Moodle 5.1 o posterior) → «Permitir herramientas de IA» desactivado en los ajustes del curso; el personal ve un aviso que lo explica.
5. No se ve nada → el usuario no tiene el permiso de uso (invitados, rol modificado), o es la página de matrícula con un asistente de curso.
6. Bloque en el Área personal → no soportado; ponerlo en un curso, una categoría o la portada.
7. Falta una opción en la configuración del asistente → el administrador no la ha permitido en el sitio.

## Árbol: el tutor responde mal o dice que el material no lo cubre
1. La base de conocimiento del aula no está activada en el asistente, o no está permitida en el sitio.
2. La actividad no está «Indexado»: Pendiente (falta cron o está en cola), Sin texto, Error, Saltado (archivo demasiado grande o pesado de leer), Excluido, Evaluable.
3. PDF escaneado o casi todo en imágenes → la página lo avisa; subir una versión con texto.
4. El alumno no puede abrir esa actividad (oculta, restringida, de otro grupo) → con él no se usa. Comprobar con «qué ve un alumno» en las herramientas de prueba.
5. Sin búsqueda por significado (proveedor de embeddings «Desactivado» o sin clave) → busca por palabras exactas.
6. La respuesta está en un cuestionario → nunca se lee.
7. Documento con más de 200 páginas o texto muy largo → solo se lee el principio; la página lo indica.
8. La pregunta fue al ayudante equivocado → preguntar la versión (antes de 5.3.3, palabras como «fecha de entrega», «me falta» o «da error» mandaban preguntas de la materia al asistente, y «cómo mejorar X» a la revisión del trabajo); revisar si se editó el prompt del enrutador y devolverlo al texto de fábrica.
8 bis. El tutor dice que no puede confirmar una cita que acaba de dar, o responde solo a una de dos preguntas del mismo mensaje → antes de 5.3.4 los seguimientos sin tema y los mensajes con dos pedidos se buscaban mal; recomendar actualizar.
9. Prompt del tutor del curso vacío o demasiado restrictivo.
10. Respuesta recortada por la comprobación con el material → probar con la comprobación apagada, cambiando solo eso.

## Árbol: respuestas cortadas, lentas o que aparecen de golpe
1. Cortadas a mitad de frase → subir los tokens máximos de salida; frecuente con modelos que razonan.
2. Aparecen de golpe con el streaming activado → un servicio intermedio (proxy, CDN) retiene la respuesta; lo resuelve el equipo técnico. Sigue funcionando.
3. Muy lentas → esfuerzo de razonamiento alto, modo «Todo el curso en cada respuesta», comprobación de respuestas, o modelo propio lento (subir la espera del servidor compatible).
4. «El asistente no está disponible temporalmente» → fallo del proveedor: saldo, clave revocada, modelo retirado o dirección base cambiada. Usar la prueba de conexión. Desde 5.3.3 el plugin ya ha repetido la llamada una vez si fue un corte o un error interno del proveedor.
5. «Estás enviando mensajes demasiado rápido o el asistente no está disponible temporalmente» (desde 5.3.3) → el proveedor de IA rechazó la petición por el límite de uso de la cuenta del cliente; no son los límites de mensajes de Moodle. Revisar el plan y los límites en la web del proveedor. El aviso corto, sin la segunda parte, sí es el límite por minuto o por día de Moodle.

## Árbol: datos de Moodle que da el asistente
1. Dice que no puede consultar algo → la herramienta correspondiente está desmarcada en «Herramientas del asistente habilitadas», o el asistente está apagado en ese bloque.
2. No sabe explicar por qué una actividad o una semana está bloqueada, o cita un número en lugar del nombre de la actividad → corregido en 5.3.3; preguntar la versión.
3. Responde en español a una pregunta corta en portugués → corregido en 5.3.3; comprobar además que la «Política de idioma» está en «Automático».

## Árbol: voz y llamadas
1. No aparece el micrófono → «Permitir la voz» (sitio), voz activada en el asistente, permiso de voz del rol, plugin y asistente habilitados. No existe en asistentes de portada o categoría.
2. No aparece «Llamar» → además, «Permitir el modo llamada», modo llamada en el asistente y, con el motor «Paso a paso», un proveedor de voz que no sea «Navegador».
3. «Has usado los minutos de voz de hoy» o el tiempo de llamada → cupo diario; también pueden ser los topes mensuales del curso o del sitio.
4. La llamada se corta → duración máxima, cupo diario, pérdida de conexión (más de 2 minutos sin latidos) o llamada abierta en otra pestaña. El panel de uso muestra el motivo. Antes de 5.3.2, con Gemini en tiempo real y duración 0 se cortaba a los 20 minutos.
5. «No se ha podido usar la grabación» → audio vacío, demasiado largo o en un formato que el servidor no reconoce.

## Árbol: soporte por correo
1. El asistente solo da el enlace → escalado apagado en el sitio o en el curso, sin dirección de destino, límites superados, o el usuario no tiene permiso de pedir soporte.
2. La tarjeta dice que venció → borrador de más de 24 horas; pedirlo de nuevo.
3. Enviada pero no llega → estado en el informe (en cola: falta cron; fallida: correo saliente de Moodle, con el motivo al lado); probar el correo en las herramientas de prueba.
4. Al guardar el formulario, error en las direcciones → mal escritas o de un dominio no permitido (desde 5.3.2 el aviso distingue los dos casos también en el enrutado por categoría).
5. Curso restaurado desde otro sitio → las direcciones de destino no se copian; hay que ponerlas otra vez.
6. El correo de un asistente de categoría o de portada lleva el nombre del sitio en lugar del curso → comportamiento anterior a 5.3.3. Desde 5.3.3 nombra el curso de la página donde se muestra el asistente o el que nombra la conversación, si es un curso del propio participante dentro de esa categoría; si no se puede determinar, sigue saliendo el del sitio.

## Árbol: gasto
1. Mirar en el panel de uso qué curso, modelo y función concentran el coste.
2. Causas habituales: modo «Todo el curso en cada respuesta», comprobación de respuestas, descripción de imágenes en la primera lectura, llamadas en tiempo real, asistente abierto a visitantes sin captcha, modelo grande escrito a mano.
3. El importe es una estimación; contrastar con la factura del proveedor.
