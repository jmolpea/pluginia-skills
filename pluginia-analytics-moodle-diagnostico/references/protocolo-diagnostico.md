# Protocolo de casos

## Ficha mínima
Pedir según la consulta, nunca todo de golpe:
- Versión de Moodle y del plugin (Administración del sitio › Extensiones › Vista general de extensiones).
- Captura de la Auditoría de preparación (Administración del sitio › Informes).
- Estado de la licencia tal como aparece bajo el campo de la clave (no la clave).
- Rol de la persona afectada en el curso y qué ve exactamente (captura).
- Para cifras: captura de las tarjetas del embudo y la línea final «Analíticas calculadas: … · Actividades con seguimiento: …».
- Para mensajes: captura del formulario del curso, de la tabla de automatizaciones, del resultado de «Enviar mensajes ahora» y del historial; exportación anonimizada de alumnos en riesgo.
- Para tareas: última ejecución y salida de la tarea afectada (Administración del sitio › Servidor › Tareas).
- Para IA: proveedor, modelo elegido, si hay modelo personalizado, mensaje de error literal.
No pedir claves, contraseñas ni acceso de administrador. Pedir datos de alumnos anonimizados.

## Árbol síntoma → causas → comprobación

### Aviso de licencia en lugar de los paneles
Causas: evaluación de 15 días terminada; clave para otra dirección (http/https, subdominio); clave caducada hace más de 30 días.
Comprobar: estado bajo el campo de la clave; dirección del sitio frente a la de la compra.
Acción: introducir clave o pedir sustitución. Nada se ha borrado.

### Panel del sitio «se está preparando» o datos desactualizados
Causas: cron parado; tarea horaria desactivada o fallando; licencia sin vigor (las tareas no hacen nada).
Comprobar: Auditoría (Cron, Actualidad y Fiabilidad de la tarea de agregación); salida de la tarea.
Acción: arreglar cron; ejecutar la tarea; esperar unos minutos.

### Etapas del embudo a cero o incoherentes
- Todo 0 tras «Iniciado»: seguimiento de finalización apagado en el sitio, en el curso o en las actividades; actividades ocultas.
- «Activos» mayor de lo esperado: cuenta cualquier actividad completada, dos o más.
- «Completado» 0 con gente avanzada: exige todas las actividades con seguimiento.
- «Calificación emitida» 0: no hay nota de aprobado, o nadie ha completado el curso.
- «Matriculados» mayor de lo esperado: incluye profesorado y otros roles matriculados; excluye matrículas suspendidas.
- Porcentajes «raros»: se calculan sobre la etapa anterior o sobre Activos, no sobre el total.
- Curso que no aparece en el sitio: está oculto.
Comprobar: línea «Actividades con seguimiento»; ajustes de finalización; libro de calificaciones.

### Un docente no ve un panel, una pestaña o un botón
- No ve «Pluginia Analytics» en Informes: no tiene el permiso de ver las estadísticas del curso.
- No ve Demografía, Satisfacción ni el panel de alumnos en riesgo: le falta el permiso de ver demografía y nombres (de fábrica solo gestor).
- No encuentra «Configurar mensajes automáticos»: está al final de la pestaña Resumen. En 1.1.0 solo se mostraba a quien veía el panel de alumnos en riesgo; desde 1.1.1 lo ve quien puede configurar mensajes. Si falta, comprobar versión y permiso.
- Ve «Alumno n.º N»: está activado «Ocultar la identidad de los alumnos».
- Cola de intervención vacía: necesita ambos permisos en el curso, curso visible y datos ya calculados.
Acción: ajustar permisos del rol o asignarlos solo en los cursos necesarios.

### Alumno en riesgo que no aparece (o aparece sin deberlo)
Construir la tabla: condición | dato del alumno | ¿se cumple?
- ¿Matrícula activa y usuario no suspendido?
- ¿Días matriculado mayores que el umbral efectivo del curso (curso > sitio > 14)?
- Nunca accedió: ¿ningún acceso al curso, ni siquiera uno?
- Inactivo: ¿días sin entrar mayores que el umbral? ¿progreso menor que el porcentaje? ¿tiene el curso actividades con seguimiento?
- ¿Ha completado el curso? Entonces nunca aparece.
- ¿Está más allá de los 50 listados? Entonces solo se cuenta.
- Señales tempranas: ¿alertas de comportamiento activadas? ¿registro estándar activo y sin purgar? ¿actividad con seguimiento? ¿mínimo de actividad previa?
- ¿Se han recalculado los datos después del cambio?

