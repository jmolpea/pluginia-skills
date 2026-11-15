# Límites y valores de fábrica: 1.4.3

Verificados en el código de la versión 1.4.3 el 15-11-2026. «Vacío» significa que el valor se deriva de otro.

## Requisitos
| Elemento | Valor |
|---|---|
| Moodle | 5.3 únicamente (no se instala en anteriores) |
| Dependencia | Tema Boost de Moodle 5.3 |
| Idiomas | Inglés y español |
| Permisos propios, tareas programadas, informes | Ninguno |

## Colores
| Ajuste | De fábrica | Notas |
|---|---|---|
| Color de marca | #00a8d6 | |
| Color de acento | #2dd4bf | |
| Color oscuro | #2b2624 | Debe ser oscuro: lleva texto blanco encima |
| Fondo de la página | #f6f1ea | |
| Color de los enlaces, de los botones | Vacío | Derivan del color de marca |
| Primer y segundo tono de franja, tarjetas | #ffffff, #f6f1ea, #ffffff | |
| Fondo y resplandor del hero | Vacío | Color oscuro y color de marca |
| Cabecera de las actividades, fondo de las actividades, índice del curso | Vacío | Oscuro, fondo del sitio, oscuro de cabeceras |
| Correcto, parcialmente correcto, incorrecto | #4f8a63, #c98a1f, #c4573f | |
| Fondo y texto del pie | Vacío | Los del estilo de pie |
- Formato admitido por el tema: hexadecimal con almohadilla, de 3, 6 u 8 dígitos. Un color escrito de otra forma (nombre, rgb) no se aplica y queda el de fábrica.
- Contraste que busca el tema para el texto sobre color: 4,5 a 1.
- Paletas preparadas: 8 (Cálida, Pizarra, Bosque, Océano, Marino, Ciruela, Arena, Grafito) más «Personalizada».

| Paleta | Marca | Acento | Oscuro | Fondo | Además cambia |
|---|---|---|---|---|---|
| Cálida | #00a8d6 | #2dd4bf | #2b2624 | #f6f1ea | Nada más |
| Pizarra | #2563eb | #38bdf8 | #1e293b | #f1f5f9 | Cabeceras, hero, índice y pie azules |
| Bosque | #2f7d5b | #e0b34a | #1f2a24 | #f3f1e7 | Cabeceras, hero, índice y pie verdes |
| Océano | #0f766e | #fb923c | #134e4a | #f0f7f6 | Cabeceras, hero, índice; menú del color de marca |
| Marino | #c2410c | #f5b94a | #172554 | #f5f3ee | Cabeceras, hero, índice; menú oscuro |
| Ciruela | #9d3f8f | #f0a6ca | #2a1f2d | #f7f1f4 | Cabeceras, hero, índice; pie del color de marca |
| Arena | #b4532a | #84a98c | #3b2f2a | #faf6f0 | Cabeceras, hero, índice; pie claro |
| Grafito | #18181b | #f59e0b | #18181b | #f4f4f5 | Enlaces y botones ámbar, cabeceras; pie claro |

## Formas, anchos y tipografía
| Ajuste | Valores | De fábrica |
|---|---|---|
| Ancho del contenido | 830, 960, 1120, 1280 px | 1280 |
| Ancho del índice del curso | 285, 320, 360 px | 320 |
| Esquinas | Rectas, ligeramente redondeadas, redondeadas, redondeadas con botones píldora | Ligeramente redondeadas |
| Sombras | Sí o no | Sí |
| Texto de los botones | Automático, blanco, oscuro | Automático |
| Fuente del texto | Inter, la de cada dispositivo, Noto Sans, propia | Inter |
| Fuente de los títulos | La misma que el texto, Inter, dispositivo, Noto Sans, propia | La misma |
| Fuente propia | 1 archivo WOFF2 por campo | Sin archivo |
| Tamaño del texto | 14 a 18 px | 16 |
| Grosor de los títulos | 500, 600, 700, 800 | 700 |

## Encabezado y pie
| Ajuste | Valores | De fábrica |
|---|---|---|
| Logotipo y logotipo compacto | 1 archivo JPG o PNG cada uno (ajustes de Moodle) | Sin archivo |
| Favicon | 1 imagen (ajuste de Moodle) | Sin archivo |
| Estilo del menú | Claro, oscuro, color de marca | Claro |
| Altura del logotipo | 28, 32, 36, 40, 48, 56 px | 36 |
| Logotipo en blanco sobre menú oscuro | Sí o no | Sí |
| Buscador en el menú | Sí o no | Sí |
| Botón del menú | Texto y enlace; enlace completo o que empiece por / | Vacío (sin botón) |
| Quién ve el botón | Solo quien no ha iniciado sesión, todos | Solo quien no ha iniciado sesión |
| Estilo del pie | Claro, oscuro, color de marca | Oscuro |
| Columnas de enlaces | 3 como máximo; un enlace por línea «Texto|dirección» | Vacías |
| Redes sociales | Facebook, X, LinkedIn, YouTube, Instagram, TikTok; dirección completa | Vacías |
| Botón de ayuda de Moodle | Sí o no | Sí |
| Imagen de fondo del acceso | 1 imagen web | Sin imagen |

## Cursos, área personal y asistente
| Ajuste o comportamiento | Valor |
|---|---|
| Aula RSMAX | Sí en instalaciones nuevas; no en sitios que actualizan desde una versión anterior a la que la introdujo y nunca la habían configurado |
| Cabecera del curso, progreso del curso, progreso por sección, barra en todos los formatos | Sí |
| Página de presentación para matricularse | Sí |
| Contenido antes de matricularse | Nada, secciones con número de actividades (de fábrica), secciones con nombres de actividades |
| Profesores en la página de matriculación | 6 como máximo |
| Bloques de los cursos nuevos | Personas, próximos eventos, valoración del curso y asistente de IA, los que estén instalados |
| Resumen del área personal | Sí; hasta 5 cursos con progreso; vencimientos a 7 días |
| «Cómo va el grupo» | Aviso por debajo del 50 %; 5 alumnos como máximo; caché de 5 minutos |
| Mapa de módulos | 12 módulos por fila; 6 en móvil |
| Código corto de sección | Hasta 8 caracteres antes de « · » |
| Asistente: botón flotante, en páginas del curso, en catálogo y matriculación | Sí los tres; texto del botón vacío («Asistente de IA») |
| SCSS inicial y adicional | Vacíos |

## En el curso
| Elemento | Límite |
|---|---|
| Banner del curso y de cada sección | 1 imagen web cada uno; recomendado 1600 × 320 px |
| Dónde se muestra el banner | Solo página principal (de fábrica) o todas las páginas |
| Aspecto de las páginas | Escenario (de fábrica) o claro; solo con el Aula apagada |
| Presentación: archivo | 2 archivos como máximo (imagen o vídeo, y subtítulos VTT); tamaño máximo, el del curso |
| Presentación: dirección de vídeo | Debe empezar por http o https; YouTube y Vimeo se incrustan |
| Presentación: línea sobre el texto, vídeo pendiente, título y línea de la tarjeta | 255 caracteres cada uno (1333 la dirección del vídeo); el formulario avisa si se supera |
| Nombre de un área | 120 caracteres |
| Etiqueta de duración | Número (con decimales) seguido de min, m o h |
| Caché de imágenes de banner en el navegador | Hasta 30 días; una imagen nueva cambia de dirección y se ve al momento |
