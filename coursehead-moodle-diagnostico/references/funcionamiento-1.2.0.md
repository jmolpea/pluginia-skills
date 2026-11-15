# Funcionamiento verificado: versión 1.2.0

Revisión estática del código que declara 1.2.0 (versión interna 2026100400), para Moodle 4.5 a 5.3. Revisado el 15-11-2026.
Manual público: https://claude.ai/artifact/S1C8aFgCzaqxcegdHXqanX
Todo lo que sigue son hechos leídos en el código, salvo lo marcado como «No verificado».

## Qué es
Plugin local de Moodle. Permite guardar, para cada curso, un texto de CSS y un texto de JavaScript, y hace que las páginas de ese curso los carguen. No añade actividades ni bloques. No usa inteligencia artificial ni servicios externos. No tiene tareas programadas.

## Flujo completo
1. El administrador decide en los ajustes del sitio si el plugin está encendido, si se permite CSS y si se permite JavaScript.
2. Una persona con permiso abre, dentro del curso, la página «Recursos personalizados del curso» (menú «Más» del curso), escribe el código, marca las casillas y guarda.
3. Al guardar, el plugin valida el código, lo almacena, genera una revisión nueva (16 caracteres) y anota un evento en los registros de Moodle.
4. Cada vez que alguien abre una página del curso que cumple las condiciones, Moodle añade en la cabecera de la página una referencia a la hoja de estilos del curso y otra a su programa, cada una con la revisión en su dirección. El código no va incrustado en la página.
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
- Aviso de seguridad amarillo cuando se puede editar JavaScript y «Mostrar advertencias de seguridad» está encendido. Al marcar la casilla de JavaScript aparece además una notificación, que no depende de ese ajuste.
- Botón «Eliminar los recursos personalizados del curso»: solo aparece si hay registro; pide confirmación; borra CSS y JavaScript de forma definitiva.
- La página funciona aunque el plugin esté apagado en el sitio: se puede editar y guardar, pero no se aplica nada hasta encenderlo.
- Desde el 15-11-2026 el código en preparación añade un enlace «Manual de configuración» en los ajustes del sitio y al principio de este formulario; puede no estar en el ZIP 1.2.0 instalado.

## Validación al guardar
- Se rechaza el texto que contenga, en mayúsculas o minúsculas, alguno de estos fragmentos: apertura o cierre de etiqueta style, apertura o cierre de etiqueta script, apertura de PHP o cierre de PHP. Mensaje: «El código no debe contener "…". Pegue únicamente reglas CSS o JavaScript sin etiquetas HTML ni PHP.»
- Se rechaza el texto más largo que la longitud máxima configurada. Mensaje: «El código supera la longitud máxima permitida de N caracteres.»
- La búsqueda es literal: no entiende el lenguaje. Un programa correcto que contenga esas letras seguidas se rechaza igual (ver límites).
- No se comprueba que el CSS o el JavaScript sean correctos. No se modifica ni se limpia el texto.
- Al guardar se vuelve a validar todo el registro, incluido lo que la persona no ve por falta de permiso. Si falla, aparece «El código enviado no superó la validación y no se ha guardado.»

## Permisos y roles
Tres permisos, a nivel de curso, concedidos de fábrica solo al rol Gestor (el administrador del sitio puede todo):
- «Gestionar los recursos personalizados del curso» (local/coursehead:manage): ver el enlace del menú, entrar a la página, usar el interruptor del curso y eliminar.
- «Editar el CSS personalizado del curso» (local/coursehead:managecss).
- «Editar el JavaScript personalizado del curso (solo usuarios de confianza)» (local/coursehead:managejs).
Sin el primero no se entra a la página aunque se tengan los otros. Quien tiene el primero puede eliminar todo, también lo que no puede editar.
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

## No verificado
- Comportamiento real en un Moodle concreto: esto es lectura de código, no una prueba de ejecución.
- Posición exacta de las referencias en la cabecera respecto a las hojas de estilo del tema.
- Compatibilidad con temas, formatos de curso o plugins concretos de terceros.
