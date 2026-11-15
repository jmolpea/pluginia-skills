# Protocolo de casos

## Ficha mínima
Pedir según la consulta, nunca todo por sistema:
- Versión de Moodle y del plugin. Proveedor de IA elegido (subsistema de Moodle o directo) y modelo.
- Ajustes de la actividad relevantes: justificación, intentos, método de calificación, calificación máxima, revisión docente, límite de tiempo y sección de IA.
- Estado del intento y, si hay IA, estado de la evaluación, estado de revisión, confianza, alertas y mensaje de error tal como se ven en «Revisar intentos» o en el resultado.
- Para dudas de nota: desglose por criterios del resultado, ruta de decisiones y la comprobación de la puntuación del constructor.
- Para dudas del escenario: mensaje literal de error y, si procede, el escenario exportado sin datos de personas.
- Para la IA: resultado de «Probar la conexión con la IA» y si el cron de Moodle se ejecuta.
No pedir claves, contraseñas ni acceso administrativo. Pedir que se anonimicen las justificaciones.

## Árbol síntoma → causas → comprobación

### No aparece la sección «Evaluación con IA» en la actividad
Causa: el administrador no ha activado las funciones de IA. Comprobación: ajustes del sitio. Certeza alta si el ajuste está apagado.

### Un intento terminado no tiene evaluación de IA ni aparece pendiente
Causas posibles: IA no activada en la actividad; sin proveedor disponible en ese momento; el alumno no escribió ninguna justificación; la IA se activó después de terminar el intento.
Comprobación: ajustes de la actividad, justificaciones en la ruta de decisiones, página de prueba. La evaluación solo se solicita al terminar el intento o al relanzarla.

### Evaluación en «Pendiente» durante mucho tiempo
Causa probable: el cron de Moodle no se ejecuta o las tareas puntuales están atascadas. Comprobación por el administrador en la lista de tareas ad hoc y en el estado del cron. No es un fallo del proveedor mientras no cambie de estado.

### «Fallback aplicado» o incidencia «Crítica»
Leer el mensaje de error (requiere el permiso de ver detalles de la IA; por defecto, profesor con edición y gestor).
- Falta la clave de API: escribirla o cambiar de proveedor.
- Ningún proveedor del sitio ofrece generación de texto: configurar uno en la IA de Moodle.
- Error con código 401: clave incorrecta. 404: modelo inexistente o retirado. 429: saldo o límite de peticiones. 400: el modelo rechaza la petición; probar otro.
- Respuesta no válida: el modelo no devolvió el formato pedido; relanzar y, si se repite, cambiar de modelo.
- El proveedor ha rechazado responder: filtros de contenido del proveedor; revisar el texto.
- Modelo no válido: el modelo de la actividad no está en la lista permitida.
- Error de conexión o tiempo agotado: red del servidor o tiempo de espera corto.
Después de corregir, un docente con permiso de calificar relanza la evaluación. No hay reintento automático.

### La IA terminó pero el alumno no ve nada
Comprobar por orden: ajuste de feedback al alumnado en «Nada»; evaluación pendiente de revisión (aprobación obligatoria, confianza bajo el umbral o alertas); evaluación rechazada por el docente; intento «Entregado» esperando revisión docente. Solución habitual: abrir el intento y guardar la revisión.

### El docente revisó y la IA sigue «Pendiente de revisión»
Causa probable: la revisión se publicó antes de que la IA terminara. Comprobación: fechas. Solución: volver a guardar la revisión.

### La nota no cambió aunque la IA cuenta para nota
Causas: modo «Solo feedback»; evaluación retenida; evaluación fallida; intento con revisión docente obligatoria o ya revisado (la combinada solo se sugiere). Comprobar el estado y la línea de puntuación combinada que ve el docente.

