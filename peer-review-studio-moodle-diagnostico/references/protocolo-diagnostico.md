# Protocolo de casos

## Ficha mínima
Pedir solo lo que haga falta para la consulta; nunca claves ni acceso de administrador. Datos anonimizados.
- Versión de Moodle y del plugin.
- Modo de flujo de trabajo; si es Manual, fase actual; si es Programado, las tres fechas y la fecha de hoy.
- «Revisiones que cada alumno debe completar», «Objetivo de revisiones recibidas por entrega», asignación automática, modo del grupo de revisores, recíprocas, días de recordatorio y de reasignación.
- Máximos de entrega y de revisión; si hay IA: casilla, respaldo y peso.
- Número de alumnos con entrega; grupos y modo de grupo si se usan.
- Del caso concreto: estado de la entrega en el panel, revisiones recibidas y hechas, lo que aparece en «Requiere atención», el desglose de nota de la página de la entrega y el mensaje exacto en pantalla.
- Si el cron funciona: última ejecución de la tarea del plugin.
Para notas: los niveles elegidos en cada revisión recibida, o al menos la nota que propone cada una, y si hay nota de IA o nota fijada por el docente.

## Árbol: síntoma, causas, comprobación

### Nadie tiene revisores asignados
1. Programado y aún no ha pasado el cierre: es lo esperado; se reparte tras el cierre.
2. Manual en fase Entrega, Feedback o Cerrada: no se reparte; pasar a Asignación o Revisión.
3. Cron parado: ver la última ejecución de la tarea; probar «Emparejar revisores ahora».
4. Asignación automática desmarcada: aparece «Pendiente de asignación manual».
5. Menos de dos entregas: no hay a quién asignar.

### Una entrega no consigue revisores («No hay ningún revisor elegible»)
Mirar el resumen de bloqueados en la página de la entrega: no está en el mismo grupo, está en el mismo grupo, recíprocas bloqueadas, ya fue emparejado antes, ya no es participante activo. Causas: grupo pequeño, autor sin grupo con «mismo grupo», recíprocas en grupo pequeño, todos los candidatos ya pasaron por esa entrega, objetivo mayor que los candidatos.

### Un alumno no tiene nada que revisar o tiene menos de las requeridas
1. No ha entregado: no puede revisar.
2. Ha entregado tarde respecto a los demás (Abierto) o fue el último en la cola: reparto desigual conocido.
3. Objetivo por entrega menor que las requeridas por alumno.
4. Reglas de grupo o recíprocas.
5. No tiene el permiso de revisar o está suspendido en el curso.
Comprobar la columna «Revisiones hechas» y los pendientes del alumno en el panel.

### Al alumno le han quitado una revisión
Superó los días de reasignación, o un tutor volvió a emparejar, o terminó el plazo. En Manual, comprobar cuánto tiempo pasó la actividad en fase Asignación antes de abrir Revisión.

### No llegan recordatorios o avisos
Umbral a 0; ya se envió el único recordatorio; cron parado; correo saliente de Moodle; preferencias del usuario; la actividad está oculta o restringida para ese usuario; en Programado el reloj empieza en el cierre.

### El alumno no ve su nota o su feedback
1. Feedback no publicado: Programado antes de la fecha límite; Manual fuera de Feedback o Cerrada; Abierto con la entrega sin completar sus revisiones.
2. Programado con plazo vencido y cron parado.
3. Entrega sin ninguna revisión: no hay nota; ver si está escalada.
4. Abierto y «Revisada parcialmente» de forma indefinida: falta un revisor posible.
Comprobar en la página de la entrega el texto «Esta nota todavía no es visible para el estudiante…».

### La nota no cuadra
Rehacer: nota de cada revisión por la rúbrica; media; mezcla con IA según el peso si hay nota de IA; nota de revisión por proporción y, con IA, por calidad; suma; o nota fijada por el docente. Causas frecuentes: el nivel más bajo no vale cero; pesos distintos de 1; la IA entró después y cambió la nota; revisión con calidad baja de IA; máximos cambiados; nota fijada por el docente; el alumno espera puntos de revisión sin tener nota de entrega.

### El libro de calificaciones está vacío
Mismo origen que el feedback no publicado, o suma de máximos igual a 0.

### No se puede activar la IA o no califica
1. Mensaje bajo la casilla: sin proveedor, o IA desactivada en el curso.
2. Autor o revisor sin aceptar la política de IA: «La revisión con IA está en espera…».
3. Entrega con un fichero no legible, vacía de texto o demasiado larga.
4. La entrega aún no ha recibido ninguna revisión: la IA actúa tras la primera.
5. Fallo o límite del proveedor: reintentos en curso o abandonados; pedir al administrador la prueba de IA y las tareas en segundo plano.
6. Respaldo: solo actúa con cero revisiones y tras el escalado.

### El profesor no puede entregar ni revisar al probar
Esperado: usar una cuenta con rol de estudiante.

## Grado de certeza
Confirmado: evidencia directa del caso más regla documentada. Probable: mecanismo compatible, pendiente de una comprobación concreta. No comprobable: falta un dato decisivo; decir cuál.

## Escalamiento al mantenedor
Preparar una ficha con versión, modo y ajustes relevantes, síntoma, comportamiento esperado, pasos anonimizados para reproducirlo, ajustes ya probados con su resultado, y criterio de aceptación. Sin código, sin datos personales. No afirmar que se ha enviado.