### No se envían mensajes automáticos
Comprobar en orden:
1. Licencia en vigor.
2. Cron y tarea «Enviar mensajes automáticos a alumnos» ejecutándose.
3. Curso visible (la tarea diaria omite los ocultos).
4. «Activar los mensajes automáticos» marcado y guardado.
5. Automatización correspondiente «Activada».
6. Hay alumnos que cumplen la condición (panel de alumnos en riesgo).
7. Plazo mínimo vencido para ese alumno (historial).
8. Tope de 200 por curso y ejecución.
9. El alumno sigue matriculado, no está suspendido y no es personal del curso (desde 1.1.1 el profesorado matriculado no recibe mensajes).
10. Entrega: preferencias de notificación del alumno y correo saliente de Moodle.
Si el historial muestra el envío, el plugin lo entregó a Moodle; el problema está en la entrega.

### Mensajes repetidos, inesperados o a quien no toca
- Se repite cada N días: comportamiento previsto mientras siga cumpliendo la condición; no hay tope.
- Llega tras acabar el curso: no se miran las fechas del curso; desactivar los mensajes.
- Lo recibe un docente matriculado: solo en 1.1.0; desde 1.1.1 el personal del curso se omite. Recomendar actualizar.
- Recibe una automatización distinta de la esperada: solo se envía la primera que cumple, por orden.
- Llega antes del plazo: registro de mensajes borrado por una conservación menor que el plazo.
- Texto en idioma inesperado: texto propio o plantilla del sitio (igual para todos) frente a texto incorporado (idioma del perfil).
- Marcador sin sustituir: mal escrito, con mayúsculas o inexistente.
- {days_inactive} vacío o {last_access} «nunca»: el alumno no ha entrado nunca.

### Resumen semanal o exportación programada
- No llega el resumen: opción sin marcar; semana sin actividad; curso oculto; notificación desactivada por el destinatario.
- Lo recibe quien no lo pidió: llega a todos los que pueden configurar los mensajes del curso.
- No llega la exportación: la dirección no corresponde a una cuenta de Moodle activa con acceso al panel del sitio; sin cursos con datos. En 1.1.0, además, mayúsculas distintas en el correo podían impedir la coincidencia en algunas bases de datos.

### Asistente de IA
- No aparece: proveedor «Desactivado» o sin clave; solo está en la pestaña Resumen.
- «Servicio de IA no disponible temporalmente»: clave de otro proveedor o sin saldo; modelo personalizado erróneo o de otro proveedor; cortafuegos o lista de bloqueo de Moodle; espera superior a 60 s.
- «Ha alcanzado el límite…»: límite por usuario y hora, compartido con «Redactar con IA».
- Dice que un dato no está disponible: grupo pequeño omitido, sección no permitida a ese usuario, o recorte por tamaño.
- Cifra distinta del panel: comprobar en el panel; el asistente puede equivocarse.

### Satisfacción, geografía y horas
- Satisfacción sin datos: nombres sin palabras clave; falta el plugin Questionnaire (NPS); valor manual que apunta a otra actividad.
- Geografía vacía: perfiles sin país y sin base GeoIP; muchos «sin ubicación».
- Horas de formación ausentes: campo sin asignar o cursos sin horas; nadie ha completado.

## Grado de certeza
Confirmado: evidencia directa del caso y regla aplicable.
Probable: mecanismo compatible, pendiente de una comprobación identificada.
No comprobable: falta la evidencia decisiva; decir cuál.

## Escalamiento al mantenedor
Ficha: versión, síntoma, comportamiento esperado, configuración relevante, reproducción anonimizada, ajustes probados y su resultado, evidencia que falta. No incluir código ni claves. No afirmar que se ha enviado sin instrucción expresa. Contacto: julio@rsmax.es.
