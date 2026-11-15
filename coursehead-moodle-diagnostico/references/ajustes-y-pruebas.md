# Ajustes y pruebas antes de escalar

## Regla de intervención
Resolver primero con lo que el cliente puede cambiar: ajustes del sitio, permisos, casillas del curso y su propio CSS o JavaScript. Cambiar una sola cosa cada vez y anotar el resultado.
No proponer activar JavaScript ni ampliar permisos como atajo. No proponer vaciar «Rutas excluidas» ni activar calificaciones para «que se vea en todas partes» sin explicar el riesgo.

## Lo que el cliente puede ajustar
| Capa | Quién | Ajustes disponibles |
|---|---|---|
| Sitio | Administrador | Los tres interruptores, las tres casillas de tipo de página, rutas excluidas, longitudes máximas, advertencias, estrategia por defecto |
| Permisos | Administrador | Conceder o retirar los tres permisos a un rol, en el sitio o en un curso concreto |
| Curso | Gestor o rol autorizado | Las tres casillas, el contenido, la estrategia de carga, eliminar |
| Código propio | Quien lo escribe | Selectores, prioridad de reglas, espacios en comparaciones, momento de ejecución del programa |

## Lo que no se resuelve con ajustes (versión 1.2.1)
- Personalizar por sección, grupo, rol o usuario; personalizar la portada del sitio.
- Excluir una actividad concreta por su número, o elegir tipos de página por curso.
- Recuperar una versión anterior del código.
- Sobrescribir los recursos de un curso de destino al restaurar.
- Que el formulario avise de errores de sintaxis.
Alternativas honestas: en CSS se puede acotar una regla a una página, sección o actividad con los identificadores que Moodle pone en cada página; guardar copias del código fuera de Moodle; eliminar los recursos del destino antes de restaurar.

## Pruebas controladas
Preparación: un curso de prueba, una cuenta de gestor y una de alumno, una ventana privada del navegador para la cuenta de alumno.

P1. Circuito mínimo de CSS. Guardar una única regla muy visible sobre el fondo de la página. Esperado: mensaje de guardado, panel «Activado» con dirección de CSS y revisión; el fondo cambia en la página principal para gestor y alumno.
P2. Revisión. Guardar un cambio mínimo. Esperado: la revisión cambia y el efecto se ve al recargar, sin purgar cachés.
P3. Interruptor del curso. Desmarcarlo y guardar. Esperado: «Desactivado», sin efecto, código intacto en el formulario.
P4. Tipos de página. Con P1 activo, abrir principal, una actividad, calificaciones, participantes y editar ajustes. Esperado según las casillas del sitio; administración, nunca.
P5. Ruta excluida. Añadir la ruta de una actividad de prueba, guardar y recargar. Esperado: sin efecto solo en las páginas que empiezan por esa ruta. Retirar la línea al terminar.
P6. Validación. Pegar el CSS envuelto en su etiqueta. Esperado: error que nombra el fragmento, nada guardado.
P7. Acceso. Abrir la dirección del CSS que muestra el panel con una cuenta sin acceso al curso o sin sesión. Esperado: respuesta de prohibido, sin contenido.
P8. JavaScript, solo si está permitido. Un programa de una línea que escriba un mensaje en la consola. Esperado: aparece en la consola del alumno en las páginas permitidas y no en el intento de cuestionario.
P9. Permisos. Con un rol que solo tenga gestionar y editar CSS. Esperado: ve el campo de CSS y el aviso de no disponible en JavaScript; al guardar, el JavaScript existente no cambia; si el curso tiene JavaScript guardado, no ve el botón de eliminar (1.2.1).
P10. Restauración. Duplicar el curso con un gestor y con un profesor. Esperado: con gestor se conserva; con profesor sin permisos se descarta y el registro de la restauración lo avisa.

## Registro de prueba
| Prueba | Cambio único | Página y cuenta | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñada; ejecutada por el cliente; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
Lo que el cliente no ha ejecutado no está probado. Un resultado en un tema no garantiza el mismo en otro.

## Aceptación
El panel refleja lo esperado, el efecto se ve con cuenta de alumno en las páginas previstas y no en las excluidas, y la consola del navegador no muestra errores nuevos.

## Solicitud final al mantenedor
Solo tras ajustes probados e insuficientes: versión de Moodle y del plugin, tema, síntoma y resultado esperado, pruebas ejecutadas con su resultado, síntoma residual, comportamiento funcional que se solicita y criterio de aceptación. Sin código del plugin y sin datos personales. No enviarla sin instrucción expresa.
