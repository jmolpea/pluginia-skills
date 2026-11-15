# Ajustes y pruebas antes de escalar (AI Viva 1.3.0)

Revisado el 15-11-2026.

## Regla de intervención
Buscar primero la solución en lo que el cliente controla. Cambiar una sola cosa cada vez y comprobar su efecto con un alumno de prueba.
Conservar criterios académicos, escala, pesos y reglas de publicación salvo autorización expresa. No desactivar la retención de notas ni la moderación para «hacer desaparecer» un síntoma.
Avisar siempre del coste: cada intento de prueba y cada regeneración consumen IA.

## Qué puede ajustar el cliente
| Ámbito | Ajuste | Para qué síntoma |
|---|---|---|
| Sitio | Clave API principal, saldo y límite de gasto en OpenAI | Error genérico del servicio de IA; evaluaciones que no terminan |
| Sitio | Clave de licencia | Aviso de licencia |
| Sitio | Máximo de tokens por llamada a la API | Error de respuesta cortada |
| Sitio | Tiempo de espera de la API (segundos) | Análisis de documentos largos que fallan |
| Sitio | Máximo de llamadas a la API por usuario por minuto | Aviso de demasiadas solicitudes en el tribunal |
| Sitio | Activar moderación de contenido de OpenAI | Bloqueos por contenido en materias sensibles (decisión institucional) |
| Sitio | Tamaño máximo global de video (MB) y límites de subida del servidor | Grabaciones que no se suben |
| Sitio | Modelos disponibles para el profesorado | Control del gasto |
| Sitio | Texto del aviso RGPD | Requisitos de protección de datos |
| Servidor | Cron cada minuto, HTTPS, salida a internet | Esperas largas, cierre de tribunales, permisos de grabación |
| Actividad | Prompts de los pasos 1 y 2 y de evaluación final | Evaluaciones genéricas o desalineadas con los criterios |
| Actividad | Personalidad de cada examinador y modelo del tribunal | Preguntas poco exigentes, repetitivas o fuera de tono |
| Actividad | Restricciones de contenido adicionales | Aspectos que no deben valorarse o tono inadecuado |
| Actividad | Pesos y calificación máxima | Nota final que no refleja lo que importa |
| Actividad | Duraciones y tamaños | Vídeos demasiado pesados; tribunales demasiado cortos o largos |
| Actividad | Retener las calificaciones | Notas que se ven antes de revisarlas, o que no se ven |
| Actividad | Conservar las grabaciones (días) | Grabaciones borradas antes de lo esperado, o disco lleno |
| Actividad | Excepciones de usuario o grupo | Un alumno necesita otro plazo u otro intento |
| Entregas | Regenerar, editar, publicar, retirar, eliminar | Corregir un intento concreto |
| Alumno | Navegador, permisos, micrófono, idioma del perfil | Fallos de grabación, de voz o de idioma |

## Lo que no se arregla con ajustes (decirlo con claridad)
- Pausar o alargar el tribunal de un alumno concreto, o terminarlo antes de tiempo.
- Usar otro proveedor de IA o un servidor propio.
- Que la IA vea el vídeo completo o la cara del alumno.
- Recuperar grabaciones ya borradas.
- Reescalar notas guardadas tras cambiar la calificación máxima.
- Ver el gasto real dentro de Moodle.
En estos casos, explicar la limitación, ofrecer la alternativa más cercana y, si el cliente lo pide, preparar la solicitud para el mantenedor.

## Preparar un entorno de prueba
1. Duplicar la actividad en un curso de pruebas o crear una nueva con los mismos ajustes.
2. Usar un usuario con rol de alumno (los docentes no pueden hacer la defensa con su cuenta).
3. Poner presentación de 5 minutos y tribunal de 5 minutos para abaratar la prueba.
4. Usar un PDF de prueba sin datos personales, siempre el mismo.
5. Activar la retención de notas para que nada se publique solo.

## Pruebas controladas (una variable cada vez)
| Prueba | Qué se cambia | Qué se observa |
|---|---|---|
| Conexión con la IA | Nada: subir un PDF pequeño | Si el intento pasa al paso de presentación con análisis visible en el detalle |
| Límites de subida | Grabar 1 minuto y después 10 | Si ambas grabaciones se suben; tamaño indicado en la revisión |
| Prompt del documento | Solo el prompt del paso 1, después «Re-analizar PDF» | Cambios en el análisis y en la puntuación del documento |
| Prompt de evaluación | Solo el prompt final, después «Recalcular evaluación final» | Cambios en puntuaciones y comentarios con las mismas evidencias |
| Modelo | Solo el modelo de un paso | Calidad y tiempo; anotar el coste en OpenAI |
| Pesos | Solo los pesos, después «Recalcular evaluación final» | Nota propuesta con las mismas puntuaciones parciales (varían algo porque la IA vuelve a puntuar) |
| Retención | Activar o desactivar en la copia y hacer un intento | Qué ve el alumno al terminar y si llega al libro de calificaciones |
| Límite de llamadas | Solo ese ajuste | Si aparece el aviso al responder deprisa |
| Variabilidad | Nada: «Recalcular evaluación final» tres veces, respetando la espera | Dispersión de las puntuaciones por paso |
Recordatorio: regenerar no pisa una nota editada por un docente; para ver el efecto en la nota final, usar un intento sin editar.

## Registro de prueba
| Ensayo | Cambio único | Intento y configuración | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñado; ejecutado en Moodle; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
No marcar como ejecutado lo que solo se ha razonado en el chat.

## Cuándo escalar
Tras al menos un ajuste pertinente probado sin resultado, o cuando el síntoma corresponde a una limitación de la lista anterior y el cliente necesita ese comportamiento. Usar la ficha de escalado del protocolo.
