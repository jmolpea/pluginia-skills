# Configuración del tema RSMAX (1.4.2)

Ruta de los ajustes de sitio: Administración del sitio > Apariencia > Temas > RSMAX (engranaje). Diez pestañas. Los nombres son los de pantalla en español. Valores de fábrica en limites-1.4.2.md. Manual público: https://claude.ai/artifact/UgYL8Job3Sh5p6a56HMjSQ

## Pestaña «Colores y formas»
- Manual de configuración: enlace al manual público.
- Paleta preparada: escribe los cuatro colores y el carácter del sitio. Recomendación: usarla solo al empezar o sin colores de marca; con colores propios, dejar «Personalizada». Sustituye colores puestos a mano.
- Color de marca, Color de acento, Color oscuro, Fondo de la página: los cuatro que mueven todo. Recomendación: marca exacta del manual de identidad; acento que destaque sobre oscuro; oscuro de verdad oscuro; fondo muy claro.
- Color de los enlaces, Color de los botones: vacíos salvo que una parte deba apartarse de la marca.
- Texto de los botones con color de marca: dejar en automático; forzar puede romper el contraste.
- Ancho del contenido: 960 para cursos de lectura; 1280 para tablas y vídeo.
- Esquinas, Sombras: estilo general.
- Modos claro y oscuro: aviso informativo; el interruptor está en los ajustes de Boost.

## Pestaña «Inicio y bloques»
- Apertura de la página de inicio, Título de la página de inicio, Línea bajo el título: la apertura sencilla del tema. No se ve si la página tiene bloques Pluginia visibles.
- RSMAX Premium: texto informativo, solo sin bloques Pluginia instalados.
- Primer tono de franja, Segundo tono de franja, Color de las tarjetas, Fondo del hero, Resplandor del hero: colores comunes de los bloques de la página de inicio. Si se cambia el fondo de la página a mano, igualar el segundo tono.

## Pestaña «Tipografía»
- Fuente del texto, Tu propia fuente de texto, Fuente de los títulos, Tu propia fuente de títulos, Tamaño del texto, Grosor de los títulos.
- Recomendación: Inter o la del dispositivo; fuente propia solo en WOFF2 y, mejor, variable; tamaño 16 o más.

## Pestaña «Encabezado»
- Logotipos e icono del sitio (logotipo, logotipo compacto, favicon): son los de Moodle. El menú muestra el compacto. PNG con fondo transparente.
- Estilo del menú, Altura del logotipo, Logotipo en blanco sobre menú oscuro, Buscador en el menú.
- Texto del botón del menú, Enlace del botón del menú, Quién ve el botón del encabezado. Ejemplo: «Crear cuenta», /login/signup y solo visitantes.

## Pestaña «Pie de página»
- Estilo del pie, Color de fondo del pie, Color del texto del pie.
- Texto del pie (editor), Título y Enlaces de las columnas 1 a 3 (un enlace por línea, «Texto|dirección»), Línea de copyright, redes sociales, Mostrar el botón de ayuda de Moodle.
- Recomendación: dejar el copyright vacío para que el año se actualice solo; poner enlaces legales en una columna.

## Pestaña «Acceso»
- Imagen de fondo del acceso: foto apaisada, ligera y sin texto.

## Pestaña «Área personal»
- Mostrar el resumen.

## Pestaña «Cursos»
- Aula RSMAX: el diseño propio dentro de los cursos. En sitios con cursos en marcha, probar antes en un entorno de pruebas.
- Cabecera del curso con imagen, Mostrar el progreso del curso, Mostrar el progreso por sección (depende del anterior), Ancho del índice del curso, Barra de navegación en todos los formatos de curso.
- Página de presentación para matricularse, Contenido que se muestra antes de matricularse. Si los nombres de actividades no deben verse desde fuera, elegir solo secciones o nada.
- Bloques de los cursos nuevos: no cambia cursos existentes ni actúa si el sitio fijó sus bloques por defecto por otra vía.
- Cabecera de las actividades, Fondo de las actividades, Índice del curso, Correcto, Parcialmente correcto, Incorrecto: colores; dejar vacíos o de fábrica salvo necesidad.

## Pestaña «Asistente de IA» (requiere el bloque del asistente)
- Botón flotante, Texto del botón, Asistente del curso en todas las páginas del curso, Asistente del sitio en el catálogo y en las páginas de matriculación.
- El asistente del sitio queda abierto a visitantes: revisar límites y captcha en los ajustes del bloque.

## Pestaña «Avanzado»
- SCSS inicial (antes de todo, para valores internos) y SCSS adicional (al final, para reglas propias). Solo con conocimientos de CSS; guardar copia antes de cambiar.

## En cada curso
### Banners (menú del curso > Más > Banners)
- Banner del curso; Dónde se muestra el banner del curso; Aspecto de las páginas del curso (solo con el Aula apagada); Banners de las secciones (botón por sección).
### Presentación del módulo (Aula encendida, edición activada, enlace en cada sección)
- Foto o vídeo: Archivo, Dirección de un vídeo, Vídeo pendiente.
- Texto junto a la foto o el vídeo: Línea sobre el texto, Texto, Texto completo.
- Sobre este módulo: Título de la tarjeta, Línea bajo el título, Contenido (sin contenido, la tarjeta no se muestra).
- Quitar la presentación: borra la presentación y sus archivos.
### Áreas (edición activada, enlace «Añadir área» en cada sección)
- Nombre del área. Se crea al principio de la sección; se arrastra a su sitio. Se renombra o borra como un área de texto y medios.
### Etiquetas de cada actividad (ajustes de la actividad > Marcas)
- tipo: seguido de leccion, practica, evaluable, hito, lectura, foro, encuesta, activacion, cierre, material, glosario o certificado (también en inglés con type:). Otra palabra se muestra tal cual.
- duracion: seguido de número y min, m o h (también duration:). Ejemplos: duracion:30min, duracion:1.5h.
- progreso:no (o progress:no): la actividad no cuenta para el progreso.
- Tipo sin etiqueta: página y libro, lectura; archivo, URL, carpeta, material; tarea y taller, evaluable; cuestionario, evaluable si puntúa y práctica si no; lección, lección; H5P y SCORM, práctica; foro; glosario; consulta, encuesta y retroalimentación, encuesta; certificado.
### Bloques
- Zonas: ancho completo arriba, encima del contenido, debajo del contenido, ancho completo abajo, derecha y, solo al editar la página del curso, «Página de matriculación».
- Ajustes comunes de los bloques Pluginia: «Mostrar a» (todo el mundo, solo visitantes, solo usuarios identificados; se guarda como permiso del bloque y los administradores ven siempre todo) y «Colores» (sin fondo, suave, oscuro, de marca o propios).
