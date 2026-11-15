# Funcionamiento verificado: 1.0.0-beta4

Revisión estática del código que declara 1.0.0-beta4 (interna 2026100600), hecha el 15-11-2026. Admite Moodle 4.5 a 5.3. Todo lo que sigue es comportamiento leído en el código, no probado en un sitio concreto, salvo que se indique.

## Qué es
Un bloque de Moodle que recomienda a cada persona cursos y rutas de aprendizaje del catálogo del sitio. Solo se puede colocar en la portada del sitio y en el Área personal; nunca dentro de un curso. Solo una instancia por página. No tiene ajustes por instancia: toda la configuración es de sitio.
No guarda claves ni llama a servicios externos por su cuenta: usa el sistema de IA de Moodle (proveedores configurados en Administración del sitio › General › IA). Necesita la acción «Generar texto»; «Generar imagen» es opcional.

## Quién ve qué
| Situación | Resultado |
|---|---|
| Invitado o sin sesión | El bloque queda vacío. |
| Sin el permiso «Recibir recomendaciones de cursos con IA» (a nivel de sitio) | Vacío. |
| No hay proveedor con «Generar texto» | Vacío para usuarios; el administrador ve un aviso con enlace a los proveedores. |
| Falta aceptar condiciones o política de IA, o no hay respuestas | Cuestionario (una pregunta por pantalla) y, si falta, casilla de aceptación. |
| Todo correcto | Se cargan las recomendaciones después de pintar la página. |

## Flujo de una recomendación
1. Aceptación. Con «Pedir consentimiento» activado, la persona acepta el aviso de privacidad del plugin. Aparte, Moodle exige su propia política de uso de la IA; se comprueba en el servidor, no solo en pantalla.
2. Respuestas. Hasta seis preguntas activas; debe responder al menos una. Se guardan las respuestas actuales y un historial de versiones.
3. Candidatos. Moodle calcula qué cursos puede recibir esa persona (tabla siguiente). La IA no decide esto.
4. Preselección. Si hay más candidatos que «Máximo de cursos por petición», se eligen sin IA los que comparten más palabras (de 3 letras o más) entre respuestas y perfil, por un lado, y nombre, categoría, etiquetas y resumen del curso, por otro. En empate, los cursos más recientes.
5. Petición. Se envían instrucciones fijas, el prompt institucional, datos del perfil, respuestas, valoraciones negativas recientes, candidatos y rutas. La IA devuelve cursos y rutas con puntuación de 0 a 100 y un motivo. Se le pide incluir solo los que puntúe con 40 o más.
6. Validación. Se descarta todo lo que no esté en la lista enviada, los duplicados y lo que exceda los máximos. Los motivos se limpian (texto plano, sin enlaces ni correos, recortados). Si la respuesta no tiene el formato esperado se reintenta una vez; si vuelve a fallar, la persona ve un error y puede reintentar.
7. Guardado. Se guarda un ranking por persona, con fecha de caducidad.
8. Presentación. Al mostrar se vuelve a filtrar: fuera lo que ya no es candidato y lo valorado con pulgar abajo dentro del plazo. «Ver más» recorre el ranking guardado sin nuevas peticiones.

## Condiciones para que un curso sea candidato (todas a la vez)
| Condición | Detalle |
|---|---|
| Visible | Los cursos ocultos nunca entran. |
| No terminado | Sin fecha de fin o con fecha futura. |
| No matriculada | La persona no tiene ninguna matrícula en el curso, tampoco suspendida. |
| Método abierto | Tiene activa una instancia de un método marcado en «Métodos de matriculación», con el plugin de matrícula habilitado en el sitio y dentro de sus fechas de matrícula. |
| Automatriculación utilizable | Si el método es automatriculación: admite nuevas matrículas, quedan plazas, la persona pertenece a la cohorte si se exige, y su rol puede automatricularse. |
| Categoría | Con «Filtrar por categoría», el curso está en una categoría elegida o en sus subcategorías. Filtro activo sin categorías = ningún candidato. |
| No excluido | No tiene marcada la casilla del «Campo de exclusión». |
| Visible para la persona | Puede ver la información del curso en el catálogo (categorías ocultas, permisos). |
Los cursos con clave o con otros métodos (por ejemplo pago) son candidatos, pero solo ofrecen «Ver curso». «Matricularme» exige automatriculación sin clave y que Moodle permita matricular a esa persona en ese momento.

