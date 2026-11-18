# Funcionamiento de Smart Tutor & Support AI 5.3.4
Documentación funcional derivada del código de la versión 5.3.4 (Moodle 4.5 a 5.3), revisada el 18-11-2026. Todo lo que sigue está verificado en el código salvo donde se indica «probable».

## 1. Qué es
Un bloque de Moodle que pone un chat de IA en un curso, en la página de una actividad, en una categoría de cursos o en la portada del sitio. Cada bloque es un asistente independiente, con su configuración, sus documentos y su historial. Un mismo curso puede tener varios; en ese caso el menú del curso muestra un enlace de configuración por cada uno, con su nombre.
No funciona en el Área personal: allí Moodle crea una copia del bloque por usuario y esa copia no tiene configuración; solo quien puede editarla ve un aviso.

## 2. Los tres papeles
- Enrutador: lee cada mensaje y decide quién responde. Si en el asistente solo está encendido uno de los dos ayudantes, el enrutador se salta.
- Tutor: explica el contenido con el material (documentos subidos y, si está activada, la base de conocimiento del aula). Nunca resuelve tareas ni cuestionarios evaluables; ofrece explicar el concepto. Ese bloqueo no se puede apagar, solo ajustar su texto.
- Asistente: responde con datos de Moodle del propio alumno (progreso, notas, fechas, entregas, cuestionarios, foros, actividades) mediante consultas de solo lectura, y gestiona el escalado a soporte. Nunca cambia nada en Moodle ni ve datos de otros alumnos.
En portada o categoría, el asistente trabaja con las matrículas, el progreso, las notas, los avisos, los certificados y las insignias del usuario en todos sus cursos, más el catálogo y cómo matricularse.

### Cómo se reparte cada pregunta (cambios de 5.3.3)
- Palabras como «fecha de entrega», «deadline», «me falta», «está bloqueado», «ticket», «prórroga» o «da error» ya no mandan el mensaje al asistente por sí solas. Lo hacen cuando el mensaje señala al aula o a lo propio del alumno (mi, la tarea, el cuestionario, la semana, una actividad por su número) y no pregunta qué dice el material. En los demás casos decide el enrutador.
- «Cómo mejorar X» o «qué falló en X» solo activan la revisión del trabajo del alumno cuando X es su trabajo (mi entrega, la 2.3) o cuando no sigue nada («¿cómo puedo mejorar?»).
- Cuando una semana o una actividad depende de una sola condición, el asistente recibe el nombre de la actividad que hay que completar o aprobar. Antes de 5.3.3 recibía un número interno y no sabía explicar el bloqueo.
- Las preguntas cortas en portugués se reconocen como portugués; antes de 5.3.3 podían responderse en español.
- Una respuesta corta y correcta del tutor que contenía «desde aquí» ya no se descarta como si fuera una remisión al chat.

## 3. Cadena para que el chat aparezca y responda
1. Licencia válida o periodo de prueba en curso (se comprueba sin conexión y está ligada a la dirección del sitio).
2. «Habilitar el plugin» encendido y clave del proveedor elegido guardada.
3. En Moodle 5.1 o posterior, «Permitir herramientas de IA» activo en el curso.
4. El usuario tiene el permiso de usar el chat (de fábrica, cualquier usuario con sesión; los invitados no).
5. «Habilitar el asistente en este curso» encendido en la configuración de ese asistente.
6. Límite de mensajes por minuto y por día sin agotar.
Si falla un eslabón, el bloque muestra un aviso en lugar del chat, o el chat devuelve un mensaje de error (ver protocolo de diagnóstico). Quien gestiona el curso ve el motivo concreto de la licencia; el alumno, un aviso genérico.

### Cuando falla el proveedor de IA (cambios de 5.3.3)
- Si el proveedor rechaza la petición por su propio límite de uso, el alumno lee «Estás enviando mensajes demasiado rápido o el asistente no está disponible temporalmente. Espera un momento e inténtalo de nuevo.». No es el límite de mensajes de Moodle, cuyo aviso es más corto y no menciona la disponibilidad.
- Si la conexión con el proveedor se corta o el proveedor responde con un error interno antes de que se haya mostrado nada, la llamada se repite una vez. No se repite tras un tiempo de espera agotado ni tras un rechazo.
- Cualquier otro fallo (clave rechazada, sin saldo, modelo retirado) da «El asistente no está disponible temporalmente».

## 4. Regla de los dos interruptores
Las funciones añadidas (base de conocimiento del aula, voz, llamadas, botón flotante, fórmulas, imágenes, pistas, practicar, revisar borrador, lectura fácil, comprobación de respuestas, descripción de imágenes, análisis semanal de temas, presupuesto) necesitan el permiso del administrador en el sitio y la activación del docente en su asistente. Si el administrador no la permite, la opción ni aparece en el formulario del docente; lo que el docente tenía elegido se conserva. Las fuentes bajo cada respuesta, las valoraciones y el informe del curso solo tienen interruptor del sitio.

