# Protocolo de diagnóstico

## Ficha mínima
Pedir solo lo que haga falta para la consulta:
- Versión de Moodle y del plugin (Administración del sitio › Extensiones › Vista general).
- Qué proveedor de IA tiene Moodle y si «Generar texto» (y «Generar imagen») están activados. No pedir la clave.
- Dónde está el bloque (portada o Área personal) y con qué rol se prueba. Pedir que se pruebe con un usuario normal, no solo como administrador.
- Mensaje exacto que se ve en el bloque.
- Valores de los ajustes relacionados con el síntoma.
- Fila de «Peticiones a la IA» del informe (tipo, éxito, error, duración, tokens), con el usuario oculto.
- Para un curso ausente: visibilidad, fechas, categoría, métodos de matriculación activos y si la persona ya está matriculada.
- Estado del cron y última ejecución de las tareas del plugin.
No pedir acceso administrativo ni datos personales. Para una pregunta simple no exigir la ficha.

## Árbol síntoma → causas → comprobación
### El bloque no aparece o está vacío
1. No hay proveedor con «Generar texto» → la primera línea de los ajustes del plugin lo dice; el administrador ve un aviso en el bloque.
2. Usuario invitado o sin sesión → probar con cuenta real.
3. Rol sin el permiso de uso → revisar el permiso en el rol de usuario identificado.
4. No está añadido en esa página, o la persona personalizó su Área personal antes de añadirlo por defecto → reiniciar el Área personal.
5. Se intenta añadir dentro de un curso → no es posible; solo portada y Área personal.

### «Ahora mismo no hay cursos disponibles que encajen con tus intereses»
1. No hay candidatos → recorrer la tabla de condiciones; lo más frecuente: sin automatriculación activa, filtro por categoría sin categorías, ningún método marcado, la persona ya está en todos los cursos.
2. Hay candidatos pero la IA no devolvió ninguno con puntuación suficiente → respuestas muy alejadas del catálogo; probar otras respuestas.
3. Todo lo devuelto está oculto por pulgares abajo recientes.
Distinguir 1 de 2 con el informe: si no hay petición de ranking registrada en ese momento, no había candidatos.

### «Ahora mismo no podemos obtener recomendaciones…»
La petición falló o la respuesta no tuvo el formato esperado dos veces. Mirar el error en el informe: clave o saldo del proveedor, modelo inexistente, tope de peticiones, tiempo de espera, entrada demasiado larga (bajar «Máximo de cursos por petición»). Si hay éxito en el registro pero error en pantalla, la respuesta era ilegible: probar otro modelo.

### Mensajes de límite
«Has alcanzado el límite de hoy…» o «…límite diario…»: ajuste «Peticiones a la IA por usuario y día». Desde 1.0.0-beta5 el mínimo es 1; en un sitio actualizado desde una versión anterior, comprobar que no quedó guardado un 0. Recordar que cuentan fallos y reintentos y que se reinicia a la medianoche del usuario.

### Un curso concreto no se recomienda
Tabla por condición: visible, no terminado, persona no matriculada, método marcado y en plazo, plazas y cohorte, categoría permitida, sin exclusión, visible para la persona. Si todas se cumplen: ¿supera el catálogo el máximo por petición? (preselección por palabras) ¿tiene pulgar abajo de esa persona? ¿la IA lo puntuó bajo? Lo último no es un fallo: mejorar nombre, descripción, etiquetas y campos del curso.

### Recomendaciones poco acertadas o con datos antiguos
Respuestas vagas; cursos sin descripción ni etiquetas; resúmenes pendientes (tarea horaria o tope del proveedor); prompt institucional contradictorio; modelo demasiado limitado. Un curso con datos cambiados se actualiza cuando se rehace su resumen.

### No aparece «Matricularme»
Solo con automatriculación sin clave y si Moodle admite a esa persona. Con clave, pago u otros métodos se ofrece «Ver curso». Si «Automatriculación» no está marcada en «Métodos de matriculación», no hay matrícula directa.

### Rutas
- No se recomiendan: «Recomendar rutas de aprendizaje» apagado, ruta oculta, o ninguno de sus cursos es candidato para esa persona.
- Curso «No disponible ahora» con el motivo «No se te puede matricular en este curso desde el recomendador…»: tiene la automatriculación abierta pero queda fuera por el filtro de categoría, el campo de exclusión o los métodos de matriculación marcados. En versiones anteriores a 1.0.0-beta5 ese caso mostraba, por error, que el curso no permitía la automatriculación.
- No aparece «Generar imagen con IA»: no hay proveedor de imagen. Error al generar: leer el mensaje del proveedor que muestra el formulario.
- No deja guardar: hay un curso oculto seleccionado o falta título o cursos.

### No llegan avisos de cursos nuevos
Cron parado; tarea desactivada; «Avisar de cursos nuevos» apagado; puntuación por debajo del umbral; la persona no ha entrado en el plazo de actividad, no aceptó condiciones o política, o no tiene ranking; aún no le ha tocado el turno (usuarios por ejecución); el curso no cuenta como nuevo; preferencias de notificación del usuario; el correo está desactivado de fábrica.

### Coste más alto de lo esperado
Revisar en el informe qué tipo de petición domina. Rankings: caché corta, cambios frecuentes del prompt institucional o de cursos, límite diario alto. Resúmenes: catálogo que cambia mucho. Ranking de cursos nuevos: tarea nocturna (sigue activa aunque los avisos estén apagados).

### Informe
Error al pulsar el filtro de fechas: fallo de versiones anteriores a 1.0.0-beta5; actualizar. Página en blanco de datos: periodo sin actividad o datos ya borrados por la conservación. CTR bajo: «Veces mostrado» cuenta cada carga. Tokens vacíos: el proveedor no los comunica.

## Grado de certeza
Confirmado: evidencia directa del caso y regla aplicable. Probable: mecanismo compatible, pendiente de una comprobación identificada. No comprobable: falta la evidencia decisiva; decir cuál.

## Escalado al mantenedor
Solo tras probar ajustes. Ficha: versiones, síntoma, esperado, ajustes relevantes, pasos de reproducción anonimizados, ensayos y resultados, evidencia que falta. No incluir código ni datos personales. Contacto de soporte indicado en el manual público.
