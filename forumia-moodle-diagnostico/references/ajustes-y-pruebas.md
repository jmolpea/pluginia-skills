# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero la solución en lo que el cliente puede cambiar. Cambiar una sola cosa cada vez y anotar el resultado real.
No subir límites ni activar la calificación automática para «hacer desaparecer» un síntoma sin entender su causa.
Avisar siempre de que cada prueba consume peticiones del proveedor y cuenta en los límites diarios.

## Qué puede ajustar el cliente
| Ámbito | Ajuste | Efecto esperado |
|---|---|---|
| Sitio | Proveedor, clave y modelo | Restablece el servicio; cambia calidad, velocidad y coste |
| Sitio | Límite global y su valor | Controla el gasto total; demasiado bajo deja mensajes sin respuesta |
| Sitio | Usuario IA predeterminado del sitio; permiso de cuenta del asistente | Permite habilitar foros y evita desactivaciones por falta de cuenta |
| Sitio | Horario de las tres tareas programadas | Cambia la hora del resumen, de las evaluaciones y de la reactivación |
| Sitio | Plan o cuota en la web del proveedor | Evita pausas por exceso de frecuencia |
| Foro | Habilitar, cuenta, modo, retraso | Decide si responde, cómo y cuándo |
| Foro | Límites por foro y por usuario | Decide a cuántos responde y cuántas veces |
| Foro | Prompts y texto de aviso legal | Tono, extensión y enfoque de las respuestas |
| Foro | Calificación: modo, horas y criterios | Cuándo se evalúa y con qué criterio |
| Foro | Reactivación: días, repetición, fecha límite, prompt | Frecuencia y final de las intervenciones |
| Foro de Moodle | Descripción del foro | Único contexto del curso que recibe la IA (500 caracteres) |
| Foro de Moodle | Calificación del foro completo en puntos, simple directa | Requisito de la calificación por IA |
| Foro de Moodle | Fecha límite de entrega | Detiene la reactivación |
| Curso | Roles de los participantes | Solo se atiende a quien cuenta como estudiante |

## Lo que ningún ajuste cambia en la versión 1.8.2
- La espera del retraso es de una hora, fija.
- Los recortes de texto enviados a la IA.
- Una sola evaluación por estudiante y foro, sin reevaluación.
- Las respuestas inmediatas no atendidas no se recuperan.
- El aviso fijo de IA no se puede quitar ni editar.
- Un solo proveedor para todo el sitio; listas de modelos cerradas.
- La IA no ve el resto del hilo al responder a un mensaje, ni materiales del curso.
- No hay panel de consumo ni de peticiones del día.
Explicarlo con claridad y, si es un requisito del cliente, prepararlo como petición de mejora al mantenedor.

## Entorno de prueba recomendado
1. Un curso de prueba con un foro nuevo y una descripción clara.
2. Dos cuentas de estudiante de prueba matriculadas como estudiantes y sin otros roles; una cuenta docente.
3. Asistente habilitado con la cuenta designada. Límite por usuario conocido.
4. Para no esperar: usar «Ejecutar ahora» en las tareas programadas, o la ejecución de tareas puntuales pendientes que ofrezca el equipo técnico.

## Pruebas controladas
| Prueba | Cambio único | Resultado esperado |
|---|---|---|
| Respuesta básica | El estudiante 1 abre un tema | Respuesta del asistente bajo su mensaje tras la siguiente pasada del cron, con el aviso fijo |
| Respuesta dentro de un tema | El estudiante 2 responde en ese tema | Respuesta bajo su mensaje |
| Límite por usuario | El estudiante 1 escribe un segundo mensaje el mismo día, con límite 1 | Sin respuesta; con límite 2, sí |
| Rol | El docente escribe en el foro | Sin respuesta |
| Retraso | Activar el retraso y publicar | Respuesta aproximadamente una hora después |
| Límite del foro | Poner el límite en 1 y publicar con dos estudiantes | Solo el primero recibe respuesta ese día |
| Resumen diario | Modo Diario, mensajes de estudiantes, ejecutar la tarea del resumen | Un único resumen en el debate del último mensaje; una segunda ejecución el mismo día no publica otro |
| Reactivación | Días de inactividad en 1, esperar un día sin mensajes, ejecutar la tarea | Una intervención en cada debate parado; no repite hasta cumplir los días de repetición |
| Calificación Sugerir | Horas en 1, mensajes de un estudiante, esperar y ejecutar la tarea de calificación | Una sugerencia en la página, con justificación; más mensajes no crean otra |
| Calificación Automática | Igual, en modo Automática, con un estudiante sin nota y otro con nota | Nota aplicada al primero; el segundo no se evalúa |
| Modelo | Cambiar solo el modelo y repetir la respuesta básica | Comparar calidad y tiempo; si con un modelo no llega respuesta y con el económico sí, anotar el modelo |
| Prompt | Cambiar una sola instrucción y publicar el mismo texto con otro estudiante de prueba | Diferencia atribuible a esa instrucción; las respuestas nunca son idénticas |

## Registro de prueba
| Ensayo | Cambio único | Configuración (modo, límites, modelo) | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñado; pendiente de ejecutar; ejecutado en Moodle; no resuelto; resuelto en las condiciones probadas.

## Cuándo escalar al mantenedor
Cuando un comportamiento contradiga esta documentación tras una prueba limpia, o cuando el requisito del cliente choque con algo que ningún ajuste cambia. Incluir: versiones, proveedor y modelo, configuración del foro, pasos, registro de pruebas, síntoma residual y criterio de aceptación. Contacto: julio@rsmax.es.