### Botón flotante
Con «Mostrar el asistente en todas las páginas del curso» activado en el asistente (y permitido en el sitio), un botón flotante abre el mismo chat y la misma conversación desde cualquier página del curso. Desde 5.3.3 aparece también en la página del curso y en sus secciones, donde la tarjeta del bloque puede quedar oculta en el cajón de bloques o fuera de la vista en el móvil. Nunca aparece dentro de un intento o una revisión de cuestionario. Solo para asistentes de curso.

## 5. Material del tutor
- Documentos subidos en la configuración del asistente: citables (los nombra y cita) e internos (los usa para entender, nunca los nombra ni los copia).
- Base de conocimiento del aula: lee páginas, libros, etiquetas, archivos, carpetas, URL, enunciados de tareas, foros, glosarios, lecciones, wikis, paquetes IMS, SCORM y H5P. Los cuestionarios no se leen nunca. Lee paquetes de Articulate Rise, Genially y páginas web hechas a mano; las preguntas, opciones y soluciones de esos paquetes quedan fuera.
- Cada alumno solo recibe trozos de lo que él puede abrir en ese momento: lo oculto no se usa nunca y lo restringido, solo cuando ese alumno cumple la restricción.
- Se actualiza sola unos minutos después de un cambio en el curso y con una revisión nocturna. El docente puede excluir actividades, ver el texto extraído, probar una pregunta y pedir una reindexación.
- Con búsqueda por significado (embeddings de OpenAI o Gemini) encuentra mejor; sin ella busca por palabras.
- Opcional: una huella numérica de las preguntas de los cuestionarios permite reconocer cuándo un alumno pega una de ellas y no resolverla. No se guardan las preguntas.
- Opcional: una IA describe una sola vez las imágenes del material para que el tutor responda sobre diagramas. Sin licencia válida no se describen imágenes nuevas (desde 5.3.2).

### Cómo se busca en el material (cambios de 5.3.4)
- Seguimientos sin tema: un mensaje que pide citar, ampliar o «qué dice exactamente» algo sin nombrarlo («¿y qué dice exactamente ahí?», «cítame el material», «amplía con lo que dice el documento») se busca junto con la pregunta anterior del alumno. Antes de 5.3.4 se buscaba solo, recuperaba fragmentos que no venían al caso y el tutor podía decir que no podía confirmar una cita correcta que acababa de dar.
- Mensajes con dos pedidos: cuando el mensaje anuncia dos o tres pedidos («dos cosas», «y además», «por otro lado»), cada uno se busca por separado, también en la base de conocimiento del aula, y sus mejores fragmentos van primero. No supone más consultas a la IA ni cambia el número de fragmentos.
- No hay ningún ajuste nuevo en pantalla para estas dos mejoras.

## 6. Feedback personalizado
Si el sitio lo permite y el docente lo activa, el tutor puede leer el trabajo del propio alumno ya publicado (entrega, nota, comentarios, rúbrica, participación en foros y, en el nivel máximo, la revisión de cuestionarios que Moodle ya le muestra). El máximo que fija el administrador manda sobre lo que elija el curso. Cada alumno puede impedirlo con el interruptor «Permitir que el tutor revise mis actividades para ayudarme» del chat.

## 7. Voz y llamadas (solo asistentes de curso)
- Voz: micrófono para dictar y altavoz para escuchar. El alumno acepta un aviso antes del primer uso. Solo se lee en voz alta lo que el asistente acaba de decir en la conversación de ese alumno. Si el proveedor de voz elegido no tiene clave, se usa la voz del navegador.
- Llamada: conversación hablada en una ventana propia. Motor «Paso a paso» (cualquier proveedor de chat; necesita un proveedor de voz del servidor, no vale «Navegador») o «Tiempo real» de OpenAI o Gemini, que no depende del proveedor de voz. Las respuestas con contenido salen de las mismas reglas y material que el chat.
- El servidor cuenta los minutos entre latidos del navegador y cuelga al llegar a los límites. El audio nunca se guarda y la cámara del alumno no sale de su navegador.
- Desde 5.3.2 la voz y las llamadas se detienen también cuando se deshabilita el plugin, se deshabilita el asistente del curso o se desactivan las herramientas de IA del curso; antes seguían respondiendo a una página ya abierta.

## 8. Escalado a soporte
El asistente puede proponer enviar la consulta a soporte. Prepara un borrador y el alumno lo confirma con un clic en una tarjeta del chat; nada se envía sin esa confirmación. El borrador caduca a las 24 horas. El correo lleva nombre, dirección, curso, resumen y, si se configura, los últimos mensajes. El alumno recibe una notificación de Moodle con la referencia. Si el envío por correo está apagado o se superan los límites, el asistente da el enlace de soporte. El destino lo cambia solo quien tiene permiso de gestor; al restaurar un curso en otro sitio, las direcciones de destino no se copian.
Desde 5.3.3, en un asistente de categoría o de portada el correo nombra el curso al que se refiere la consulta en lugar del nombre del sitio: el de la página en la que se muestra el asistente o, fuera de un curso, el que nombra la conversación, aceptado solo si es un curso del propio participante dentro de la categoría del asistente. El resumen nombra además el curso o la actividad cuando la conversación lo deja claro. Los destinatarios, los cupos y la referencia no cambian.

