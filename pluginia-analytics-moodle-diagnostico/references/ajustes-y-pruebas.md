# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero la solución en la configuración. Cambiar solo el elemento que explica el síntoma y comprobar el efecto antes de tocar otro.
No proponer bajar la privacidad (umbral de supresión, ocultar identidad, permisos) para «hacer aparecer» datos sin advertir de la consecuencia.
No proponer envíos reales a alumnos como prueba. Las pruebas de mensajes se hacen en un curso de pruebas con usuarios de prueba.
Recordar que casi todo cambio necesita un recálculo: esperar a la tarea horaria o pulsar «Actualizar datos» y recargar a los pocos minutos.

## Lista de revisión
| Capa | Revisar | Ajuste que puede hacer el cliente |
|---|---|---|
| Moodle | Cron, seguimiento de finalización, registro estándar, nota de aprobado, correo saliente | Activar o corregir lo que marque la Auditoría de preparación |
| Sitio | Licencia, umbrales de riesgo, alertas de comportamiento, supresión, identidad, IA | Cambiar el ajuste concreto en la página del plugin |
| Permisos | Qué rol ve qué | Dar o quitar un permiso al rol, en el sitio o en un curso |
| Curso | Interruptor de mensajes, umbrales propios, plazo mínimo, resumen | Formulario «Mensajes automáticos» |
| Automatización | Estado, valor de su condición, asunto y texto, capa de la que sale el texto | Editar, Activar/Desactivar, Restaurar el texto por defecto |
| Actividades | Nombres para satisfacción, seguimiento de finalización, visibilidad | Renombrar o configurar la actividad |

## Pruebas controladas (una variable cada vez)

### P1. ¿Se calculan los datos?
1. Anotar la fecha de «Analíticas calculadas» en un curso.
2. Pulsar «Actualizar datos», esperar 5 minutos y recargar.
3. Esperado: la fecha cambia. Si no, revisar cron y tareas puntuales.

### P2. ¿Cuenta el embudo lo que espero?
1. En un curso de pruebas con 3 actividades con seguimiento, matricular un usuario de prueba.
2. Sin entrar: Matriculados +1. Tras entrar: Iniciado +1. Tras completar 2: Activos y 50% completado +1. Tras completar las 3: Completado +1.
3. Recalcular entre pasos (P1). Registrar cada cifra.

### P3. ¿Quién se señala como en riesgo?
1. En el curso de pruebas, poner «Inactividad para estar en riesgo (días)» en 1 y guardar.
2. Usuario A: matriculado hace más de un día, sin entrar. Usuario B: entró hace más de un día y completó menos del porcentaje.
3. Recalcular. Esperado: A en «Nunca accedió», B en «Inactivo». Cambiar solo el porcentaje de progreso y repetir para ver salir a B.

### P4. Envío de mensajes
1. Con P3 preparado, activar los mensajes, guardar y revisar la vista previa de cada automatización.
2. Pulsar «Enviar mensajes ahora». Anotar «N enviados, N omitidos (plazo mínimo), N error(es)».
3. Comprobar el historial y la notificación del usuario de prueba (campana y correo).
4. Pulsar de nuevo: esperado 0 enviados y los anteriores omitidos por plazo.

### P5. Orden y exclusividad
Con un usuario que cumpla dos condiciones, comprobar que recibe solo la primera automatización activada. Desactivar esa y, vencido el plazo, comprobar que recibe la siguiente.

### P6. Capas del texto
1. Sin tocar nada: el usuario de prueba con idioma inglés recibe el texto incorporado en inglés.
2. Guardar un texto propio en el curso: todos reciben ese texto.
3. «Restaurar el texto por defecto»: vuelve a la capa inferior. Comprobar la columna «Texto del mensaje».

### P7. Permisos
Entrar con un usuario de prueba con el rol afectado y anotar qué ve. Dar un único permiso y repetir.

### P8. Privacidad
Cambiar solo el umbral de supresión (por ejemplo de 0 a 5), recalcular y comparar un desglose con un grupo pequeño: «≤ 5» en el curso, omitido en el sitio.

### P9. Asistente de IA
1. Vaciar «ID de modelo personalizado», dejar «Valor recomendado», guardar.
2. Hacer una pregunta de ejemplo en un curso con datos.
3. Si falla, probar con otra clave recién creada del mismo proveedor. Cambiar solo una cosa cada vez. Cada intento consume del límite por hora y tiene coste.

## Registro de prueba
| Ensayo | Cambio único | Curso y usuarios | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados: diseñado; ejecutado en Moodle; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
No dar por ejecutada una prueba que solo se ha descrito.

## Aceptación
El síntoma desaparece en la prueba, las cifras se explican con las reglas documentadas, los permisos son los deseados y no se ha debilitado la privacidad sin decisión expresa del responsable.

## Solicitud final al mantenedor
Preparar solo tras ajustes probados e insuficientes:
- Versión instalada de Moodle y del plugin, síntoma y resultado esperado.
- Configuración relevante (capturas, sin claves).
- Pruebas realizadas y resultado de cada una.
- Comportamiento funcional que se solicita y criterio de aceptación.
- Datos anonimizados. Sin código fuente.
Ejemplos de peticiones que son cambios de producto y no de configuración: tope de mensajes por alumno, dejar de enviar al terminar el curso, excluir al profesorado matriculado, exportar más de 50 alumnos por grupo, acceso a la configuración de mensajes sin ver nombres.
