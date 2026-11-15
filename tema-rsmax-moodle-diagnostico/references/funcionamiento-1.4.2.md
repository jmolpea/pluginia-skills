# Cómo funciona el tema RSMAX: 1.4.2

Revisión estática del código de la versión 1.4.2 (interna 2026111400), hecha el 15-11-2026. Todo lo que sigue es hecho verificado en el código salvo donde se indica «hipótesis» o «no verificado».

## Qué es
- Un tema hijo de Boost para Moodle 5.3. Boost debe estar instalado (viene con Moodle). No se instala en versiones anteriores.
- Funciona sin ningún otro plugin. El paquete premium añade 17 bloques Pluginia (dependen del tema) y plugins de IA independientes.
- No tiene permisos propios, tareas programadas, informes ni servicios web. No es un plugin de IA: no envía nada a ningún proveedor de IA.
- Idiomas incluidos: inglés y español.

## Cómo llegan los ajustes a la pantalla
1. El administrador guarda una pestaña de ajustes (Administración del sitio > Apariencia > Temas > RSMAX).
2. Cada ajuste, al cambiar, vacía las cachés del tema; Moodle recalcula la hoja de estilos en la siguiente carga. La primera página tras guardar puede tardar más o salir con los estilos anteriores: se arregla recargando.
3. Antes de usarse, cada valor se comprueba: los colores deben ser hexadecimales y el resto se toma de listas cerradas. Un valor no válido se descarta en silencio y se usa el de fábrica.
4. Moodle guarda solo la pestaña abierta: lo cambiado en otra pestaña sin guardar se pierde.

## Colores
- Cuatro colores principales (marca, acento, oscuro, fondo) dibujan todo el sitio. Los demás ajustes de color vienen vacíos y se derivan de ellos.
- El texto sobre un color (botones, índice, pie) lo pone el tema en blanco u oscuro buscando un contraste de 4,5 a 1. El color de marca usado como texto se oscurece lo necesario.
- Paleta preparada: al cambiar el desplegable y guardar, el tema escribe los cuatro colores, los colores y estilos que esa paleta nombra (cabeceras, portada, índice, pie, estilo del menú y del pie, según la paleta) y devuelve a su valor de fábrica los demás colores derivados. Se aplica al terminar de guardar el formulario, por encima de los colores que el formulario mostraba. «Personalizada» no cambia nada.
- La paleta solo actúa cuando el valor del desplegable cambia. Volver a guardar la misma paleta no la reaplica (comportamiento estándar de los ajustes de Moodle; probable, no probado en vivo).
- El logotipo no forma parte de la paleta.
- Modo oscuro: es una función de Moodle que se activa en los ajustes de Boost (pestaña de ajustes experimentales). RSMAX solo informa de si está activo y dibuja su versión oscura a partir del color oscuro. Cada persona con sesión elige claro, oscuro o sistema; visitantes e invitados ven el modo por defecto.

## Encabezado y pie
- El menú usa el logotipo compacto de Moodle. Los tres archivos (logotipo, logotipo compacto, favicon) son los ajustes del propio Moodle, repetidos en la pestaña Encabezado.
- Con menú oscuro o de marca, y la opción de logotipo en blanco activa, el logotipo se pinta como silueta blanca.
- El buscador del menú usa la búsqueda global si está activada y la persona puede usarla; si no, busca cursos. No se muestra a visitantes en sitios que obligan a iniciar sesión.
- El botón del menú se muestra solo con texto y enlace válidos. Según el ajuste de audiencia, a todos o solo a quien no ha iniciado sesión (visitantes e invitados).
- Pie: texto con formato, hasta 3 columnas de enlaces, redes con dirección, línea de copyright (vacía: símbolo, año actual y nombre del sitio). Una columna sin enlaces válidos no se muestra. Las líneas mal formadas se ignoran sin aviso.

## Página de inicio y área personal
- Apertura de la página de inicio: título (o nombre del sitio), frase, buscador de cursos, botón al catálogo y un segundo botón (acceso para visitantes, área personal para quien tiene sesión). Se retira sola si la página tiene a la vista algún bloque Pluginia con contenido para esa persona.
- Zonas de bloques a lo ancho en inicio, área personal, mis cursos, página del curso y categorías: ancho completo arriba, encima del contenido, debajo del contenido, ancho completo abajo; además del panel lateral derecho.
- Resumen del área personal: saludo, cursos en marcha y completados, lo que vence en los próximos 7 días y el curso con el que continuar. Calcula el progreso de hasta 5 cursos (los visitados más recientemente). No se muestra a invitados ni al editar.
- Al instalar, el tema ordena el área personal por defecto del sitio (línea de tiempo, vista general de cursos y recomendador si existe). No toca las áreas personales ya personalizadas.