## 9. Visitantes sin sesión
Solo en asistentes de portada o categoría que un gestor abra expresamente. Responden sobre cursos, matrícula y acceso; nunca sobre personas. Tienen límites propios por dirección y un tope diario del sitio; al alcanzarlo se dan los enlaces de acceso, registro y soporte sin gastar IA, y se avisa a los administradores una vez al día.

## 10. Qué se envía al proveedor y qué se guarda
- Se envía: el mensaje del alumno, su nombre de pila, las instrucciones del asistente, los trozos de material pertinentes y los datos de Moodle de ese alumno que haga falta consultar. Nunca datos de otros alumnos ni claves.
- Las imágenes adjuntas pierden sus datos ocultos, no se guardan y viajan solo con ese mensaje.
- Se guarda en Moodle: las conversaciones (si el sitio y el asistente lo tienen activado), estadísticas de uso por día, consultas a soporte, valoraciones, minutos de voz y duración de las llamadas. Con el registro apagado solo quedan cifras sin texto.
- La retención borra cada noche lo que supera los días configurados. El plugin declara sus datos en la API de privacidad de Moodle (exportación y borrado por usuario); desde 5.3.3 la exportación incluye el curso al que se refiere cada consulta de soporte.

## 11. Informes
Panel de uso (administrador): preguntas, personas, tokens y coste estimado por curso y modelo, voz, llamadas y calidad. Informe de escalados a soporte. Respuestas con pulgar abajo, sin decir quién valoró. Herramientas de prueba: conexión con el proveedor, correo de soporte, búsqueda en el material y qué ve un alumno concreto. Los cuatro piden el permiso de configuración global (de fábrica, administrador y gestor). Informe del curso «Asistente de IA: uso y temas» (docentes), con análisis semanal de temas si se activa.

## 12. Tareas programadas (necesitan el cron de Moodle)
| Tarea (nombre en pantalla) | Cuándo |
|---|---|
| Indexar archivos PDF/texto para el chatbot | cada 5 minutos |
| Generar embeddings de los documentos de la base de conocimiento | cada 10 minutos |
| Enviar escalados de soporte agrupados | cada 5 minutos |
| Construir analítica de uso del chatbot | 02:15 |
| Conciliar las bases de conocimiento del aula con sus cursos | 02:45 |
| Purgar conversaciones antiguas del chatbot | 03:30 |
| Analizar los temas recurrentes de cada curso | lunes 04:30 |
Además hay tareas puntuales para indexar un asistente, enviar cada correo de soporte y hacer el examen del tutor. Sin cron no se indexa material, no salen correos y no se actualiza el panel.

## 13. Copia de seguridad y restauración
La copia del curso incluye la configuración de cada asistente, sus herramientas y los documentos subidos. No incluye conversaciones. Los índices se reconstruyen al restaurar.

## 14. Limitaciones conocidas en 5.3.4
- No funciona en el Área personal.
- Los asistentes de portada y categoría no tienen voz, llamadas, base de conocimiento del aula, botón flotante, pistas, practicar, borrador, fórmulas, imágenes, comprobación de respuestas, feedback personalizado ni análisis semanal de temas. Sí tienen presupuesto, lectura fácil, documentos subidos, FAQs y escalado a soporte.
- Los cuestionarios nunca entran en la base de conocimiento.
- Con DeepSeek no hay imágenes en el chat ni descripción de imágenes; Anthropic y DeepSeek necesitan OpenAI o Gemini para la búsqueda por significado.
- Los PDF escaneados (solo imagen) no aportan texto.
- En la app de Moodle solo hay chat escrito; voz, imágenes y botones están en la web.
- La política de idioma solo permite fijar inglés o español; «Automático» sigue al alumno.

## 15. Qué cambió desde la 5.3.2
- 5.3.3: botón flotante también en la página del curso y sus secciones; reparto de preguntas más fino entre tutor, asistente y revisión del trabajo; aviso propio cuando el proveedor rechaza por su límite; un reintento ante cortes o errores internos del proveedor; el correo de soporte de un asistente de categoría o portada nombra el curso; el asistente explica los bloqueos con una sola condición; portugués reconocido en preguntas cortas; dos correcciones con Anthropic como proveedor.
- 5.3.4: los seguimientos sin tema se buscan con la pregunta anterior y los mensajes con dos pedidos se buscan por separado.
- Ningún ajuste, permiso, límite ni valor de fábrica cambió entre la 5.3.2 y la 5.3.4.
