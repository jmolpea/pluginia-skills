# Protocolo de casos

Revisado para la versión 1.7.2 el 15-11-2026. En versiones anteriores, los casos de la fila «no se ha podido calificar» no dejaban ninguna nota.

## Ficha mínima
Pedir según la consulta:
- Versión de Moodle y del plugin; proveedor y modelo efectivo, incluido modelo personalizado si existe.
- Descripción literal de la actividad y prompt docente.
- Rúbrica completa de Moodle: criterios, todos sus niveles y puntos; distinguir rúbrica de guía.
- Entrega original anonimizada, con extensiones y tamaños.
- Feedback real, nota y captura/exportación de los niveles seleccionados en Moodle.
- Configuración de AI Tutor en la tarea: método, publicación directa, reentregas, umbral de confianza, retraso, topes y usuario que firma.
- Configuración de la tarea de Moodle: flujo de trabajo de calificación, comentarios de retroalimentación, botón de envío, intentos adicionales, entrega en grupo.
- Quién hizo la entrega (rol), fecha y hora, y si era el primer intento o una reentrega.
Para variabilidad, añadir las dos evaluaciones completas, fechas, número de intento y cambios de configuración entre ejecuciones.
No exigir todo para contestar una pregunta simple. No pedir claves ni acceso administrativo.

## Árbol de síntomas
| Síntoma | Causas posibles, de más a menos frecuente | Comprobación |
|---|---|---|
| La entrega no tiene nota, comentario ni aviso | Entregó una cuenta que puede calificar; AI Tutor no estaba activado al entregar; retraso de una hora; cron parado; licencia caducada o clave de API vacía; tope alcanzado; comentarios de retroalimentación desactivados en la tarea; versión anterior a 1.7.2 | Rol de quien entregó; página de AI Tutor; tareas ad hoc pendientes; estado de la licencia; número de correcciones del día; versión instalada; salida del cron |
| Nota de «no se ha podido calificar automáticamente» | Fallo o tiempo de espera del proveedor; clave rechazada o sin saldo; modelo inexistente; dirección personalizada errónea; respuesta sin nota utilizable en tarea de puntos o escala; usuario que firma sin permiso para calificar | Notificaciones a administradores; proveedor, modelo y modelo personalizado; matrícula y rol del usuario que firma; tamaño de la entrega; salida del cron |
| Aviso de «no se ha podido leer» | Formato no admitido; archivo protegido, vacío o dañado; tamaño superior al tope; audio sin transcripción activa | Extensión y tamaño de cada archivo frente a la tabla de límites |
| Nota sin comentario | Comentarios de retroalimentación desactivados en la tarea | Tipos de retroalimentación de la tarea |
| El alumno ve una nota que debía revisarse | La tarea no usa el flujo de trabajo de calificación | Ajuste de calificación de la tarea |
| La nota no se publica aunque se pidió publicar | Confianza bajo el umbral; correspondencia incompleta o nota recortada; es una reentrega sin la opción de reentregas | Avisos entre corchetes en el comentario; número de intento |
| Aviso de correspondencia incompleta | Nombres de criterio o nivel no reconocidos, duplicados o contenidos unos en otros; prompt que pide valores que la rúbrica no tiene; respuesta cortada | Rúbrica guardada criterio a criterio; textos exactos de la rúbrica; prompt |
| Aviso de confianza baja | Entrega breve, ambigua o parcialmente ilegible; evidencia que la IA no ve; umbral alto | Qué parte de la evidencia llegó realmente a la IA |
| Unas entregas sí y otras no | Límite diario de la tarea; máximo por alumno; topes por hora; archivos de formatos distintos | Recuento de correcciones guardadas ese día y por alumno |
| La corrección ignora parte del trabajo | Recorte a 200.000 caracteres o a 5 imágenes; archivo omitido; imágenes de Word, Excel o PowerPoint; descripción más allá de 8.000 caracteres | Orden y tamaño de los archivos; dónde está la evidencia |
| AI Tutor desactivado sin tocarlo | Usuario que firma eliminado o suspendido y sin reserva válida; tarea copiada o restaurada sin usuarios (llega siempre desactivada); restauración anterior a 1.7.1 | Usuario elegido en la tarea; origen de la tarea |
| Doble corrección o doble cobro | Plugin antiguo «AI Tutor» aún instalado y activo | Aviso de migración en los ajustes del sitio |
| Aviso de autenticación a los administradores | Clave errónea, caducada, sin saldo o de otro proveedor | Proveedor elegido frente a la clave; cuenta del proveedor |