## Dentro de un curso
- Progreso: requiere finalización activada en el curso, que la persona sea seguida por la finalización y al menos una actividad con finalización. Cuentan las actividades visibles para el alumno y las de secciones bloqueadas que se le muestran en gris con su condición. No cuentan las ocultas ni las marcadas con la etiqueta de exclusión.
- El progreso por sección necesita, además de su ajuste, que el progreso del curso esté activado.
- Con el modo de edición activado no se muestran cabecera con imagen, progreso, mapa ni cabeceras de actividad.
- Cabecera del curso: banner (o imagen del curso), categoría, profesorado, progreso y actividad con la que continuar.
- Aula RSMAX (ajuste de sitio): páginas claras en todos los cursos; cabecera «tu siguiente paso» con mapa de módulos (hasta 12 en fila; 6 en móvil); áreas; presentación de cada módulo; tipo y duración de cada actividad; panel de entrega en las tareas; preguntas sugeridas para el asistente; y, para quien no puede editar el curso, el menú del curso reducido a «Curso» y «Mis entregas» (las calificaciones).
- «Siguiente paso»: la primera actividad sin completar en orden de curso; con el Aula, la última actividad sin terminar que el alumno visitó (se consulta el registro estándar de Moodle), si sigue disponible.
- Módulos: toda sección salvo la primera, que se trata como recursos generales. Un nombre de sección «código · título» con código de hasta 8 caracteres muestra el código en el mapa.
- Cabeceras de actividad y de sección: tipo de actividad, nombre, lugar en la sección y progreso. El ancho de las páginas de actividad es común, salvo en las de tabla grande (calificación de tareas, edición e informes de cuestionario, asignación de taller).
- Barra anterior/siguiente: la de Moodle en formatos que la admiten; el tema la añade en los demás si el ajuste está activo. No se añade al editar, con otra barra fija abajo, ni en actividades ocultas para quien no puede verlas.
- Calificaciones del alumno: resumen leído de la propia tabla de Moodle (no consulta notas aparte, así que lo oculto sigue oculto). Docente: «Cómo va el grupo» sobre el calificador, con media, porcentaje calificado, aprobados por actividad y hasta 5 alumnos por debajo del 50 %. Requiere poder ver las notas de todos y, con grupos separados, acceder a todos los grupos. Se guarda en caché 5 minutos y se renueva al calificar.

## Lo que configura el docente
- Banners (menú del curso > Más > Banners; requiere poder editar los ajustes del curso): banner del curso, dónde se muestra, aspecto de las páginas (solo con el Aula apagada) y un banner por sección. Una sección con banner propio usa el suyo en su página y sus actividades.
- Presentación del módulo (con el Aula, en edición, enlace en cada sección): foto o vídeo, texto, texto completo y tarjeta «Sobre este módulo». YouTube y Vimeo se incrustan (YouTube en su dominio sin cookies); otra dirección se muestra como enlace.
- Áreas (en edición, enlace bajo las actividades de cada sección; requiere poder gestionar actividades): crea un área de texto y medios marcada como área, al principio de la sección. Agrupa visualmente las actividades siguientes. No afecta a progreso, restricciones ni finalización.
- Etiquetas en las marcas de cada actividad: tipo, duración y exclusión del progreso (ver configuracion.md).

## Página de matriculación
- Con el ajuste activo, la página de opciones de matriculación se presenta como ficha del curso: descripción, contenido (según ajuste), hasta 6 profesores, fechas, campos personalizados visibles, etiquetas, cierre de matrícula (métodos de automatrícula y de pago), valoración media si existe el bloque de valoración, y precio o «Gratis». Los formularios son los de cada método de Moodle.
- El contenido lista lo visible en la página del curso aunque tenga restricciones de acceso; lo oculto no se anuncia.
- Los bloques de esa página se colocan desde la página del curso, en una zona visible solo al editar.

## Asistente de IA (solo si está instalado el bloque del asistente)
- El tema lo coloca una vez: lo añade a los bloques de cursos nuevos y crea uno del sitio en la página de inicio, abierto a visitantes.
- El del curso se lleva a todas las páginas del curso salvo durante un intento de cuestionario; el del sitio, al catálogo, categorías y páginas de matriculación. Nunca hay dos en una página. Un asistente oculto en la página del curso sigue oculto.
- Con botón flotante, el chat se abre desde un botón abajo a la derecha. Quién puede usarlo lo deciden los permisos y ajustes del bloque.

## Qué se guarda y qué no
- Por curso: banners, dónde se muestran, aspecto de las páginas y la presentación de cada módulo con sus archivos. Se incluyen en la copia de seguridad y la restauración del curso, y se borran al borrar el curso o la sección.
- No guarda datos personales. Al cargar una página no pide nada a otros sitios; la fuente Inter va incluida. Solo un vídeo externo incrustado se carga desde su servicio.
- Los archivos de banners y presentaciones se sirven a quien puede entrar en el curso.
