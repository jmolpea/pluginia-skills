# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero una solución con lo que el cliente controla. Cambiar una sola cosa cada vez y anotar el resultado real. No proponer bajar protecciones (consentimiento, redacción, límites) para «arreglar» un síntoma que tiene otra causa.

## Qué puede ajustar el cliente
| Palanca | Dónde | Sirve para |
|---|---|---|
| Proveedor, modelo y topes | IA de Moodle | Errores de petición, lentitud, calidad, ritmo de los resúmenes. |
| Ajustes del bloque | Página de ajustes del plugin | Límites, coste, datos enviados, catálogo, resultados, avisos, privacidad. |
| Datos de los cursos | Cada curso | Nombre, descripción, etiquetas, campos, fechas, visibilidad: mejoran la preselección y el resumen. |
| Matriculación | Métodos de cada curso | Que un curso sea candidato y tenga «Matricularme». |
| Rutas | Gestionar rutas de aprendizaje | Contenido, orden, descripción y visibilidad. |
| Permisos | Definir roles | Quién usa el bloque, gestiona rutas o ve el informe. |
| Tareas | Tareas programadas de Moodle | Horario, activación y ejecución manual. |
| Preferencias de notificación | Mensajería del sitio y de cada usuario | Canal de los avisos. |

## Preparación de una prueba
1. Usar un usuario de prueba con rol normal, no matriculado en los cursos que se quieren ver, con el perfil rellenado como un usuario real.
2. Anotar la línea base: mensaje del bloque, cursos mostrados y fila del informe.
3. Cambiar una variable.
4. Forzar un ranking nuevo de forma legítima: editar una respuesta en «Cambiar mis intereses» y pulsar «Guardar y actualizar». Recordar que consume una petición del límite diario.
5. Comparar con la línea base y mirar la nueva fila del informe.
6. Deshacer el cambio si no aporta.
Avisar del coste: cada ranking, resumen, descripción o imagen es una petición de pago al proveedor.

## Pruebas controladas habituales
| Pregunta | Prueba | Resultado esperado |
|---|---|---|
| ¿Funciona la conexión con la IA? | Usuario de prueba responde una pregunta. | Aparecen tarjetas y una fila «Ranking» con éxito en el informe. |
| ¿Es candidato este curso? | Crear un curso visible, sin fecha de fin, con automatriculación sin clave, en una categoría permitida; responder algo que encaje claramente con su título. | Aparece, con «Matricularme». Si no, repasar condiciones una a una. |
| ¿Actúa el filtro por categoría? | Activarlo con una sola categoría y pedir ranking nuevo. | Solo cursos de esa categoría y subcategorías. |
| ¿Actúa el campo de exclusión? | Marcar la casilla en un curso recomendado y recargar. | Desaparece sin nueva petición. |
| ¿Funciona la caché? | Recargar la página dos veces sin cambiar nada. | Mismo resultado y ninguna fila nueva de ranking. |
| ¿Funciona el límite diario? | Ponerlo en 1 en un sitio de pruebas y cambiar respuestas dos veces. | La segunda vez, ranking anterior con aviso de límite. |
| ¿Cambia el tono? | Escribir un prompt institucional muy marcado y pedir ranking nuevo. | Motivos con ese tono; la lista de cursos sigue saliendo solo del catálogo. |
| ¿Se ocultan los pulgares abajo? | Valorar «No me sirve» y recargar. | El elemento desaparece; vuelve tras el plazo configurado. |
| ¿Se generan resúmenes? | Ejecutar la tarea de resúmenes y mirar el informe. | Filas «Resumen de curso»; si se detiene pronto, tope del proveedor. |
| ¿Llegan avisos? | Con un usuario que ya tiene ranking: crear un curso candidato muy afín, esperar a que tenga resumen, ejecutar la tarea de cursos nuevos (respetando las 12 horas entre revisiones). | Fila «Ranking de cursos nuevos» y aviso si la puntuación alcanza el umbral. |
| ¿Funciona la matrícula de ruta? | Ruta con un curso con automatriculación sin clave y otro con clave. | Matricula en el primero y explica el motivo del segundo. |
| ¿Qué recibe la IA del perfil? | Desmarcar campos de perfil y pedir ranking nuevo. | Motivos que ya no aluden a esos datos. El plugin no ofrece vista del texto enviado. |

## Registro de ensayo
| Ensayo | Cambio único | Usuario y configuración | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados: diseñado; ejecutado por el cliente; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
Una respuesta de la IA en una prueba no demuestra qué respondió en un caso pasado: el plugin no guarda las respuestas completas.

## Qué no se puede resolver con ajustes (decirlo con claridad)
- Poner el bloque dentro de un curso o tener ajustes distintos por instancia.
- Recomendar a invitados o a personas sin sesión.
- Matrícula directa en cursos con clave, pago u otros métodos.
- Obligar a la IA a recomendar un curso concreto o fijar su posición.
- Ver o exportar el texto exacto enviado a la IA y su respuesta completa.
- Cambiar los límites fijos (1.000 caracteres por respuesta, 6 preguntas, 3 avisos por ejecución, etc.).
- Elegir un proveedor o modelo distinto solo para este bloque: usa el de Moodle.
- Un límite diario «sin límite»: el mínimo es 1 (se puede poner un valor alto).
- Detener el gasto de la tarea nocturna con el interruptor de avisos (hay que desactivar la tarea o bajar usuarios por ejecución).

## Solicitud final al mantenedor
Preparar solo tras pruebas insuficientes: versiones, síntoma y esperado, ajustes probados con resultados reales, fallo residual, cambio funcional pedido y criterio de aceptación. Sin código y sin datos personales. No afirmar que se ha enviado.
