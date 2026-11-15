# Funcionamiento verificado: versión 1.2.1

Revisión estática del código que declara 1.2.1 (versión interna 2026111500), para Moodle 4.5 a 5.3. Revisado el 15-11-2026.
Manual público: https://claude.ai/artifact/S1C8aFgCzaqxcegdHXqanX
Todo lo que sigue son hechos leídos en el código, salvo lo marcado como «No verificado».

## Cambios de 1.2.0 a 1.2.1
- Validación: 1.2.0 rechazaba cualquier texto que contuviera las letras de apertura de una etiqueta script o style, aunque fuera una comparación de JavaScript; 1.2.1 solo rechaza etiquetas completas.
- Guardado: 1.2.0 revalidaba también el contenido guardado que quien edita no ve, y podía bloquear el guardado con «El código enviado no superó la validación…»; 1.2.1 valida solo lo que se envía.
- Eliminar: en 1.2.0 bastaba el permiso de gestionar; en 1.2.1 hace falta además el permiso de edición de cada tipo de código guardado.
- Contenido solo con espacios: en 1.2.0 se guardaba tal cual y la página pedía un archivo que respondía «no encontrado»; en 1.2.1 se guarda como vacío. Lo guardado con 1.2.0 sigue igual hasta que se vuelva a guardar el curso.
- Aviso de seguridad de JavaScript: en 1.2.0 salía dos veces (sobre el formulario y dentro de él); en 1.2.1, una, sobre el formulario.
- Enlace «Manual de configuración» en los ajustes del sitio y al principio del formulario del curso: nuevo en 1.2.1.
- La descripción de «Rutas excluidas» explica ahora que el resto de páginas del curso reciben siempre los recursos.
- Sin cambios en la base de datos ni en los valores de fábrica.

## Qué es
Plugin local de Moodle. Permite guardar, para cada curso, un texto de CSS y un texto de JavaScript, y hace que las páginas de ese curso los carguen. No añade actividades ni bloques. No usa inteligencia artificial ni servicios externos. No tiene tareas programadas.

## Flujo completo
1. El administrador decide en los ajustes del sitio si el plugin está encendido, si se permite CSS y si se permite JavaScript.
2. Una persona con permiso abre, dentro del curso, la página «Recursos personalizados del curso» (menú «Más» del curso), escribe el código, marca las casillas y guarda.
3. Al guardar, el plugin valida el código enviado, lo almacena, genera una revisión nueva (16 caracteres) y anota un evento en los registros de Moodle.
4. Cada vez que alguien abre una página del curso que cumple las condiciones, Moodle añade en la cabecera de la página una referencia a la hoja de estilos del curso y otra a su programa, cada una con la revisión en su dirección. El código no va incrustado en la página. Estas referencias quedan antes que las hojas de estilo del tema (comprobado en el núcleo de Moodle 5.3).
5. El navegador pide esas dos direcciones. El plugin comprueba en cada petición que la persona puede entrar al curso y entonces entrega el contenido.
6. El navegador aplica el CSS y ejecuta el JavaScript.

## Las condiciones para que una referencia aparezca en la página
Todas a la vez:
- «Habilitar el plugin» encendido en el sitio.
- La página pertenece a un curso que no es la portada del sitio.
- La página no usa un diseño de administración, de acceso, de mantenimiento, de redirección ni incrustado. Las pantallas de administración del curso (por ejemplo, editar ajustes del curso, o la propia página del plugin) quedan fuera.
- La ruta de la página no empieza por ninguna línea de «Rutas excluidas».
- Según el tipo de página: si es de calificaciones, «Inyectar en páginas de calificaciones» encendido; si es una actividad, «Inyectar en páginas de actividades» encendido; si es la página principal del curso o de una sección, «Inyectar en la página principal del curso» encendido. Cualquier otra página del curso (por ejemplo, participantes) no depende de ninguna de las tres casillas.
- En el curso: «Habilitar recursos personalizados para este curso» marcado.
- Para el CSS: «Permitir CSS personalizado» en el sitio, «Habilitar CSS personalizado» en el curso y que haya CSS guardado.
- Para el JavaScript: «Permitir JavaScript personalizado» en el sitio, «Habilitar JavaScript personalizado» en el curso y que haya JavaScript guardado.
No se añade nada en peticiones internas de Moodle (servicios web, llamadas en segundo plano, línea de comandos) ni durante una instalación o actualización.
Si el plugin sufre un error interno al preparar la cabecera, la página se muestra igualmente sin los recursos; solo queda un aviso para desarrolladores.

## Entrega del CSS y del JavaScript
- Solo se entregan a quien puede entrar al curso (incluye invitados si el curso los admite). A quien no puede, se le responde «prohibido»; nunca se le redirige a la página de acceso.
- Si el plugin, el tipo de recurso o el curso están desactivados, o el contenido está vacío, la respuesta es «no encontrado».
- Con la revisión correcta en la dirección, el navegador puede guardar el archivo hasta 7 días, en caché privada. Como cada guardado cambia la revisión, el cambio se ve en la siguiente página que se abra.
- Con una revisión antigua o sin ella, se entrega el contenido actual y se obliga al navegador a revalidar.
- El JavaScript se entrega con una primera línea de comentario generada por el plugin que indica el número del curso.
- Todos los participantes reciben el mismo contenido. No lleva datos de la persona.
- Cualquier participante puede leer ese CSS y ese JavaScript desde su navegador: no es un lugar para secretos.