Cada fila es una lista de hipótesis: ninguna queda confirmada sin su comprobación.

## Rúbrica incompleta
1. Precisar si falta un criterio en la rúbrica guardada, en el feedback narrativo o en ambos.
2. Verificar el modo activo en Moodle y la opción del tutor.
3. Inventariar todos los criterios y niveles sin abreviarlos para la comparación.
4. Construir esta tabla:
| Criterio | Evidencia y ubicación en entrega | ¿Puede leerla el plugin? | Resultado real | Explicación y certeza |
5. Distinguir “no hay evidencia en la entrega” de “hay evidencia visual que el extractor no transmite”.
6. Revisar recortes, etiquetas duplicadas, textos parcialmente coincidentes y exigencias contradictorias del prompt.
7. Si existe respuesta íntegra, comprobar presencia de cada criterio y correspondencia de cada nivel. Si no existe, no atribuir con certeza el fallo a la generación o al procesamiento.
8. Revisar estado de publicación y errores de guardado.
9. Proponer una prueba en una copia de la actividad, con alumno de prueba. Cambiar una sola variable y verificar todos los criterios, nota y publicación.

## Notas diferentes
Separar identidad del archivo de identidad de la solicitud efectiva. Comprobar configuración, versión, proveedor/modelo, contenido extraído, prompt, rúbrica y escala.
Considerar cambios entre envío y ejecución porque el proceso es asíncrono.
Comparar los niveles asignados criterio por criterio y su evidencia; no limitarse a la diferencia total de nota.
No prometer reproducibilidad exacta por usar temperatura baja. No suponer que la “confianza” mide la calidad real.
Recomendar repetición controlada solo como prueba autorizada, en entorno de prueba y teniendo en cuenta el consumo de API.

## Sin evaluación o sin publicación
Separar tarea no ejecutada, error de proveedor, falta de contenido, guardado fallido y resultado pendiente de revisión.
Verificar habilitación, licencia, configuración del proveedor, usuario tutor, permisos del participante de prueba, límites, cola y cron.
Comprobar que la tarea usa el flujo de trabajo de calificación y tiene activados los comentarios de retroalimentación.
Recordar que una entrega no corregida por un límite o un fallo no se reintenta: hay que corregirla a mano o volver a entregar.
Comprobar retraso de una hora y condiciones de revisión. No sugerir bajar el umbral como forma de ocultar un problema de rúbrica.

## Orden de intervención
Aplicar references/ajustes-y-pruebas.md en todos los casos.
Primero contrastar descripción, rúbrica y prompt. Proponer la alternativa pertinente sin cambiar la escala académica para hacer desaparecer el error.
Después realizar o solicitar ensayos controlados con alumno de prueba y evidencias anonimizadas. No confundir una simulación del mapeo con una evaluación real de la API y Moodle.
Registrar cada ensayo: cambio único, entrada, versión, modelo, salida, niveles guardados, nota, publicación y conclusión.
Si falta acceso, marcar ejecución pendiente. No concluir que los ajustes fallaron.
Solo después de que ajustes probados resulten insuficientes, plantear un cambio de código al administrador del plugin.

## Escalamiento
Entregar una ficha breve con:
versión, síntoma, comportamiento esperado, configuración relevante, reproducción anonimizada, resultados observados, hipótesis descartadas y evidencia faltante.
Para solicitar un cambio de código, añadir los ajustes de descripción/rúbrica/prompt ya probados, el resultado de cada uno, el fallo residual, el comportamiento funcional solicitado y los criterios de aceptación. No incluir código fuente del plugin ni afirmar que el administrador ha recibido la solicitud.
Solicitar al mantenedor, cuando resulte necesario, la solicitud efectiva anonimizada, respuesta original, parámetros y motivo de finalización; indicar que la versión revisada no ofrece un exportador confirmado.
No afirmar que un informe está enviado ni crear incidencias externas sin petición expresa.

## Grado de certeza
Confirmado: evidencia directa del caso y regla aplicable.
Probable: mecanismo compatible con el síntoma, pendiente de una comprobación identificada.
No comprobable: falta evidencia decisiva; explicar qué dato permitiría avanzar.
Un límite documentado es un hecho; que haya sido la causa de un caso es una conclusión independiente.