### La nota por reglas no es la esperada
1. Revisar el desglose por criterios y la ruta de decisiones.
2. Identificar el modo de cada criterio: variables, solo puntos o automático de versiones anteriores.
3. Comprobar si los criterios suman la calificación máxima; si no, hay reescalado.
4. Comprobar variables que tocan su mínimo o máximo: los efectos sobrantes se pierden.
5. Comprobar el sentido de cada variable.
6. Si el escenario se editó después del intento, la nota del intento no se recalcula.
7. Reproducir el recorrido con «Probar escenario», que muestra la puntuación que obtendría.

### Todas las notas salen parecidas, o nadie llega al máximo
Mirar la comprobación de la puntuación del constructor. Ajustar efectos, valores iniciales o puntos.

### El alumno no ve su nota
Intento «Entregado» con revisión docente obligatoria, o intento aún «En curso».

### Intento «En curso» con el tiempo agotado
En la 0.8.1 se cierra solo: al instante si el alumno vuelve a entrar y, si no, por la tarea programada de cierre pasados 5 minutos (se ejecuta cada 10). Si sigue abierto más de un cuarto de hora, comprobar con el administrador que el cron funciona y que esa tarea programada no está desactivada. En la 0.8.0 es el comportamiento previsto: se cierra cuando el alumno vuelve a entrar o se elimina.

### «Has alcanzado el número máximo de intentos»
Los intentos en curso también cuentan. Subir el límite o eliminar un intento.

### El docente no puede hacer la actividad
Los roles docentes no tienen el permiso de realizar el escenario. Usar «Probar escenario» o cambiar de rol.

### No se puede guardar o importar un escenario
Leer el mensaje: indica el primer problema (nodo de entrada, destino inexistente, variable desconocida en un efecto, criterio inválido, identificador con caracteres no admitidos, texto sin escenario reconocible). Corregir ese punto y repetir. En importaciones desde un asistente de IA, pegar la respuesta completa.

### No se pueden guardar los ajustes de la actividad
Mensajes habituales: la IA exige justificación; peso entre 1 y 100; confianza entre 0 y 1; criterios de la IA no válidos (más de 8, peso no positivo); número máximo de decisiones fuera de rango; calificación máxima no positiva; modelo no permitido.
«Intentos a finalizar» mayor que «Intentos permitidos»: el formulario lo rechaza desde la 0.8.1.
Si el formulario vuelve a mostrarse sin ningún mensaje visible, con IA activada en la actividad y el sitio cambiado al subsistema de IA de Moodle (o con un modelo retirado de la lista), comprobar la versión: es un defecto de la 0.8.0 corregido en la 0.8.1, donde el formulario ofrece el modelo por defecto. Recomendar actualizar; como alternativa temporal en la 0.8.0, que el administrador valore volver al proveedor anterior para guardar.

### Evaluación de IA fallida en un curso restaurado, con el aviso de que estaba pendiente en la copia
No es un fallo del proveedor: la evaluación estaba en cola cuando se hizo la copia de seguridad. Relanzarla desde el resultado del intento.

### «Esta actividad no está disponible en este momento»
El escenario guardado no es válido. Un docente con edición ve el motivo en la página de la actividad.

### La IA comenta [PERSON] u otras marcas
Es el enmascarado. En modo estricto afecta a nombres propios no personales.

### Feedback de la IA en un idioma inesperado
Se usa el idioma forzado del curso; si no hay, el del perfil del alumno; si no, el del sitio.

## Grado de certeza
Confirmado: evidencia directa del caso y regla aplicable.
Probable: mecanismo compatible con el síntoma, pendiente de una comprobación identificada.
No comprobable: falta evidencia decisiva; explicar qué dato permitiría avanzar.

## Escalamiento
Entregar una ficha breve: versiones, síntoma, comportamiento esperado, configuración relevante, reproducción anonimizada, resultados observados, hipótesis descartadas y evidencia faltante.
Para solicitar un cambio, añadir los ajustes probados, el resultado de cada uno, el fallo residual, el comportamiento funcional solicitado y los criterios de aceptación. No incluir código ni afirmar que la solicitud ha sido enviada.
