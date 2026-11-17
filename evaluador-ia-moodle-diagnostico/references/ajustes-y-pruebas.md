# Ajustes y pruebas antes de escalar

Revisado para la versión 1.8.0 el 17-11-2026.

## Regla de intervención
Buscar primero una solución con descripción de actividad, rúbrica o prompt. Revisar los tres y cambiar solo el elemento que explique el problema.
Conservar objetivos de aprendizaje, requisitos, criterios, niveles, puntos, ponderaciones y reglas de aprobación. No simplificar una rúbrica suprimiendo competencias necesarias.
Si un archivo pierde evidencia visual, comprobar alternativas de entrega admitidas y coherentes con la actividad; no prometer que cambiar una frase recuperará imágenes que no llegan al modelo.
No bajar el umbral de confianza ni activar publicaciones para ocultar un mapeo incompleto.

## Lista de revisión
| Elemento | Revisar | Ajuste que se puede probar |
|---|---|---|
| Descripción | Disponibilidad del caso, preguntas, límites y requisitos; contenido dentro de 8.000 caracteres efectivos | Eliminar duplicaciones, aclarar preguntas y situar instrucciones esenciales dentro del límite |
| Rúbrica | Método activo, niveles/puntos, criterios distinguibles, duplicados, descriptores observables | Corregir inconsistencias y distinguir etiquetas preservando la exigencia académica |
| Prompt | Niveles válidos, contradicciones, cobertura, tratamiento de evidencia, compatibilidad del formato | Valores discretos, reglas coherentes y una referencia inequívoca a cada criterio |
| Entrega | Formato, tamaño, ubicación de evidencia y límites de lectura | Preparar una copia de prueba que conserve la evidencia en un formato verificable |
| Tarea de Moodle | Flujo de trabajo de calificación, comentarios de retroalimentación, botón de envío, intentos adicionales, tipos de archivo | Activar el flujo de trabajo y los comentarios; exigir botón de envío; limitar los tipos de archivo a los que se leen |
| Página de AI Tutor de la tarea | Activación, usuario que firma, método, publicación, umbral, topes y texto de aviso | Ajustar un solo campo y repetir la entrega de prueba |
| Ajustes del sitio (administrador) | Licencia, proveedor, clave, modelo, modelo personalizado, dirección, transcripción y topes por hora | Corregir la clave o el modelo; vaciar el modelo personalizado; ajustar el tope por hora |

## Ajustes al alcance del cliente, por síntoma
| Síntoma | Ajuste que se puede probar |
|---|---|
| No se corrige ninguna entrega | Entregar con cuenta de alumno; activar AI Tutor en la tarea; revisar cron, licencia, clave y modelo personalizado |
| Solo se corrigen algunas | Subir el límite diario de la tarea, el máximo por alumno o los topes por hora |
| El alumno ve notas que debían quedar en revisión | Activar el flujo de trabajo de calificación en la tarea |
| Hay nota pero no comentario | Activar los comentarios de retroalimentación en la tarea |
| Cada cambio del alumno gasta una corrección | Exigir el botón de envío en la tarea |
| La parte visual no se valora | Pedirla como JPG o PNG de menos de 4 MB, hasta 5 por entrega; no usar DeepSeek |
| Tarda demasiado o no llega a responder | Probar un modelo más rápido; limitar la extensión de la entrega |
| AI Tutor aparece desactivado tras copiar el curso | Activarlo de nuevo; elegir el usuario que firma si la copia viene de otro sitio |
| El prompt y la rúbrica parecen contradecirse, o las notas no convencen | «Analizar prompt» en la página de AI Tutor de la tarea; revisar la propuesta y comprobarla con «Probar corrección» |
| No aparecen los botones de análisis y de prueba | Marcar la casilla de activar; si hay aviso de «no disponible», revisar licencia y clave de API del sitio |
| «Ha usado sus pruebas de hoy» | Esperar a medianoche o subir «Pruebas por usuario y día» en los ajustes del sitio |
| Entregas con la nota de «no se ha podido calificar automáticamente» | Revisar clave, saldo y modelo; matricular al usuario que firma con un rol que pueda calificar; probar un modelo más rápido |

Lo que el cliente no puede ajustar: recortes de caracteres, tamaños máximos, tiempo de espera, presupuesto de respuesta, duración del retraso, temperatura y ausencia de reintentos.

## Secuencia
1. Registrar una línea base del fallo, sin atribuir causas todavía.
2. Comparar los tres elementos y seleccionar un cambio único pertinente.
3. Entregar el texto o ajuste completo cuando haga falta; explicar la diferencia.
4. Desde 1.8.0, probar primero con «Probar corrección» en la página de AI Tutor de la tarea: usa la configuración escrita sin guardarla, no deja nada en Moodle y solo gasta pruebas del día del docente (20 de fábrica). Sirve para prompt, rúbrica, formatos y modelo. No sirve para comprobar publicación real, usuario que firma, cron, topes ni reentregas: para eso, seguir con el paso siguiente.
4b. Usar una actividad de prueba, un participante de prueba con rol de alumno y una entrega anonimizada idéntica. Cada repetición gasta una de las calificaciones de ese alumno en la tarea y una petición del límite diario: subir ambos topes en la actividad de prueba o usar varios alumnos de prueba. Mantener versión, proveedor/modelo, rúbrica, escala y demás opciones.
5. Para variabilidad, proponer tres ejecuciones por condición. No ejecutarlas automáticamente si tienen coste o afectan calificaciones; pedir que las realice el responsable o usar autorización existente.
6. Comparar los niveles guardados por criterio, el comentario, la suma directa, la nota transformada por Moodle y el estado de publicación.
7. Repetir con otro ajuste pertinente si el resultado lo justifica. No mezclar cambios sin registrar su efecto.
8. Si las alternativas probadas no resuelven el síntoma, preparar una solicitud de cambio de código al administrador.

## Registro de prueba
| Ensayo | Cambio único | Entrega y configuración | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñado; simulación ejecutada; ejecutado en Moodle; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
Una simulación con respuestas inventadas puede demostrar un mecanismo, pero no qué devolvió el proveedor en una evaluación pasada.
No afirmar que tres repeticiones demuestran ausencia de errores en todos los casos.

## Aceptación
Todos los criterios deben tener un nivel válido. El feedback debe concordar con las selecciones. La suma debe ser correcta y la transformación de Moodle debe verificarse por separado. La publicación debe respetar la configuración.
Para una respuesta académicamente incompleta, aplicar el descriptor que corresponda; no confundir «nivel bajo» con «criterio sin seleccionar».

## Solicitud final al administrador
Preparar únicamente tras pruebas de ajustes insuficientes:
- Versión instalada, síntoma y resultado esperado.
- Descripción, rúbrica, prompt y entrega anonimizados relevantes.
- Ajustes probados y resultados reales, diferenciados de simulaciones.
- Fallo residual y evidencia disponible o pendiente.
- Cambio funcional solicitado y criterios de aceptación; no código fuente.
- Comprobación de que no se intenta resolver una contradicción docente pendiente.

Si la ejecución está bloqueada, entregar el plan preparado y declarar el bloqueo; no afirmar que los ajustes han fallado ni solicitar desarrollo como siguiente paso automático.
