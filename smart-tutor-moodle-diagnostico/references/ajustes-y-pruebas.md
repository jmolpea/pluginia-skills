# Ajustes que puede hacer el cliente y pruebas controladas (5.3.2)
Regla: cambiar una sola variable cada vez, anotar el resultado y volver al valor anterior si no mejora. Las pruebas consumen IA: hacerlas en un curso de prueba y con una cuenta de alumno de prueba. Avisar siempre del coste.

## Preparar un banco de pruebas
1. Curso de prueba con el bloque y dos o tres actividades con texto (una página, un PDF con texto, un libro).
2. Una cuenta con rol de estudiante matriculada. No probar solo como administrador: ve contenido que el alumno no ve.
3. Tres preguntas fijas, siempre las mismas: una de contenido, una de datos de Moodle («¿qué tengo pendiente?») y una que el material no cubre.
4. Anotar antes de empezar: proveedor, modelos, interruptores del sitio y del asistente.

## Ajustes por objetivo
| Objetivo | Ajuste más pequeño | Cómo comprobarlo |
|---|---|---|
| Que responda con el material del curso | Activar «Usar el contenido del curso como base de conocimiento» en el asistente | La página de la base de conocimiento muestra las actividades como «Indexado»; «Probar una pregunta» devuelve trozos |
| Que encuentre mejor | «Proveedor de embeddings» en OpenAI o Gemini con su clave | Repetir «Probar una pregunta» con sinónimos de lo que dice el material |
| Dar prioridad a los documentos del docente | Subir las plazas reservadas a los documentos del tutor | Misma pregunta antes y después |
| Que no resuelva ejercicios | Modo de pistas en «Solo pistas» y añadir las tareas a «Actividades protegidas» | Pegar un enunciado como alumno |
| Menos invenciones | Comprobar las respuestas con el material (sitio y asistente) | Pregunta que el material no cubre: debe decir que no lo encuentra |
| Respuestas completas | Subir los tokens máximos de salida del tutor | Pregunta que antes salía cortada |
| Respuestas más rápidas | Esfuerzo de razonamiento «Bajo»; modo «Mapa del curso + búsqueda» | Cronometrar la misma pregunta |
| Solo dudas administrativas | Apagar el tutor, rellenar las FAQs, activar el escalado | Pregunta de contenido: debe atenderla el asistente o declinarla |
| Que cite y enlace | Fuentes bajo cada respuesta (sitio) y «El tutor puede citar el contenido del curso y enlazarlo» | Ver los enlaces bajo la respuesta |
| Controlar el gasto | Presupuesto mensual por asistente; cupos de voz; modelos recomendados | Panel de uso tras unos días |
| Datos en la UE | Proveedor «Compatible» con un servicio europeo o propio; revisar embeddings y voz | Prueba de conexión |
| Avisar de que es una IA | «Mensaje de bienvenida» del bloque | Abrir el chat como alumno |
| Soporte a los profesores del curso | En la dirección de soporte del curso, el comodín de profesores del curso | Enviar una consulta de prueba y mirar el informe de escalados |
| Abrir a visitantes sin sustos | Captcha invisible y tope diario antes de abrir el asistente | Ventana privada sin sesión |

## Pruebas controladas
1. Indexación: activar la base de conocimiento, esperar al cron y comprobar estados. Si queda «Pendiente» mucho tiempo, mirar las tareas programadas antes que cualquier otra cosa.
2. Visibilidad: ocultar una actividad al alumno de prueba y repetir la pregunta; el tutor no debe usarla. Confirma que el filtro por alumno funciona y explica muchos «a mí me responde y al alumno no».
3. Dos interruptores: con la función permitida en el sitio y apagada en el asistente, comprobar que el alumno no la ve; activarla y comprobar que aparece.
4. Enrutador: enviar la pregunta de contenido y la de datos; cada una debe ir a su ayudante. Si no, volver al prompt de enrutador de fábrica.
5. Streaming: con «Mostrar las respuestas palabra a palabra» activo, ver si el texto aparece poco a poco. Si llega de golpe, es un intermediario del servidor.
6. Voz: dictar diez segundos y escuchar una respuesta. Si falla solo en un navegador, es el permiso del micrófono de ese navegador.
7. Llamada: una llamada corta con el motor «Paso a paso»; después, si se quiere, cambiar solo el motor a tiempo real.
8. Soporte: pedir hablar con una persona, confirmar la tarjeta y seguir la consulta en el informe hasta «enviada». Repetir la misma consulta para ver que no se duplica.
9. Límites: bajar temporalmente «Mensajes por usuario y minuto» a 2, enviar tres mensajes seguidos, comprobar el aviso y restaurar el valor.
10. Examen del tutor: si está permitido, lanzarlo en el curso piloto y revisar los fallos con su fuente. Uno al día por asistente; tiene coste.

## Qué no se arregla con ajustes
- Que lea cuestionarios, o que funcione en el Área personal.
- Voz, llamadas o base de conocimiento del aula en asistentes de portada o categoría.
- Imágenes con DeepSeek.
- Texto de un PDF escaneado sin capa de texto.
- Fijar un idioma de respuesta distinto de inglés o español (sí se puede pedir en el prompt del tutor, como propuesta sin garantía).
En estos casos, explicar la limitación y, si el cliente quiere, preparar una petición de mejora para el mantenedor.

## Plantilla de solicitud al mantenedor
Versión de Moodle y del plugin · proveedor y modelos · dónde está el bloque · configuración del asistente relevante · pasos exactos para reproducirlo · qué se esperaba y qué ocurrió (texto del aviso) · ajustes probados y su resultado · evidencias anonimizadas · criterio de aceptación.