## Cuándo se reutiliza el ranking guardado
Se reutiliza si no ha caducado, si no han cambiado respuestas, texto de preguntas, datos del perfil enviados, idioma de navegación ni prompt institucional, y si todos los candidatos actuales ya estaban en el ranking con los mismos datos. Que desaparezca un curso no obliga a repetir. Un candidato nuevo o un curso con datos cambiados sí. Guardar respuestas caduca el ranking, pero no lo borra: sirve de respaldo cuando se alcanza el límite diario. Solo hay una petición de ranking a la vez por persona; una segunda simultánea recibe «Estamos preparando tus recomendaciones…».

## Qué se envía a la IA y qué no
Se envía: campos de perfil marcados (ciudad, país, institución, departamento, intereses, descripción y personalizados elegidos), idioma, preguntas y respuestas, nombre y motivo de los últimos elementos con pulgar abajo, y por cada curso candidato su identificador interno, nombre, categoría, fechas, etiquetas, campos personalizados públicos, información de matrícula y un resumen (o la descripción recortada si aún no hay resumen). De las rutas: título, descripción recortada y sus cursos visibles.
No se envían nombre, correo, usuario, número de ID, teléfono, dirección ni IP. En el texto libre se sustituyen correos, enlaces, números de 9 o más cifras y el nombre, apellidos, usuario y número de ID de la propia persona. Es una sustitución por patrones: no detecta nombres de terceros.
Los cursos ocultos y el campo de exclusión nunca se envían. Los campos de curso no públicos solo con «Enviar campos de curso no públicos».

## Resúmenes de curso
La IA escribe una vez por curso un resumen breve en inglés. Se rehace solo si cambian los datos del curso. Se generan en la tarea horaria y al crear, editar o restaurar un curso o cambiar sus etiquetas (en segundo plano; guardar un curso no espera a la IA). Se piden en nombre del administrador principal, por lo que el tope de peticiones por usuario del proveedor de Moodle los frena; al llegar al tope la tarea se detiene y continúa en la siguiente ejecución.

## Valoraciones, clics y matrículas
«Útil» / «No me sirve», con motivo opcional en el pulgar abajo. Un pulgar abajo oculta el elemento durante «Días ocultos tras un pulgar abajo» desde la última valoración y se comunica a la IA. Solo se aceptan valoraciones, clics y matrículas de elementos que estén en el ranking guardado de esa persona. Las valoraciones no caducan el ranking.

## Rutas de aprendizaje
Las crea quien tenga «Gestionar las rutas de aprendizaje del recomendador»: título, cursos visibles, orden, descripción, imagen y visibilidad. Una ruta se recomienda si está visible, «Recomendar rutas de aprendizaje» está activado y al menos uno de sus cursos visibles es candidato para la persona. La página de la ruta la puede abrir cualquier usuario con permiso de uso; muestra por curso: Completado, En curso, Disponible o No disponible ahora (con motivo). «Matricularme en toda la ruta» matricula solo en los cursos con automatriculación sin clave y muestra el resultado curso por curso.
Botones de IA del formulario: «Generar descripción con IA» (texto en todos los idiomas instalados, con vista previa) y «Generar imagen con IA» (solo con proveedor de imagen; sustituye la imagen al guardar). Requieren cursos seleccionados y que el gestor acepte la política de IA.

## Tareas
| Tarea | Frecuencia de fábrica | Efecto |
|---|---|---|
| Generar resúmenes de curso con IA | Cada hora | Hasta «Resúmenes de curso por ejecución». |
| Ordenar cursos nuevos y avisar a los usuarios | Diaria, sobre las 3:00 | Personas con ranking y respuestas, activas, no revisadas en las últimas 12 horas, con permiso, consentimiento y política aceptados; las menos recientes primero. Pide puntuar solo los cursos nuevos, los añade al ranking y avisa de los que alcanzan el umbral. |
| Borrar datos antiguos | Diaria, sobre las 4:00 | Aplica «Conservación de datos (días)». |
Un curso es «nuevo» para una persona si no estaba en su ranking y se creó o modificó, o su matrícula se abrió o cambió, después de la última revisión. Apagar «Avisar de cursos nuevos» quita el aviso, pero la tarea sigue puntuando cursos nuevos (con coste).

## Qué se guarda
Respuestas actuales y consentimiento; historial de respuestas; último ranking; valoraciones; actividad (mostrado, clic, matrícula); registro de peticiones a la IA (tipo, éxito, error, duración, tokens; no el texto enviado ni la respuesta). «Borrar mis datos» elimina respuestas, consentimiento, ranking, valoraciones y actividad, pero conserva el registro de peticiones. Todo se incluye en las herramientas de privacidad de Moodle y se borra al eliminar al usuario.

## Informe
Para quien tenga «Ver el informe…». Periodo por fechas (30 días al abrir). Totales, cursos y rutas más recomendados, y registro de peticiones con usuario. Tablas descargables. «Veces mostrado» cuenta cada aparición de una tarjeta, también recargas.