## La página del curso
- Panel «Estado actual»: sin registro guardado dice «Todavía no hay recursos personalizados configurados para este curso». Con registro muestra «Activado» o «Desactivado» (interruptor del curso), la «URL del recurso CSS» y la «URL del recurso JavaScript» solo cuando cada uno se serviría (permitido en el sitio, habilitado en el curso y con contenido), y la «Revisión».
- Formulario con tres apartados: «Configuración de recursos del curso», «CSS personalizado» y «JavaScript personalizado».
- Si el sitio no permite un tipo o el rol no tiene el permiso, en ese apartado aparece «La edición de CSS no está disponible…» o «La edición de JavaScript no está disponible…», y lo guardado en ese apartado se conserva sin cambios al guardar el resto.
- Aviso de seguridad amarillo, una sola vez y encima del formulario, cuando se puede editar JavaScript y «Mostrar advertencias de seguridad» está encendido. Al marcar la casilla de JavaScript aparece además una notificación, que no depende de ese ajuste.
- Botón «Eliminar los recursos personalizados del curso»: solo aparece si hay registro y quien lo ve puede editar cada tipo de código guardado (si hay CSS, el permiso de CSS; si hay JavaScript, el de JavaScript; no depende de los interruptores del sitio). Pide confirmación y borra CSS y JavaScript de forma definitiva.
- La página funciona aunque el plugin esté apagado en el sitio: se puede editar y guardar, pero no se aplica nada hasta encenderlo.
- Enlace «Manual de configuración» al principio del formulario y de los ajustes del sitio; se abre en una pestaña nueva.

## Validación al guardar
- Se rechaza el texto que contenga, en mayúsculas o minúsculas, una etiqueta style o script de apertura o de cierre. Cuenta como etiqueta el nombre completo seguido de un espacio, un salto de línea, una barra, el signo «mayor que» o el final del texto; con o sin atributos. Un nombre más largo o seguido de un punto (como una variable llamada scripts) no es una etiqueta.
- Se rechaza también, de forma literal, la marca de apertura de PHP y la de cierre (interrogación seguida de «mayor que»). Mensaje para ambos casos: «El código no debe contener "…". Pegue únicamente reglas CSS o JavaScript sin etiquetas HTML ni PHP.»
- Se rechaza el texto más largo que la longitud máxima configurada. Mensaje: «El código supera la longitud máxima permitida de N caracteres.»
- La validación no entiende el lenguaje: quedan falsos positivos residuales (ver límites).
- No se comprueba que el CSS o el JavaScript sean correctos. No se modifica ni se limpia el texto, con una excepción: un campo que solo contiene espacios o líneas en blanco se guarda vacío.
- Solo se valida lo que se envía. El contenido guardado que quien edita no ve (por falta de permiso o porque el sitio no permite ese tipo) se conserva sin revisarlo y no puede bloquear el guardado. El mensaje «El código enviado no superó la validación y no se ha guardado.» queda como segunda barrera y no debería verse en el uso normal del formulario.

## Permisos y roles
Tres permisos, a nivel de curso, concedidos de fábrica solo al rol Gestor (el administrador del sitio puede todo):
- «Gestionar los recursos personalizados del curso» (local/coursehead:manage): ver el enlace del menú, entrar a la página y usar el interruptor del curso.
- «Editar el CSS personalizado del curso» (local/coursehead:managecss).
- «Editar el JavaScript personalizado del curso (solo usuarios de confianza)» (local/coursehead:managejs).
Sin el primero no se entra a la página aunque se tengan los otros. Para eliminar hace falta el primero y, además, el de edición de cada tipo de código guardado: quien no puede editar el JavaScript de un curso tampoco puede borrarlo.
Qué ve cada rol de fábrica: gestor y administrador, la página completa (JavaScript solo si el sitio lo permite); profesorado y alumnado, nada del plugin, solo el curso personalizado.

## Qué se guarda
Un registro por curso: los tres interruptores del curso, el CSS, el JavaScript, la estrategia de carga, la revisión y las fechas de creación y modificación. No se guarda quién lo escribió ni ningún dato personal; el plugin lo declara así a la API de privacidad de Moodle.
Quién hizo cada cambio y cuándo queda en los registros estándar de Moodle (eventos de creación, actualización y eliminación), sin el contenido del código.
Una caché interna de Moodle guarda un resumen por curso; se renueva al guardar, al eliminar y al cambiar los tres interruptores generales del sitio.

## Copias de seguridad, restauración y borrado
- La copia de seguridad del curso incluye sus recursos.
- Al restaurar (también al duplicar o importar una copia): el CSS solo se restaura si quien restaura tiene el permiso de editar CSS en el curso de destino; el JavaScript, igual con su permiso. El contenido se vuelve a validar con los límites del sitio de destino. Lo descartado se avisa en el registro de la restauración.
- Si el curso de destino ya tiene un registro de recursos, se conserva el del destino y se ignora el de la copia (con aviso informativo en el registro de la restauración).
- La revisión se genera de nuevo al restaurar.
- Al borrar un curso, sus recursos se eliminan.

## Página de información del curso
La página de información que ve quien aún no está matriculado pertenece al curso, así que recibe las referencias; pero el archivo solo se entrega a quien puede entrar, de modo que esa persona no ve la personalización y su navegador registra una petición denegada. Es inofensivo. Se evita añadiendo /course/info.php a «Rutas excluidas». La página de matriculación no recibe referencias.

## No verificado
- Comportamiento real en un Moodle concreto: esto es lectura de código, no una prueba de ejecución. Las pruebas automáticas añadidas en 1.2.1 no se han ejecutado en esta revisión.
- Posición de las referencias respecto al CSS del tema en Moodle 4.5 a 5.2 (en 5.3 sí: van antes).
- Compatibilidad con temas, formatos de curso o plugins concretos de terceros.
